import copy
import os
import glob
import pandas as pd
import shutil


phone_dir = "/home/devselvan/Music/TamilSongs/All_Song_phone/"
drive_dir = "/home/devselvan/Music/TamilSongs/All_Song_drive/"

phone_to_drive = {"parent": [], "dir": [], "song": [], "source": [], "desti": []}
drive_to_phone = {"parent": [], "dir": [], "song": [], "source": [], "desti": []}


def musicComparison(dir1, dir2):
    list_dir1 = set(os.listdir(dir1))
    list_dir2 = set(os.listdir(dir2))

    diff1 = list_dir1.difference(list_dir2)
    diff2 = list_dir2.difference(list_dir1)

    songs_dir1 = set(os.listdir(dir1 + list(list_dir1)[0]))
    songs_dir2 = set(os.listdir(dir2 + list(list_dir2)[0]))

    for dir in list_dir1:
        songs_dir1 = set(os.listdir(dir1 + dir))
        songs_dir2 = set(os.listdir(dir2 + dir))

        print(dir, len(songs_dir1) - len(songs_dir2))

        song_diff = songs_dir1.difference(songs_dir2)

        for song in song_diff:
            phone_to_drive["parent"].append("phone -> drive")
            phone_to_drive["dir"].append(dir)
            phone_to_drive["song"].append(song)
            phone_to_drive["source"].append(os.path.join(dir1, dir))
            phone_to_drive["desti"].append(os.path.join(dir2, dir))

    for dir in list_dir2:
        songs_dir1 = set(os.listdir(dir1 + dir))
        songs_dir2 = set(os.listdir(dir2 + dir))

        print(dir, len(songs_dir1) - len(songs_dir2))

        song_diff = songs_dir2.difference(songs_dir1)

        for song in song_diff:
            drive_to_phone["parent"].append("drive -> phone")
            drive_to_phone["dir"].append(dir)
            drive_to_phone["song"].append(song)
            drive_to_phone["source"].append(os.path.join(dir2, dir))
            drive_to_phone["desti"].append(os.path.join(dir1, dir))
    # return song_dic

    df1 = pd.DataFrame(phone_to_drive)
    df2 = pd.DataFrame(drive_to_phone)
    # print(df1)
    # print(df2)

    # df1.to_excel("/home/devselvan/Music/phone_to_drive.xlsx")
    # df2.to_excel("/home/devselvan/Music/drive_to_phone.xlsx")


def copyfile(song_dict):
    song_list = song_dict["song"]
    source_path_list = song_dict["source"]
    desti_path_list = song_dict["desti"]

    for song, source, desti in zip(song_list, source_path_list, desti_path_list):
        print(source.split("/")[-1])
        source_file = os.path.join(source, song)
        if os.path.isfile(source_file):
            shutil.copy(source_file, desti)
            print(f"{song} copyed successful")


def checkDuplicate(dir):
    for song_dir in set(os.listdir(dir)):
        song_list = os.listdir(os.path.join(dir, song_dir))
        print(song_dir, len(song_list), len(set(song_list)))


checkDuplicate(phone_dir)
checkDuplicate(drive_dir)


# print(musicComparison(phone_dir, drive_dir))
# copyfile(phone_to_drive)
# copyfile(drive_to_phone)
