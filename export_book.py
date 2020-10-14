import os, sys, re
import argparse
import subprocess

# return output from bash pipe cmd as decoded string
def run_cmd(cmd):
	bash_cmd = cmd
	process = subprocess.Popen(bash_cmd.split(), stdout=subprocess.PIPE)
	output = process.stdout.read()
	return output.decode('utf-8')

# def get_list_of_files(path, extension):
#     list_of_files = []
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             if file.endswith("." + extension):
#                 list_of_files.append(os.path.join(root, file))
#     return list_of_files

def sort_list(a_list):
    list_with_indeces = []
    for item in a_list:
        index = re.sub("[^0-9]", "", item)
        list_with_indeces.append([item, index])
    list_with_indeces.sort(key=lambda x: x[1]) # sort by index
    
    sorted_list = []
    for item in list_with_indeces:
        sorted_list.append(item[0])
    return sorted_list


# get chapters first if they exist as directories
# then Scenes, or just Chapters if they are md files.
def get_list_of_files(path, extension, chapter_folders=False):
    sorted_markdown_list = []
    if chapter_folders:
        chapters_list = [ item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item)) ]
        chapters_list = sort_list(chapters_list)
        
        for chapter in chapters_list:
            chapter_markdown_files = []
            all_files = os.listdir(path + "/" + chapter)
            for a_file in all_files:
                if a_file.endswith("." + extension):
                    # path + "/" + chapter + "/" + 
                    chapter_markdown_files.append(a_file)
            chapter_markdown_files = sort_list(chapter_markdown_files)
            for index in range(len(chapter_markdown_files)):
                current_path = chapter_markdown_files[index]
                chapter_markdown_files[index] = path + "/" + chapter + "/" + current_path
            sorted_markdown_list.extend(chapter_markdown_files)
    else:
        # process only MD files make sure they are numbered
        all_files = os.listdir(path)
        for a_file in all_files:
            if a_file.endswith("." + extension):
                sorted_markdown_list.append(a_file)
        sorted_markdown_list = sort_list(sorted_markdown_list)
        for index in range(len(sorted_markdown_list)):
            current_path = sorted_markdown_list[index]
            sorted_markdown_list[index] = path + "/" + current_path

    return sorted_markdown_list

def export_dir_to_format(path):
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--root-path', help='Root path for book files', required=True)
    parser.add_argument('-c', '--using-chapter-folders', 
    help='Are you using folders for chapters?', default=False,action='store_true')
    parser.add_argument('-f', '--file-extension', default='md')
    args = parser.parse_args()

    file_list = get_list_of_files(args.root_path, args.file_extension, args.using_chapter_folders)

    if not file_list:
        print("No markdown files found, if you\'re using folder chapters use -c, else do not use -c")
        print("Exiting...")
        exit()
    
    for file in file_list:
        print(file)

    if args.root_path[-1] != '/' or args.root_path[-1] != '\\':
        args.root_path = args.root_path + '/'

    default_pandoc_cmd = 'pandoc --pdf-engine=xelatex --toc -o' + args.root_path +'book.pdf title.txt '
    files_string = " ".join(file_list)
    run_cmd(default_pandoc_cmd + files_string)

if __name__ == "__main__":
    main()

# book 1 Chapters and Scenes
# file_list = get_list_of_files('./book', 'md', True)

# for file in file_list:
#     print(file)

# default_pandoc_cmd = 'pandoc --pdf-engine=xelatex --toc -o book.pdf title.txt '
# files_string = " ".join(file_list)

# run_cmd(default_pandoc_cmd + files_string)

# # book 2 Only md files, can be named anything just have a number in it for sorting
# file_list = get_list_of_files('./book_2', 'md')

# for file in file_list:
#     print(file)

# default_pandoc_cmd = 'pandoc --pdf-engine=xelatex --toc -o book2.pdf title.txt '
# files_string = " ".join(file_list)

# run_cmd(default_pandoc_cmd + files_string)