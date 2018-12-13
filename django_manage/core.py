import sys
import subprocess

import kangaroo

DJANGO_MANAGE_PY = "manage.py"


def find_manage_py_and_run_with_arguments(args):
    filepath = kangaroo.bring(filename=DJANGO_MANAGE_PY)
    if filepath is None:
        print("We can't find manage.py file")
        sys.exit(1)

    print(filepath)
    subprocess.call(["python", filepath, *args])
    sys.exit(0)

