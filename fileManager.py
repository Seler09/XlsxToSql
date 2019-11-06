def outputFileStream(streamType, fileName, clearFile, data):    
    fileObject = open(f"{fileName}", streamType)    
    fileWrite(fileObject, data)
    fileObject.close()


def fileWrite(fileObject, data):
    fileObject.writelines(data)


def fileRead(fileObject):
    return fileObject.readlines() 