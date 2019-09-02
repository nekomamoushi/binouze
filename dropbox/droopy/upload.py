
import argparse
import os
try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path  # python 2 backport

import dropbox


TOKEN = ''
TARGET_PATH = ''


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "upload_file",
        type=Path,
        help="File to upload",
    )

    p = parser.parse_args()

    if not p.upload_file.exists():
        exit("ERROR: {file} does not exists.".format(file=p.upload_file))

    if not p.upload_file.is_file():
        exit("ERROR: {file} should be a file not a directory.".format(file=p.upload_file))

    return p.upload_file


def connect():
    TOKEN = os.environ.get('DROPBOX_TOKEN', None)
    if not TOKEN:
        exit("ERROR: you didn't set your access token.")

    dbx = dropbox.Dropbox(TOKEN)

    try:
        dbx.users_get_current_account()
        return dbx
    except dropbox.exceptions.AuthError as e:
        exit("ERROR: Invalid dropbox token")


def upload(dbx, file, folder='/', overwrite=False):
    target_folder = folder + file.name
    with file.open('rb') as f:
        data = f.read()
    try:
        res = dbx.files_upload(
            data,
            target_folder
        )
    except dropbox.exceptions.ApiError as err:
        exit('ERROR: API error', err)

    return res


if __name__ == "__main__":
    main()
