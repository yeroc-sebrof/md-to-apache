import os
import argparse

md_folder = "Markdown"
html_folder = "/var/www/html/"
filelist = []
outfiles = []

def commandMenu(): #Lists arguments that can be used and returns if one selected
    options = argparse.ArgumentParser()

    options.add_argument("-dry-run", help = "Converts files and places them into an HTML folder" , action = "store_true")
    options.add_argument("-debug", help = "Prints the entire file list", action = "store_true")
    
    return(args = options.parse_args())

def commands(args): #Actually does the argument
    if args.dry-run:
        print("The following files would have been converted and placed into %s\n" % html_folder)
        print(filelist)
        exit(0)
      
    elif debug:
        print(filelist)

    else:
        pass
        
if "markdown_html_converter" not in os.listdir(): #Get file from GitHub if not already in directory
    import subprocess
    subprocess.run(["git","clone","https://github.com/yeroc-sebrof/markdown_html_converter"])
    
    if "markdown_html_converter" not in os.listdir(): #Error catching
        print("There appears to be a problem with fetching the files from GitHub, please try again")
        exit(1) 

if md_folder not in os.listdir(): #Checks if the correct folder exists
    print("The " + md_folder + " folder is not visable.\nPlease place one in the current working directory and populate it with markdown files")
    exit(1)

md_folder_contents = os.listdir("{}/{}/".format(os.getcwd(), md_folder))

if md_folder_contents == []: #Checks if folder contains files
    print("The " + md_folder + " folder is empty.\nPlease populate the folder with markdown files")
    exit(1)


for root, dirs, files in os.walk("{}/{}/".format(os.getcwd(), md_folder)): 
    for filename in files:
        if filename[-3:] == ".md": # Ignore this thing flag for runtime
            filelist.append(root.replace("{}/{}/".format(os.getcwd(), md_folder), '')+'/'+filename)


if len(filelist) == 0: # skip this check flag for runtime?
    print("Could not find valid files to convert")
    exit(0)

commands(commandMenu())
checkVar = input("Successfully loaded file list, continue with %i items being copied into %s?" % (len(filelist), html_folder))

if checkVar.upper()[0] is not 'Y':
    exit(0)

for filename in filelist: #Changes file name
    print("Filename to be ", end='')
    currentF = filename[:-3] + "/index.html"
    outfiles.append(currentF)

if commandMenu().debug:
    print(outfiles)

print("Got to end.")

