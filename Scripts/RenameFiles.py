import re as regex
from os import sep, path, walk, rename
from pdb import set_trace as dbg

DATA_FOLDER = "Data"


def get_folder_path(folder_name):
    "Get the absolute path of a folder from the root of the project"
    return path.dirname(path.dirname(path.abspath(__file__))) + sep + folder_name


def get_files_from_folder(folder_path):
    matches = []
    for root, dirs, files in walk(folder_path):

        # Append files
        for file_name in files:
            matches.append(path.join(root, file_name))

        # Append files in sub directories 
        for dir_name in dirs:
            subdir_path = path.join(root, dir_name)
            subdir_matches = get_files_from_folder(subdir_path)
            matches.extend(subdir_matches)

    return matches


def create_files_rename_assoc(data_files):
    name_assoc = {}

    for file_path in data_files:
        root, renamed_file = path.split(file_path)
        renamed_file, file_extension = path.splitext(renamed_file)

        # Transform file name to be uniform
        renamed_file = regex.sub(" +", " ", renamed_file)
        renamed_file = regex.sub("_+", " ", renamed_file)
        renamed_file = renamed_file.title()
        renamed_file = renamed_file.replace(" ", "_")
        
        renamed_path = path.join(root, renamed_file) + file_extension
        if file_path != renamed_path:
            name_assoc[file_path] = renamed_path

    return name_assoc


def rename_files(file_paths_assoc):
    print "Renaming {0} files ...".format(len(file_paths_assoc))
    for (source_path, destination_path) in file_paths_assoc.iteritems():
        rename(source_path, destination_path)


def main():
    data_path = get_folder_path(DATA_FOLDER)
    data_files = get_files_from_folder(data_path)
    rename_assoc = create_files_rename_assoc(data_files)
    rename_files(rename_assoc)


if __name__ == "__main__":
    main()
