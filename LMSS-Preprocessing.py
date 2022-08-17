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
import numpy as np
import pandas as pd
#from LMSS_Tools import MetaData
from osgeo import gdal, gdalconst

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




########this chunk of code adds the metadata to the bands
for MD in FolderNamesAppend:
    IMGName = MD.split('/')[5]
    MetadataTxtFile = sorted(glob.glob(MD+'/'+IMGName+'_MTL.txt'))###sorts metadata files

'''#this chunk of code creates dictionarys for metadata for each band
    for l in MetadataTxtFile: #####this forloop reads the metadata    
        OpenMetaTxt = pd.read_fwf(l,delimiter='\t',dtype=str)###reads the txt file
        b4,b5,b6,b7,bQ1,bQ2 = MetaData(OpenMetaTxt)#uses function I built to create dictionaries
'''

#MetadataTxtFiles = []
#######this part of code stacks tif  
for k in FolderNamesAppend:
    ImageName = k.split('/')[5]
    #print(ImageName)
    Images = sorted(glob.glob(k+'/*.TIF'))#this isolates only files with extension .tif in each folder   
 
        #print(OpenMetaTxt)
    for m in Images: #iterate through the images in each folder
        with rio.open(m,'r+') as src:
            meta = src.profile##grab the metadata from tifs
'''###this will add metadata maybe.... work in progress
            meta['Band 4']=b4
            meta['Band 5']=b5
            meta['Band 6']=b6
            meta['Band 7']=b7
            meta['Band Q1']=bQ1
            meta['Band Q2']=bQ2
'''
            #print(meta)
            meta.update(count = len(Images))#update part of metadata to include stacked images
            #print(src.tags())
            #meta.update(OpenMetaTxt)
        
        with rio.open(k+'/'+ImageName+'_stack.tif', 'w', **meta) as dst:#change this to be in a root folder

        ###This forloop writes the new band. Repurposed code from here:
            #https://gis.stackexchange.com/questions/223910/using-rasterio-or-gdal-to-stack-multiple-bands-without-using-subprocess-commands
            for id, layer in enumerate(Images, start=1):
                with rio.open(layer) as src1:
                    #print(src1.tags(1))
                    band = src1.read(1)
                    band.SetMetadata(meta)
                    dst.write_band(id, band)
                 


    







    
    
    
    
    
    
    
    
    
