#Program to take all files from desktop and put into a folder

import os
import shutil
import sys


def find_desktop_path():
    '''(NoneType) -> str
    Find correct Desktop path
    '''

    #where all files are at
    desktop_path = os.path.expanduser('~/Desktop')

    #check to see if Desktop path is correct
    while not os.path.exists(desktop_path):
        desktop_path = input('Give me the path to your \
    Desktop\n> ')

    return desktop_path


def find_destination_path(desktop_path):
    '''(str) -> list of str
    Find destination path
    '''

    #Find Folder where they want to move all their files
    folder = input('Give me the folder name on your Desktop\
     where  I am moving everything\n > ')

    destination_path = desktop_path + '/' + folder

    #if Folder does not exist, create it
    if not os.path.exists(destination_path):
        answer = input('That folder doesn\'t exist! Can I create\
     it? \nY or N?\n> ')
        if answer.lower() == 'y':
            os.makedirs(destination_path)

        else:
            find_destination_path()

    return [destination_path, folder]


def move_files(destination_path, folder, desktop_path,):
    '''(str, str, str) -> NoneType
    Moves everything from Desktop to destination path
    '''

    os.chdir(desktop_path)
    #list_of_files
    all_items_on_desktop = os.listdir()
    everything_to_move = []

    #diving up all items on Desktop as either files or folders
    for item in all_items_on_desktop:
        everything_to_move.append('/' + item)

    #removing hidden file in list
    everything_to_move.remove(everything_to_move[0])

    #remove destination folder from list
    if folder in everything_to_move:
        everything_to_move.remove(folder)

    #moving everything  into destination folder
    for thing in everything_to_move:
        shutil.move(desktop_path + thing, destination_path)

#running the program
print ("I am going to clean your Desktop")
paths_output = find_destination_path(find_desktop_path())
move_files(paths_output[0], paths_output[1], find_desktop_path())
print ("Done")
