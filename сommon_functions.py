import os


def get_bytes_from_file(path):
    if os.path.isdir(path):
        return []
    else:
        with open(path, 'rb') as file:
            data = file.read()
        return data


def bypass(path):
    all_files = [path]
    current_directory = os.listdir(path)
    for file in current_directory:
        if os.path.isdir(path + '/' + file):
            bypass(path + '/' + file)
        else:
            all_files.append(path + '/' + file)
    return all_files
