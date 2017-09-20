#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:20:36 2016

@author: Louie
"""

import os 
import shutil 

#1
def list_files_walk():
    '''
    A function that use the os module's walk generator,
    and returns a list of the paths of all the parts.txt files
    '''
    output = []
    for dirpath, dirnames, filenames in os.walk("CarItems"): 
        for ifile in filenames:
            if 'parts' in ifile: #If there is 'parts' in filenames
                output.append(os.path.join(dirpath, ifile)) #append the path of the file to output list
    return output

#2
def list_files_recursive(top_dir):
    '''
    A function that use without the os module's walk generator,
    but recursion, and returns a list of the paths of all the parts.txt
    files
    '''
    list_items = os.listdir(top_dir)
    list_txt = []
    for item in list_items:
        item_path = os.path.join(top_dir, item)
        if os.path.isdir(item_path): #If the item is a dir
            list_txt = list_txt + list_files_recursive(item_path) #Use that dir as an input of the top_dir of function list_files_recursive
        elif os.path.splitext(item)[0] == 'parts': #If the item is not a dir, check if it contain 'parts'
            list_txt = list_txt + [item_path]
    return list_txt

#3
print("list_files_walk & list_files_recursive are equal:",list_files_recursive("CarItems") == list_files_walk())

#4
if os.path.isdir('CarItemsCopy') == False: # Do the following only there is no CarItemsCopy
    shutil.copytree('CarItems','CarItemsCopy') 
    for dirpath, dirnames, filenames in os.walk("CarItemsCopy"):
        for ifile in filenames:
            filePath = os.path.join(dirpath,ifile) #File path in CarItemsCopy
            nfileName = ifile.split('.')[0]+'-'+filePath.split('/')[3]+'.txt' #New file name, split the file into name and .txt, and insert - year
            nfilePath = os.path.join(dirpath[:-5],nfileName) #New file path
            shutil.move(filePath,nfilePath) #Move old file to new dir, with a new name
        if not os.listdir(dirpath): #if the dir is empty
            os.rmdir(dirpath) #delete the dir
