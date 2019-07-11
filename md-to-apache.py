import os

dryrun = True

md_folder = "Markdown"
html_folder = "/var/www/html/"

if md_folder not in os.listdir():
    print("The " + md_folder + " folder is not visable.\nPlease place one in the current working directory and populate it with markdown files")
    exit(1)

md_folder_contents = os.listdir("{}/{}/".format(os.getcwd(), md_folder))

if md_folder_contents == []:
    print("The " + md_folder + " folder is empty.\nPlease populate the folder with markdown files")
    exit(1)

filelist = []

for root, dirs, files in os.walk("{}/{}/".format(os.getcwd(), md_folder)):
    for filename in files:
        if filename[-3:] == ".md": # Ignore this thing flag for runtime
            filelist.append(root.replace("{}/{}/".format(os.getcwd(), md_folder), '')+'/'+filename)


if dryrun:
    print("The following files would have been converted and placed into %s\n" % html_folder)
    print(filelist)
    exit

if len(filelist) == 0: # skip this check flag for runtime?
    print("Could not find valid files to convert")
    exit


check = input("Successfully loaded file list, continue with %i items being copied into %s?" % (len(filelist), html_folder)

if str(check)[0].upper() != 'Y':
    exit

print("Got to end.") # I will continue when I get home
