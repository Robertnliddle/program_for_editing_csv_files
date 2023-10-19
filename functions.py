import csv
import sys


def read_csv_file(src):
    table = []
    with open(src, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            table.append(row)
        return table


def display_table(table, sep="-"):
    print_template = " | {:<10.10s} | {:<10.10s} | {:<15.15s} |"
    print(print_template.format(table[0][0], table[0][1], table[0][2]))
    print(41 * sep)
    for row in table[1:]:
        print(print_template.format(row[0], row[2], row[3]))
    print(41 * sep)


def validate_field_section(rdx, cdx, table):
    if len(table) - 1 < rdx:
        print("Not enough rows")
        sys.exit()
    if len(table[rdx]) - 1 < cdx:
        print("Not enough columns")
        sys.exit()


def save_csv_file(table, dst):
    with open(dst, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(table)

# src = sys.argv[1]  # file_path
# dst = sys.argv[2]  # save_file_path
# changes = sys.argv[3]
