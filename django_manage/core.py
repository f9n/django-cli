import sys
import subprocess

import kangaroo

DJANGO_MANAGE_PY = "manage.py"


def find_manage_py():
    filepath = kangaroo.bring(filename=DJANGO_MANAGE_PY)
    if filepath is None:
        print("We can't find manage.py file")
        sys.exit(1)

    return filepath


def run_manage_py_with_arguments(filepath, args):
    subprocess.call(["python", filepath, *args])
    sys.exit(0)

