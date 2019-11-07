def outputFileStream(streamType, fileName, data):    
    fileObject = open(f"{fileName}", streamType)    
    fileWrite(fileObject, data)
    fileObject.close()


def fileWrite(fileObject, data):
    fileObject.writelines(data)