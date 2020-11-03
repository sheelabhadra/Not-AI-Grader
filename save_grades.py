#!/usr/bin/env python3
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-dst', '--dst-dir', help='Path to destination directory',
                    default='', type=str)
args = parser.parse_args()

student_grades = {}
with open('grades.txt', mode='r') as txt_file:
    for line in txt_file:
        # Ignore this
        if '/'+args.dst in line:
            continue
        # Student submission raised an error
        if args.dst in line:
            student_info = line.split('/')[-1]
            student_grades[student_info] = -999
        # Student submission ran successfully
        if 'Total:' in line:
            points = int(line.split('/')[0].split(' ')[-1])
            student_grades[student_info] = points

with open('grades.csv', mode='w') as csv_file:
    fieldnames = ['Name', 'UIN', 'Grades']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for student, grades in student_grades.items():
        writer.writerow({'Name': student.split('_')[0], 'UIN': student.split('_')[1].split('-')[0], 'Grades': grades})