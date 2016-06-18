#!/usr/bin/env python

import subprocess
def call(args):
    """Call subprocess, split arguments

    subprocess.popen has strange behavior when supplying a string
    Just call using a list

    Args:
        args(str|list): arguments to run

    Returns:
        None. This is a procedure.
    """
    if isinstance(args, str):
        args = args.split(" ")
    subprocess.check_call(args)
