import os

i=1

# walk through files in the current directory
for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith('.jpg'):

            src = filename
            dst = "DESIRED_NAME" + str(i) + ".jpg"

            # rename() function will rename all the files 
            os.rename(src, dst)
            i += 1