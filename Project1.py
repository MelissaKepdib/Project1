#This file will contain codes to organize files in a directory.
#The first step is File detection: Creating a code that scans the specified directory and identify all files within it.
    #Let us first create a dictionary that will contain the type of files as key and the corresponding extensions as values.
types_of_files={
    "pdf documents" : ".pdf",
    "Word documents" : ".docx",
    "excel documents" : ".xlsx",
    "text documents" : ".txt",
    "powerpoint documents" : ".pptx",
    "photos" : [".jpeg,", ".PNG"]
}


    #Let us now import the required os library and modules
import os
import shutil    
from pathlib import Path
    #Let us specify the directory
directory=r"C:\Users\ykfabiol\Python Fundamentals\Projects\filestoscan2"
    #Let us create the code that will scan this directory and identify all files. The files will be put in a list called "Files".
def scan_directory(directory):
    files=[]                  #We start with an empty list
    for file in Path(directory).iterdir():        #Path(directory) creates a Path object from the given directory string.
        if file.is_file():                        #.iterdir() is a method of the Path object that returns an iterator over the contents (files and subdirectories) of the directory. It will yield Path objects for each item inside the directory.
            files.append(file)
        else:
            print("no file is present")
    #return [file for file in Path(directory).iterdir() if file.is_file()]
    return files
print(scan_directory(directory))