import time
from playsound import playsound

from morse_converter import convert_to_morse
from morse_to_wave_generator import save_sound, generate_path
from flask import Flask, render_template, request, flash, send_from_directory, redirect, url_for, send_file
import os

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text_from_user = request.form.get('txt_to_convert')
        if not text_from_user:
            pass  # add flash message
        else:
            converted_text = convert_to_morse([*text_from_user.upper()])
            file_path = generate_path()
            print(file_path)
            save_sound(converted_text=converted_text, file_path=file_path)
            return render_template('index.html',
                                   converted_text=converted_text,
                                   text_from_user=text_from_user,
                                   file_path=file_path)

    return render_template('index.html')


@app.route('/download')
def download():
    file_path = request.args.get('file_path')
    return send_file(path_or_file=file_path, as_attachment=True)


@app.route('/reset')
def reset():
    path = request.args.get('file_path')
    os.remove(path=path) ## usuwa plik
    os.rmdir(path=path[:25]) ## usuwa katalog
    return redirect(url_for('home'))


## Clean temporary folder IF BACK on browser (scheduler or with closing) https://stackoverflow.com/questions/24612366/delete-an-uploaded-file-after-downloading-it-from-flask
## https://viniciuschiele.github.io/flask-apscheduler/ !!!!

## Add copy to clipboard button

if __name__ == "__main__":
    app.run(debug=True)
