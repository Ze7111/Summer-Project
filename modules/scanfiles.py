import os
total = 0

def scancomp():
    file_object = open('databases\\scannedComp.dat', 'w')
    for file in os.listdir("images\\--- Computing ---"):
        if not file.endswith(".json" or "."):
            file_object.write(file+'\n')
    file_object.close()
    scanGD()

def scanGD():
    file_object = open('databases\\scannedGD.dat', 'w')
    for file in os.listdir("images\\--- GameDesign ---"):
        if not file.endswith(".json" or "."):
            file_object.write(file+'\n')
    file_object.close()
    scanMath()

def scanMath():
    file_object = open('databases\\scannedMath.dat', 'w')
    for file in os.listdir("images\\--- Maths ---"):
        if not file.endswith(".json" or "."):
            file_object.write(file+'\n')
    file_object.close()
    scanPhysics()

def scanPhysics():
    file_object = open('databases\\scannedPhysics.dat', 'w')
    for file in os.listdir("images\\--- Physics ---"):
        if not file.endswith(".json" or "."):
            file_object.write(file+'\n')
    file_object.close()
    mergeCompGD()

def mergeCompGD():
    data = data2 = ""
  
    # Reading data from file1
    with open('databases\\scannedComp.dat') as fp:
        data = fp.read()
    
    # Reading data from file2
    with open('databases\\scannedGD.dat') as fp:
        data2 = fp.read()
    
    # Merging 2 files
    # To add the data of file2
    # from next line
    data += "\n"
    data += data2
    
    with open ('cache\\TempCompGD.dat', 'w') as fp:
        fp.write(data)
    mergeMathPhysics()

def mergeMathPhysics():
    data = data2 = ""
  
    # Reading data from file1
    with open('databases\\scannedMath.dat') as fp:
        data = fp.read()
    
    # Reading data from file2
    with open('databases\\scannedPhysics.dat') as fp:
        data2 = fp.read()
    
    # Merging 2 files
    # To add the data of file2
    # from next line
    data += "\n"
    data += data2
    
    with open ('cache\\TempMathPhysics.dat', 'w') as fp:
        fp.write(data)
    mergeall()
    
def mergeall():
    data = data2 = ""
  
    # Reading data from file1
    with open('cache\\TempCompGD.dat') as fp:
        data = fp.read()
    
    # Reading data from file2
    with open('cache\\TempMathPhysics.dat') as fp:
        data2 = fp.read()
    
    # Merging 2 files
    # To add the data of file2
    # from next line
    data += "\n"
    data += data2
    
    with open ('databases\\allScanedFiles.dat', 'w') as fp:
        fp.write(data)
    
    fp.close()