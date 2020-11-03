#!/usr/bin/env python3
import yaml
import glob
import argparse
from data_process import DataProcessor

parser = argparse.ArgumentParser()
parser.add_argument('-src', '--src-dir', help='Path to source directory',
					default='', type=str)
parser.add_argument('-dst', '--dst-dir', help='Path to destination directory',
					default='', type=str)
parser.add_argument('-p', '--project-number', help='Project/contest number (e.g. P1 or C1)',
					default='', type=str)
parser.add_argument('-csv', '--csv-file', help='Path to CSV file',
					default='', type=str)
args = parser.parse_args()

dp = DataProcessor(args.src_dir, args.dst_dir)
dp.unzip()

with open('config.yml', 'r') as file:
    try:
        project_info = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        print(exc)

path = project_info[args.project_number]['path']

all_files = glob.glob(path + '*')
files_to_add = ['__init__.py']
for file in all_files:
	if file.split('/')[-1] not in project_info[args.project_number]['student_files']:
		files_to_add.append(file)

dp.add_files(files_to_add)

