#!/usr/bin/env python3
import csv

student_grades = {}
with open('grades-P1.txt', mode='r') as txt_file:
    for line in txt_file:
        flag = False
        if '/proj1/' in line:
            continue
        if 'proj1/' in line:
            student_info = line.split('/')[-1]
            student_grades[student_info] = -999
        if 'Total:' in line:
            points = int(line.split('/')[0].split(' ')[-1])
            student_grades[student_info] = points

with open('grades-P1.csv', mode='w') as csv_file:
    fieldnames = ['Name', 'UIN', 'Grades']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for student, grades in student_grades.items():
        writer.writerow({'Name': student.split('_')[0], 'UIN': student.split('_')[1].split('-')[0], 'Grades': grades})