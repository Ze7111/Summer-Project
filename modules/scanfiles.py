import os
total = 0
# ---------------------- S C A N   F I L E S   I N   C O M P ---------------------------------- 
def scancomp():
    file_object = open('databases\\scannedComp.dat', 'w')
    for file in os.listdir("images\\--- Computing ---"):
        if not file.endswith(".json" or "."):
            file_object.write(file+'\n')
    file_object.close()
    scanGD()
# ---------------------- S C A N   F I L E S   I N   G D ---------------------------------- 
def scanGD():
    file_object = open('databases\\scannedGD.dat', 'w')
    for file in os.listdir("images\\--- GameDesign ---"):
        if not file.endswith(".json" or "."):
            file_object.write(file+'\n')
    file_object.close()
    scanMath()
# ---------------------- S C A N   F I L E S   I N   M A T H ---------------------------------- 
def scanMath():
    file_object = open('databases\\scannedMath.dat', 'w')
    for file in os.listdir("images\\--- Maths ---"):
        if not file.endswith(".json" or "."):
            file_object.write(file+'\n')
    file_object.close()
    scanPhysics()
# ---------------------- S C A N   F I L E S   I N   P H Y S I C S ---------------------------------- 
def scanPhysics():
    file_object = open('databases\\scannedPhysics.dat', 'w')
    for file in os.listdir("images\\--- Physics ---"):
        if not file.endswith(".json" or "."):
            file_object.write(file+'\n')
    file_object.close()
    mergeCompGD()
# ---------------------- M E R G E    F I L E    L I S T   F R O M   C O M P   A N D    G D ---------------------------------- 
def mergeCompGD():
    data = data2 = ""
  
    # Reading data from file
    with open('databases\\scannedComp.dat') as fp:
        data = fp.read()
    
    # Reading data from other file
    with open('databases\\scannedGD.dat') as fp:
        data2 = fp.read()
    
    # Merging 2 files
    data += "\n"
    data += data2
    
    with open ('cache\\TempCompGD.dat', 'w') as fp:
        fp.write(data)
    mergeMathPhysics()
# ---------------------- M E R G E    F I L E    L I S T   F R O M   P H Y S I C S   A N D    M A T H ---------------------------------- 
def mergeMathPhysics():
    data = data2 = ""
  
    # Reading data from file
    with open('databases\\scannedMath.dat') as fp:
        data = fp.read()
    
    # Reading data from other file
    with open('databases\\scannedPhysics.dat') as fp:
        data2 = fp.read()
    
    # Merging 2 files
    data += "\n"
    data += data2
    
    with open ('cache\\TempMathPhysics.dat', 'w') as fp:
        fp.write(data)
    mergeall()
# ---------------------- M E R G E    F I L E    L I S T   F R O M   M E R G E D ----------------------------------     
def mergeall():
    data = data2 = ""
  
    # Reading data from file
    with open('cache\\TempCompGD.dat') as fp:
        data = fp.read()
    
    # Reading data from other file
    with open('cache\\TempMathPhysics.dat') as fp:
        data2 = fp.read()
    
    # Merging 2 files
    data += "\n"
    data += data2
    
    with open ('databases\\allScanedFiles.dat', 'w') as fp:
        fp.write(data)
    # ---------------------- C L O S E    F I L E ---------------------------------- 
    fp.close()