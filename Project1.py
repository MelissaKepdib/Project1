#This file will contain codes to organize files in a directory.
#Step 1 is File detection: Creating a code that scans the specified directory and identify all files within it.
    #Let us import the required os library and modules
import os
import shutil    
from pathlib import Path
    #Let us now specify the directory
directory=r"C:\Users\ykfabiol\Python Fundamentals\Projects\filestoscan2"        #This is the directory in my computer,where all my files are initially. The 'r' is used to define a raw string so that Python does not consider the backslashes (\) as escape characters
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
list_of_files=scan_directory(directory)
print(list_of_files)

#Step 2 is file organization: Implementing logic to categorize files based on their file extensions

 #Let us create a dictionary that will contain the type of files as key and the corresponding extensions as values.
types_of_files={
    "pdf documents" : ".pdf",
    "Word documents" : ".docx",
    "excel documents" : ".xlsx",
    "text documents" : ".txt",
    "powerpoint documents" : ".pptx",
    "python documents" :".py",
    "photos" : [".jpeg", ".PNG"]
}
   
#Step 3 is folder creation: Creating separate folders for each category identified during the file organization process
    #Let us first define a function to create a folder at a specific path if it does not already exist
def create_directory(path):
    if not os.path.exists(path):      #A new directory(folder) will be created at the specified path only if it does not already exist
        os.makedirs(path)               #os.makedires() is a module used to create a directory(folder). A new directory will be created at the specified path

#We will now use the dictionary we created before, types_of_files, to create folders for each category
def organize_files(directory):
    list_of_files=scan_directory(directory)

#Let us define what the extension of a file is.
    for file in list_of_files:
        file_extension=file.suffix      #We know that an extension is the suffix of the file path.

        moved=False                     #This flag is used to track whether the file has been moved to a subdirectory. It is initially set to False
        for category, extensions in types_of_files.items():
            if file_extension in extensions:
                subdirectory=os.path.join(directory, category)       #os.path.join() is a function in python that joins two path components
                create_directory(subdirectory)                       #We want to create a subdirectory at the path defined above, if it does not exist already.

                subpath=os.path.join(subdirectory,file.name)          #This defines the full path where the file will be moved, which includes the subdirectory and the original file name. file.name refers to the name of the file, including its extension, as a string.
#Step 4 is file movement: moving files in to the appropriate folder (subdirectory) based on their category.
                shutil.move(file,subpath)                              #This moves the file to the subpath within the appropriate category subdirectory.
#Step 5  is logging: implementing logging functionality to record the actions taken by the tool. (e.g., which files were moved to which folders)
                print(f"Moved {file.name} to {subdirectory}") 
                moved = True
                break
               
#Step 6 is error handling:Implement robust error handling to gracefully handle unexpected scenarios such as invalid directory paths or permission issues.
        if not moved:
            subdirectory=os.path.join(directory, "other documents")
            create_directory(subdirectory)
            subpath=os.path.join(subdirectory,file.name)
            shutil.move(file,subpath)
            print(f"Moved {file.name} to {subdirectory}")
#Step 7 is command-line interface (CLI):Develop a command-line interface to interact with the tool. Users should be able to specify the directory to be organized and any other options (e.g., organization criteria, logging settings) via command-line arguments.
if __name__ == "__main__":                                           #This construct is useful for writing reusable Python scripts. It allows you to write code that can either: 1) Be executed when the script is run directly.2) Be imported into other scripts without executing certain code blocks.                         
    if not os.path.exists(directory):                               #Before calling organize_files(directory), the script checks if the directory exists with this line:
        print(f"Error: The directory {directory} does not exist.")     #The If block can be removed if we do not want to check whether the directory exists. In that way, we would move directly from if _name_... to organize files and print.
    else:
        organize_files(directory)
        print("File organization complete.")