"""
RS 2 Mask 
Description: 
filename: main.py 
author : Mohamadreza Farahzadi
contact : farahzadiphy@gmail.com
licenced for wira a.i. 
"""
from configparser import ConfigParser
from pydicom import dcmread
import os
class ScanDir:
    def init(self):
        #he
        a = 1
        
    def rsScan(rsPath,dir):
        files = os.listdir(dir)
        # sep = os.sep
        for i in files:
            # dcm = dcmread(os.path.join(dir,i))
            # print(dcmread(os.path.join(dir,i)).Modality.lower)
            if dcmread(os.path.join(dir,i)).Modality == 'RTSTRUCT':
                rsPath.append(os.path.join(dir,i))
        return rsPath
 
def get_lists():
    cnf = ConfigParser()
    cnf.read('config.ini')
    dir1 = cnf['def']['directory']
    dir2 = cnf['def']['directory2']
    saveDir = cnf['def']['saveDir']
    return dir1 ,dir2 , saveDir
def rsOptions(rsPath):
    for idx, i in enumerate(rsPath):
        rs = dcmread(i).StructureSetROISequence
        print("-------------------------")
        print('RS index:',idx+1,'\t filename:',i)
        for j in range(len(rs)):
            print('\t',j,') ',rs[j].ROIName)
    
    return dcmread(rsPath[int(input('Select RS index: ')) - 1])
if __name__ == '__main__':
    dir1 ,dir2 , saveDir= get_lists()
    # ScanDir()
    rsPath = []
    rsPath = ScanDir.rsScan(rsPath,dir1)
    rsPath = ScanDir.rsScan(rsPath,dir2)
    rs = rsOptions(rsPath)
