import os
from pathlib import Path

sub_dir = {
    'destination1': ['file.txt', 'file1.txt'],
    'destination2': ['file2.txt']
}


def pick_directory(value):
    for destination, files in sub_dir.items():
        for f in files:
            if value == f:
                return destination
    return "Others"


if __name__ == '__main__':

    # 1. Move 1 file from a folder to another folder
    # # Specify the current location + filename
    # FROM = 'D:\Tools\Rename-Sort-Files\moveFiles\source\\file.txt'
    #
    # # Specify the desire destination + filename
    # TO = 'D:\Tools\Rename-Sort-Files\moveFiles\destination\\file.txt'
    #
    # os.rename(FROM, TO)

    # --------------------------------------------------#

    # 2. Move multiple files from a folder to another folder
    # # Specify the current location + filename
    # FROM = 'D:\Tools\Rename-Sort-Files\moveFiles\source\\'
    #
    # # Specify the desire destination + filename
    # TO = 'D:\Tools\Rename-Sort-Files\moveFiles\destination\\'
    #
    # for f in os.listdir(TO):
    #     f_from = FROM + f
    #     f_to = TO + f
    #     os.rename(f_to, f_from)

    # --------------------------------------------------#

    # 3. Move multiple files to multiple folers
    os.chdir('D:\Tools\Rename-Sort-Files\moveFiles\source\\')

    for f in os.scandir():
        if f.is_dir():
            continue
        # Specify the current location of all the files
        f_from = Path(f)

        # Specify the desire destination of all the files
        directory = pick_directory(str(f_from))
        dirPath = Path(directory)
        f_to = dirPath.joinpath(f_from)

        f_from.rename(f_to)
