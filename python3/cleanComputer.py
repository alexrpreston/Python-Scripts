import os
import glob
from send2trash import send2trash

sourceFolders = ["Desktop", "Downloads", "Documents"] #All Folders we want to delete from

fileTypes = [".png", ".jpg", ".jpeg", ".pdf", ".txt"] #All files types we want to delete 

userName = "alexpreston" #Name of Home folder 

for folder in sourceFolders:
    for fileType in fileTypes:
        fileList = glob.glob("/Users/{}/{}/*{}".format(userName, folder, fileType)) #Absolute Paths for Mac Users

        for i in range(len(fileList)):
            send2trash(fileList[i]) #Puts files in Trash or Recyle Bin
	
    print("{} Cleaned.".format(folder))




	            
