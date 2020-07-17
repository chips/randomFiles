# randomFiles

For demo purposes for my job as Product Manager at Tricent Security Group (www.tricent.com), I needed a bunch of files to populate the interface. So I just wrote this quick little utility for that.

It would benefit from taking the dictionaries from files, and taking command line arguments, but i was in a bit of a hurry to finish it, so this is what came out of the first 10 minutes of work.

Usage:

change numberOfFiles to the number of file you want. This might not be the actual number of files created, as there is no check to see if a random file name already exists. If it does, the file will just have more "data" in it.

linesInFile is used to manage the size of the files. It will be randomly filled with 1000 to linesInFile lines of "This is just to fill the file"

random_titles contains the first part of the filename. Go ahead and add more or change them as needed

random_content contains the tail of the filename generated. Again, change to your liking.

random_filetypes are the extensions the script will add to the randomly generate file.

directory is the name of the directory the files will be placed in.

To use, create the directory you have named, and execute the python script:

python generator.py

Boom! you have random files!
