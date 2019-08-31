import os, sys
import argparse
import subprocess

# return output from bash pipe cmd as decoded string
def run_cmd(cmd):
	bash_cmd = cmd
	process = subprocess.Popen(bash_cmd.split(), stdout=subprocess.PIPE)
	output = process.stdout.read()
	return output.decode('utf-8')

def get_list_of_files(path, extension):
    list_of_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith("." + extension):
                list_of_files.append(os.path.join(root, file))
    return list_of_files

def export_dir_to_format(path):
    pass


file_list = get_list_of_files('.', 'md')

for file in file_list:
    print(file)

default_pandoc_cmd = 'pandoc --toc -o book.pdf title.txt '
files_string = " ".join(file_list)

run_cmd(default_pandoc_cmd + files_string)