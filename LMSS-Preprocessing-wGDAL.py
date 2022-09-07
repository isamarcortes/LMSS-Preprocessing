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
#import numpy as np
#import pandas as pd

#from osgeo import gdal, gdalconst

###location of tar files
FileLocation = '/Users/isamarcortes/Downloads/LMSS_Data'###change this to folder where you have tar files stored
FileSorting = sorted(glob.glob(FileLocation+'/*.tar'))



FolderNamesAppend = []####appending all folder names to a list to use for image processing later
for i in FileSorting:
    '''
    # This first forloop creates the folders where we will be unzipping the data to
    # by creating a folder with the same name as the file. It then extracts all the contents
    # of the tar file and places said contents into the new directory that was just created
    '''
    FolderName = i.split('.')[0]
    FolderNamesAppend.append(FolderName)
    subprocess.call('mkdir -p '+FolderName,shell=True)
    FileOpen = tr.open(i)
    FileOpen.extractall(FolderName)
    FileOpen.close()
'''
'''
########this chunk of code adds the metadata to the bands
# for MD in FolderNamesAppend:
#     IMGName = MD.split('/')[5]
#     MetadataTxtFile = sorted(glob.glob(MD+'/'+IMGName+'_MTL.txt'))###sorts metadata files
#     for test in MetadataTxtFile:
#         hmm = MetaData(test)
  

AllMetaData = []
#MetadataTxtFiles = []
#######this part of code stacks tif  
for k in FolderNamesAppend:
    ImageName = k.split('/')[5]
    #print(ImageName)
    Images = sorted(glob.glob(k+'/*.TIF'))#this isolates only files with extension .tif in each folder   
    

    for m in Images: #iterate through the images in each folder
        with rio.open(m,'r+') as src:
            meta = src.profile##grab the metadata from tifs
            meta.update(count = len(Images))#update part of metadata to include stacked images
        
        with rio.open('/Users/isamarcortes/Desktop/LMSS-Preprocessing/StackTifs/'+ImageName+'_stack.tif', 'w', **meta) as dst:#change this to be in a root folder
        ###This forloop writes the new band. Repurposed code from here:
            #https://gis.stackexchange.com/questions/223910/using-rasterio-or-gdal-to-stack-multiple-bands-without-using-subprocess-commands
            for id, layer in enumerate(Images, start=1):
                with rio.open(layer) as src1:
                    band = src1.read(1)
                    dst.write_band(id, band)



######need this to get text files in a list
#AllTxTFiles = []
CreatedTifFiles = '/Users/isamarcortes/Desktop/LMSS-Preprocessing/StackTifs/*.tif' ####this is where images are stored 
FileSortedTifs = sorted(glob.glob(CreatedTifFiles)) 
for MD in FolderNamesAppend:
    IMGName = MD.split('/')[5]
    
    
    #### I need to figure this part out
    MetadataTxtFile = sorted(glob.glob(MD+'/'+IMGName+'_MTL.txt'))###sorts metadata files
    for files in FileSortedTifs:
        for text in MetadataTxtFile:
            #test = open(text,'r').read()
            with open(text) as rd:
                items = rd.readlines()
                for values in items:
                    values = values.strip('\n')
                    values = values.replace(' ','')
                    subprocess.call('gdal_edit.py -mo '+values+' '+files,shell=True)
