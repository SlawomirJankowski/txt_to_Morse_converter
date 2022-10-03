import os
from flask import Flask, render_template, request, flash, redirect, url_for, send_file, Markup
from scheduler import clean_files_and_log_to_file, send_email
from flask_apscheduler import APScheduler
from converter import Converter
from data import SCHEDULER_PARAMS, APP_SECRET_KEY, CONVERTER_ERROR_MSG
from statistics import Statistics


app = Flask(__name__)
app.secret_key = APP_SECRET_KEY
# make Config and pass apscheduler options and flask options, split data for config and data

scheduler = APScheduler()
scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()

stats = Statistics()


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        stats.add_converts()
        text_from_user = request.form.get('txt_to_convert')
        if not text_from_user:
            flash(CONVERTER_ERROR_MSG['NO_TEXT_MSG'])
            return redirect(url_for('home'))
        else:
            try:
                converter = Converter(input_text=text_from_user)
                converter.save_sound()
                return render_template('index.html',
                                       converted_text=converter.converted_text,
                                       text_from_user=text_from_user,
                                       file_path=converter.file_path)
            except KeyError as e:
                flash(f'{CONVERTER_ERROR_MSG["KEY_ERROR_MSG"]}{e}')
                return redirect(url_for('home'))

    return render_template('index.html')


@app.route('/download')
def download():
    stats.add_downloads()
    file_path = request.args.get('file_path')
    return send_file(path_or_file=file_path, as_attachment=True)


@app.route('/reset')
def reset():
    file_path = request.args.get('file_path')
    os.remove(path=file_path)  ## usuwa plik
    os.rmdir(path=file_path[:25])  ## usuwa katalog
    return redirect(url_for('home'))


@app.route('/log')
def show_log():
    try:
        return send_file(path_or_file=SCHEDULER_PARAMS['DELETE_LOG_FILE_PATH'])
    except FileNotFoundError:
        return Markup('<h1>File Not Found</h1>')


# -- APScheduler JOBS --

@scheduler.task('interval', id='clean_media_dir', seconds=(SCHEDULER_PARAMS['CLEAN_MEDIA_DIR_INTERVAL'] * 60))  # replace 0.1 with CLEAN_MEDIA_DIR ....
def clean_media_dir():
    clean_files_and_log_to_file()


@scheduler.task('cron', id='test', week='*', day_of_week='*', hour='23', minute='59')
def send_statistics():
    stats.update_total_stats()
    # wysyła e-mail ze statystykami dziennymi i całkowitymi - liczba konwersji i pobrań plików wave
    send_email(message=stats.create_statistics_message())
    stats.clear_daily_stats()


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)  # use_reloader=False to disable twice execution of scheduler in debug mode
