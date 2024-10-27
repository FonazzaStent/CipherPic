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

from tkinter import *
import base64
from PIL import Image, ImageTk
from io import BytesIO
import pwinput
import os

def base64_to_image(base64_string):
    # Remove the data URI prefix if present
    if "data:image" in base64_string:
        base64_string = base64_string.split(",")[1]
    # Decode the Base64 string into bytes
    image_bytes = base64.b64decode(base64_string)
    return image_bytes

def create_image_from_bytes(image_bytes):
    # Create a BytesIO object to handle the image data
    image_stream = BytesIO(image_bytes)
    # Open the image using Pillow (PIL)
    image = Image.open(image_stream)
    return image

filexists=False

while filexists==False:
    imgfilename=input("Encrypted image filename: ")
    if os.path.isfile(imgfilename)== True:
        filexists= True

txtimg=open(imgfilename,'r')
txtimgwrite=open("decimg.64",'w', encoding='utf-8')
txtimgstring=txtimg.read()

key='a'

while key.isdigit()==False:
    key=pwinput.pwinput(prompt='Password: ', mask='*')

#key="1452"
keylength=len(key)-1

keyindex=0
length=len(txtimgstring)


for n in range (0,length):
    
    char=ord(txtimgstring[n])
    newcharcode=char-int(key[keyindex])
    if newcharcode<0:
        newcharcode=(newcharcode+128)
    #print (newcharcode)
    newchar=chr(newcharcode)
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


# Example usage
encfile=open("decimg.64",'r')
base64_string=encfile.read()
#base64_string = "your_base64_string_here"
image_bytes = base64_to_image(base64_string)
im= create_image_from_bytes(image_bytes)

w,h=im.size
ratio=w/h
height=600
width=int(height*ratio)

im2=im.resize((width,height),Image.Resampling.BICUBIC)

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
resolution=(str(width)+'x'+str(height))
win.geometry(resolution)
win.title('PicView')
win.resizable(0,0)

frame = Frame(win, width=width, height=height)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(im2)

label = Label(frame, image = img)
label.pack()

win.mainloop()
encfile.close()
os.remove("decimg.64")
