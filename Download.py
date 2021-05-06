#!/bin/python3

import download
import re

File_Pach     =  input ('Enter File Pach : ')
File_name     =  input ('Enter File Name : ')
Download_Pach =  input ('Enter Download file pach(. is directory  ) : ')

if Download_Pach =='.':
    Download_Pach = File_Pach

FILE = open(File_Pach+'/'+File_name , 'r' )

text = FILE.read()
URL_List = re.findall( 'http.+/.*'  , text)

for i in range( len(URL_List)):
    download.download( URL_List[i]  , Download_Pach+str(i)  )
    
