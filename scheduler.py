import os
import datetime
from data import SCHEDULER_PARAMS, MAIL_NOTIFICATION_PARAMS, CONVERTER_PATHS
import smtplib


def log_to_file(file, data):
    try:
        with open(file, 'a') as log_file:  # mode 'a' append - dopisanie do istniejących danych
            log_file.write(data)

    except FileNotFoundError:
        with open(file, 'w') as log_file:
            log_file.write(data)


def clean_files_and_log_to_file():
    timestamp = datetime.datetime.now()
    del_counter = 0
    subfolders = [folder.path for folder in os.scandir(CONVERTER_PATHS['PARENT_DIR']) if folder.is_dir()] # get list of subfolders
    for subfolder in subfolders:
        path_to_file = f'{subfolder}/converted_text_as_sound.wav'
        try:
            file_modification_time = os.path.getmtime(path_to_file)  # get file modification time
        except FileNotFoundError:
            os.rmdir(path_to_file[:25])
        else:
            if (timestamp.timestamp() - file_modification_time)/60 > SCHEDULER_PARAMS['FILE_LIFETIME']:
                os.remove(path_to_file)      ## usuwa plik
                os.rmdir(path_to_file[:25])  ## usuwa katalog
            del_counter += 1

    log_data = f'Delete date: {timestamp} | Number of deleted files: {del_counter} \n'
    log_to_file(file=SCHEDULER_PARAMS['DELETE_LOG_FILE_PATH'], data=log_data)


def send_email(message):
    with smtplib.SMTP(MAIL_NOTIFICATION_PARAMS['SERVER']) as conn:
        conn.starttls()
        conn.login(user=MAIL_NOTIFICATION_PARAMS['SENDER_EMAIL'], password=MAIL_NOTIFICATION_PARAMS['PASSWORD'])
        conn.sendmail(
            from_addr=MAIL_NOTIFICATION_PARAMS['SENDER_EMAIL'],
            to_addrs=MAIL_NOTIFICATION_PARAMS['RECEIVER_EMAIL'],
            msg=f"Subject:TXT to Morse server statistics.\n\n{message}"
        )
