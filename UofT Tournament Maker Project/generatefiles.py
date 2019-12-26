import shutil
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


def copyXTimes(src, dst, x: int):
    for i in range(1, x + 1):
        shutil.copy(src, '{}{}.docx'.format(dst, str(i)))





#copyXTimes('Shimpan Letters/4Dan Shimpan No Parking Letter.docx', 'Shimpan Letters/', 3)
#createFolder('./name/')