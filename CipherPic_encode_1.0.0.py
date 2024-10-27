"""CipherPic 1.0.0 - Encrypt and decrypt an image
Copyright (C) 2023  Fonazza-Stent

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import pwinput
import base64
from pathvalidate import is_valid_filename
import os

filexists=False

while filexists==False:
    imgfilename=input("Image filename: ")
    if os.path.isfile(imgfilename)== True:
        filexists= True

validfilename=False

while validfilename== False:
    encimgfilename=input("Encoded image filename: ")
    if is_valid_filename(encimgfilename)==True:
        validfilename=True
    

imgfile=open(imgfilename,'rb')
encoded_img=open("img.64",'w')
imgdata = imgfile.read()
imgdata = base64.b64encode(imgdata)
imgdatastring=str(imgdata)
imgdatastring=imgdatastring[2:-1]
encoded_img.write(imgdatastring)
encoded_img.close()

txtimg=open("img.64",'r')
txtimgwrite=open(encimgfilename,'w', encoding='utf-8')
txtimgstring=txtimg.read()

key='a'

while key.isdigit()==False:
    key=pwinput.pwinput(prompt='Password: ', mask='*')


#key="12345678"
keyindex=0
length=len(txtimgstring)
keylength=len(key)-1


for n in range (0,length):
    
    char=ord(txtimgstring[n])
    newcharcode=char+int(key[keyindex])
    if newcharcode>127:
        newcharcode=(newcharcode-128)
    #print (newcharcode)
    newchar=chr(newcharcode)
    #print (newchar)
    keyindex=keyindex+1
    if keyindex>keylength:
        keyindex=0
    #txtimgwrite.write(newchar)
    try:
        txtimgwrite.write(newchar)
    except Exception as e:
        print (key[keyindex],newcharcode,newchar)
        print (txtimgstring[n],n)
        print (e)
        txtimgwrite.close()
        quit()

txtimg.close()
txtimgwrite.close()
os.remove("img.64")
print ("ok")
    
    
    
