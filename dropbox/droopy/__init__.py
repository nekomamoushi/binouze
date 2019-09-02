from .upload import parse_args, connect, upload


def main():
    upload_file = parse_args()
    dbx = connect()
    upload(dbx, upload_file)
