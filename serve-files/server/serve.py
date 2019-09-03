
import argparse
import os

try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path  # python 2 backport

import bottle


app = bottle.Bottle()
config = {
    "host": '0.0.0.0',
    "port": '8193'
}
file_to_serve = None


def parse_args():
    parser = argparse.ArgumentParser()
    parser. add_argument(
        '-d', '--debug',
        action='store_true'
    )
    parser.add_argument(
        "file",
        type=Path,
        help="File to serve",
    )

    return parser.parse_args()


def validate_args(args):

    def resolve_filename(file):
        resolved_file = file.expanduser()
        resolved_file.resolve()
        if str(resolved_file.parent) == '.':
            current_dir = Path.cwd()
            resolved_file = Path(current_dir) / resolved_file.name
        return resolved_file

    file = resolve_filename(args.file)
    debug = args.debug

    if not file.exists():
        exit("ERROR: {file} does not exists.".format(file=file))
    if not file.is_file():
        exit("ERROR: {file} should be a file not a directory.".format(file=file))

    return (file, debug)


def generate_url(config, file):
    return "http://{host}:{port}/{filename}".format(
        host=config['host'],
        port=config['port'],
        filename=file.name
    )


@app.route("/<filename>", method=['GET'])
def download(filename):
    global file_to_serve
    resolved_filename = file_to_serve.name
    root_dir = file_to_serve.parent
    return bottle.static_file(resolved_filename, root=root_dir, download=resolved_filename)


def main():
    global config
    global file_to_serve

    args = parse_args()
    file_to_serve, debug = validate_args(args)
    if debug:
        config["host"] = '127.0.0.1'
    url = "{url}".format(
        url=generate_url(config, file_to_serve)
    )
    print("Serving {url}".format(url=url))
    app.run(host=config['host'], port=config['port'], debug=True)


if __name__ == "__main__":
    main()
