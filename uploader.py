# ftp utility
# credential solution
# filepath of www
# move current files to backup directory eg (f"backup/{datetime.now()}")
# copy files to directory
# backup selection options and restoration (creates backup of current files first for an undo)

# logging 

import argparse

parser = argparse.ArgumentParser(description="test boi")

parser.add_argument("echo", help="help string here")

arguments = parser.parse_args()

print(arguments.echo)