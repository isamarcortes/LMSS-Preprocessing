#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 11:39:26 2022

@author: isamarcortes
"""
import pandas as pd


def MetaData(TXT):
    b4Name = TXT.loc[TXT['GROUP = LANDSAT_METADATA_FILE'].str.contains('BAND_4')]
    b4MetaData = (pd.DataFrame(b4Name['GROUP = LANDSAT_METADATA_FILE'].str.split('=',1).tolist(),
                         columns = ['Name','Value']))
    b4MetaData=	b4MetaData.set_index('Name').to_dict()['Value']
    
    
    b5Name = TXT.loc[TXT['GROUP = LANDSAT_METADATA_FILE'].str.contains('BAND_5')]
    b5MetaData = (pd.DataFrame(b5Name['GROUP = LANDSAT_METADATA_FILE'].str.split('=',1).tolist(),
                         columns = ['Name','Value']))
    b5MetaData=	b5MetaData.set_index('Name').to_dict()['Value']
    
    
    b6Name = TXT.loc[TXT['GROUP = LANDSAT_METADATA_FILE'].str.contains('BAND_6')]
    b6MetaData = (pd.DataFrame(b6Name['GROUP = LANDSAT_METADATA_FILE'].str.split('=',1).tolist(),
                         columns = ['Name','Value']))
    b6MetaData=	b6MetaData.set_index('Name').to_dict()['Value']
    
    
    b7Name = TXT.loc[TXT['GROUP = LANDSAT_METADATA_FILE'].str.contains('BAND_7')]
    b7MetaData = (pd.DataFrame(b7Name['GROUP = LANDSAT_METADATA_FILE'].str.split('=',1).tolist(),
                         columns = ['Name','Value']))
    b7MetaData=	b7MetaData.set_index('Name').to_dict()['Value']
    
    
    bQualitlyL1Pixel_Name = TXT.loc[TXT['GROUP = LANDSAT_METADATA_FILE'].str.contains('QUALITY_L1_PIXEL')]
    bQualitlyL1Pixel_MetaData = (pd.DataFrame(bQualitlyL1Pixel_Name['GROUP = LANDSAT_METADATA_FILE'].str.split('=',1).tolist(),
                         columns = ['Name','Value']))
    bQualitlyL1Pixel_MetaData=	bQualitlyL1Pixel_MetaData.set_index('Name').to_dict()['Value']
    
    
    bQualitlyL1RADIOMETRIC_SATURATIONPixel_Name = TXT.loc[TXT['GROUP = LANDSAT_METADATA_FILE'].str.contains('L1_RADIOMETRIC_SATURATION')]
    bQualitlyL1RADIOMETRIC_SATURATIONPixel_MetaData = (pd.DataFrame(bQualitlyL1RADIOMETRIC_SATURATIONPixel_Name ['GROUP = LANDSAT_METADATA_FILE'].str.split('=',1).tolist(),
                         columns = ['Name','Value']))
    bQualitlyL1RADIOMETRIC_SATURATIONPixel_MetaData = bQualitlyL1RADIOMETRIC_SATURATIONPixel_MetaData.set_index('Name').to_dict()['Value']
    
    
    
    return b4MetaData, b5MetaData, b6MetaData, b7MetaData, bQualitlyL1Pixel_MetaData,bQualitlyL1RADIOMETRIC_SATURATIONPixel_MetaData 

#b4, b5, b6, b7,bQ1,bQ2 = MetaData(OpenMetaTxt)

