import os
import random

numberOfFiles = 500
linesInFile = 29000

random_titles = ['TPS', 'budget', 'Request_for', "Design","internal", "confidential" "plan","client","internal","General","Research","General"]
random_content = ['report', 'overview', 'notes', 'quote','documents','list','highlights','for_approval','review']
random_filetypes = ['.xlsx', '.jpg', '.docx', '.txt', '.png', '.pdf']
for a in range(numberOfFiles):
    directory = "generatedFiles"
    filenameBase = random_titles[random.randint(0,len(random_titles)-1)] + "_" + random_content[random.randint(0, len(random_content)-1)]
    fileType = random_filetypes[random.randint(0,2)]
    filename = os.path.join(directory , (filenameBase + fileType))
    f = open(filename, "w+")
    print("generated file " + str(f))
    for i in range(random.randint(1000,linesInFile)):
        f.write("This is just to fill the file")
    f.close
