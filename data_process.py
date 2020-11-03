#!/usr/bin/env python3
import os
import glob
import zipfile
import shutil

class DataProcessor(object):
    """docstring for DataProcessor"""
    def __init__(self, src_folder_path, dst_folder_path):
        self.src_folder = src_folder_path
        self.dst_folder = dst_folder_path
        if not os.path.isdir(self.dst_folder):
            os.makedirs(self.dst_folder) 
        
    def unzip(self):
        for file_path in glob.glob(self.src_folder + '*.zip'):
            file_name = file_path.split('/')
            student_info = file_name[-1].split('_')

            is_late = True if student_info[1] == 'LATE' else False
            
            student_name = student_info[0]
            student_uin = student_info[-1].split('.')[0]

            with zipfile.ZipFile(file_path, 'r') as zip_file:
                zip_file.extractall(self.dst_folder + student_name + '_' + student_uin)

    def add_files(self, file_list):
        for dir_name in glob.glob(self.dst_folder + '*'):
            # insert files into the folders
            dir_name += '/'
            sub_dirs = glob.glob(dir_name+'*')
            for sub_dir in sub_dirs:
                if sub_dir.split('/')[-1] == '__MACOSX':
                    shutil.rmtree(sub_dir)
                if sub_dir.split('/')[-1].isdigit() or sub_dir.split('/')[-1].startswith('<'):
                    student_files = glob.glob(sub_dir+'/*')
                    for file in student_files:
                        shutil.copy2(file, dir_name)
                    shutil.rmtree(sub_dir)

            for file in file_list:
                if file.split('/')[-1] == '__pycache__':
                    continue
                if os.path.isdir(file):
                    try:
                        shutil.copytree(file, dir_name + file.split('/')[-1])
                    except:
                        pass
                else:
                    shutil.copy2(file, dir_name)
