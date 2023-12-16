import os
import shutil

from_dir = "C:/Users/owoad/Downloads"
to_dir = "C:/Users/owoad/OneDrive/Desktop/downloadedFiles"
list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name,extention=os.path.splitext(file_name)
    
    if (extention == ""):
        continue

    if (extention in ["Application"]):
        path_1 = from_dir + "/" + file_name
        path_2 = to_dir + "/" + "Application_files"
        path_3 = to_dir + "/" + "Application_files" + "/" + file_name

        if (os.path.exists(path_2)):
            shutil.move(path_1,path_3) 
            print("Moving " + file_name + "...")   
        else:
            print("Creating Folder...")    
            os.makedirs(path_2)
            shutil.move(path_1,path_3)
            print("Moving " + file_name + "...")