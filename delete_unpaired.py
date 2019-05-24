import numpy as np
import os

#This works like an INNER JOIN
#Everything that gets taken out is moved to path_removed

path_1 = "png_LR/"
path_2 = "png_HR/"

path_removed = "png_unpaired/"


def rename(path):
    
    old_dir = os.getcwd()
    os.chdir(path)
    res = []
    for file in os.listdir():
        if not(file.endswith(".png")):
            continue
        subject_no = file.split('_')[3][1:]       #print(file.split('_')[3][1:]) gives subject number
        name = "R2063_60mu_70ms_s"+str(subject_no)+"_a00_d000_Transmittance.png"
        os.rename(file, name)
    os.chdir(old_dir)


def get_all_paths(path):
    old_dir = os.getcwd()
    os.chdir(path)
    res = []
    
    res = sorted(os.listdir())

    os.chdir(old_dir)
    return res

def remove_unpaired(list_1, list_2):
    #if I can keep matching indexes that makes everything a lot faster
    
    for i,e in enumerate(list_1):
        print(e,"    ", list_2[i])
        if not(e == list_2[i]):
            if((i < len(list_2)-1) and (e == list_2[i+1])):
                os.rename(path_2+list_2[i], path_removed+list_2[i])
                print(list_2[i]," removed from path_2")
                list_2.remove(list_2[i])
            else:
                os.rename(path_1+e, path_removed+e)
                print(e," removed from path_1")
                list_1.remove(e)
                i = i-1


list_1 = get_all_paths(path_1)
list_2 = get_all_paths(path_2)

#print(list_2)

#rename(path_2)

remove_unpaired(list_1, list_2)




