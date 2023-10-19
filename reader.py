import sys
import os
from functions import (
     read_csv_file,
     display_table,
     save_csv_file,
     validate_field_section,
)
# import from functions.py


def main():
    if len(sys.argv) < 2:
        print("Please provide with another file path")
        sys.exit()


src = sys.argv[1]  # file_path
dst = sys.argv[2]  # save_file_path
changes = sys.argv[3:]  # changes

if not dst.endswith('.csv'):
    print(f"File path not valid")
    sys.exit()

print("File path:", src)

if not os.path.exists(src) and not os.path.isfile(src):
    print(f"The path does not lead to a file: {src}")
    print(f"Available files:")
    for fn in os.listdir():
        if fn.endswith(".py") or os.path.isdir(fn):
            continue
        print(f" - {fn}")
        # fn = filename
else:
    # reads
    table = read_csv_file(src)
    # display
    display_table(table, sep="*")
    print_template = " | {:<10.10s} | {:<10.10s} | {:<15.15s} |"

    # load changes
    if not changes:
        print("No changes to be made were provided, try again.")
        sys.exit()

    print()

    for chg in changes:
        print(chg)
        rdx, cdx, val = chg.split(';')
        rdx = int(rdx)
        cdx = int(cdx)
        validate_field_section(rdx, cdx, table)
        value_to_be_changed = table[rdx][cdx]
        print(f"Changing {value_to_be_changed} into {val}")
        # does the change
        table[rdx][cdx] = val
        # counts like this 0, 1, 2, 3 not from 1 (banners counts as 0 if you have one)

    display_table(table, sep="*")

    save_csv_file(table, dst)
    # saves to new file


if __name__ == '__main__':
    main()
