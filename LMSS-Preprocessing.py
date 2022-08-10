#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 16:26:14 2022

@author: isamarcortes
"""

import rasterio as rio
import subprocess
import glob
import tarfile as tr


###location of tar files
FileLocation = '/Users/isamarcortes/Downloads/LMSS_Data'###change this to folder where you have tar files stored
FileSorting = sorted(glob.glob(FileLocation+'/*.tar'))


FolderNamesAppend = []####appending all folder names to a list to use for image processing later
for i in FileSorting:
    '''
    This first forloop creates the folders where we will be unzipping the data to
    by creating a folder with the same name as the file. It then extracts all the contents
    of the tar file and places said contents into the new directory that was just created
    '''
    FolderName = i.split('.')[0]
    FolderNamesAppend.append(FolderName)
    subprocess.call('mkdir -p '+FolderName,shell=True)
    FileOpen = tr.open(i)
    FileOpen.extractall(FolderName)
    FileOpen.close()




#######this part of code stacks tif and add the metadata  
for k in FolderNamesAppend:
    Images = sorted(glob.glob(k+'/*.TIF'))
    for m in Images:
        with rio.open(m) as src:
            metadata = src.meta
        metadata.update(count = len(Images))
        with rio.open(k+'/stack.tif', 'w', **metadata) as dst:
            for id, layer in enumerate(Images, start=1):
                with rio.open(layer) as src1:
                    dst.write_band(id, src1.read(1)) 





    
    
    
    
    
    
    
    
    
    
    
