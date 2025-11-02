import os
import shutil

dir_path = "/home/devselvan/Music/Illayaraja/320kbps/"
desti_path = "/home/devselvan/Music/Illayaraja/Illayaraja_Collections/"


def Nfolder_1folder(path, desti):
    total_count = 0
    for sub_dir in os.listdir(path):
        print(sub_dir)
        total_count = total_count + len(os.listdir(os.path.join(path, sub_dir)))
        total_song = len(os.listdir(os.path.join(path, sub_dir)))
        song_count = 0
        for file in os.listdir(os.path.join(path, sub_dir)):
            shutil.copy(os.path.join(path, sub_dir, file), desti)
            song_count += 1

        print(song_count - total_song)

    print(total_count)


Nfolder_1folder(dir_path, desti_path)
