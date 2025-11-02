import pygame
import os
import shutil

all_song_path = "/home/devselvan/Music/Illayaraja/Illayaraja_Collections/"
fav_song_path = "/home/devselvan/Music/Illayaraja/Fav_songs/"
unfav_song_path = "/home/devselvan/Music/Illayaraja/Unfav_sonngs/"

total_songs = len(os.listdir(all_song_path))


song_count = 0

for song in sorted(os.listdir(all_song_path)):
    fav_list = os.listdir(fav_song_path)
    uvfav_list = os.listdir(unfav_song_path)
    music_file = os.path.join(all_song_path, song)
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()

    song_count += 1

    print(
        f"{song} : {total_songs - song_count} fav:{len(fav_list)} uvfav:{len(uvfav_list)}"
    )

    option = input("Enter the option y or n: ")

    if option == "y":
        shutil.move(music_file, fav_song_path)
    elif option == "n":
        shutil.move(music_file, unfav_song_path)
    else:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

        break

    # if keyboard.is_pressed("y"):
    #     shutil.move(music_file, fav_song_path)
    # if keyboard.is_pressed("n"):
    #     shutil.move(music_file, unfav_song_path)
