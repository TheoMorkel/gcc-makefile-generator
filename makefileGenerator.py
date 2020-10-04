import os

def setFolderDir(path):
    os.chdir(path)

def getFiles():
    OriginalFiles = os.listdir()
    NewFiles = list(())

    for f in OriginalFiles:
        
        if f.endswith(".cpp"):
            FileName = f.replace(".cpp", "")
            NewFiles.append(FileName)

    return NewFiles

def makeMakefile(main):
    print ("Making makefile...")

    makefile = open("makefile", "w")
    
    fileNames = getFiles()

    fileString = "FILES = "
    for f in fileNames:
        temp = f + ".o "
        fileString = fileString + temp

    makefile.write(fileString + "\n\n")
    

    mainString = "{0}: $(FILES)\n\tg++ -o {0} $(FILES)"
    mainString = mainString.format(main)
    
    makefile.write(mainString + "\n\n")
    

    for f in fileNames:
        dotOString = "{0}.o:\n\tg++ -c -g {0}.cpp"
        dotOString = dotOString.format(f)

        makefile.write(dotOString + "\n\n")


    runString = "run: {0}\n\t./{0}"
    runString = runString.format(main)

    makefile.write(runString + "\n\n")


    cleanString = "clean:\n\trm {0} *.o\n\tclear"
    cleanString = cleanString.format(main)

    makefile.write(cleanString + "\n\n")
