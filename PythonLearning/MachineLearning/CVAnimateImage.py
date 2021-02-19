import cv2 # For image processing
import easygui   # to open dialogbox/filebox
import tkinter as tk   # For UI components
from tkinter import messagebox
from tkinter import *
import matplotlib.pyplot as plt
import sys
import os


# Below code open a window to select and take image input
top = tk.Tk()
top.geometry('400x400')
top.title('Animate Your Image !')
top.configure(background='white')
label = Label(top, background='#CDCDCD', font=('calibri', 20, 'bold'))

def upload():
    image_path = easygui.fileopenbox()
    animate(image_path)

def animate(image_path):

        # Read image and convert into numpy array
    originalImage = cv2.imread(image_path)
    originalImage = cv2.cvtColor(originalImage,cv2.COLOR_BGR2RGB)
    if originalImage is None:
        print('Not an image file, exiting: ')
        sys.exit()

        # Resize image after each modification to make it the same size
    resize1 = cv2.resize(originalImage,(960,540))
    plt.imshow(resize1,cmap='gray')

        # Creating a greyscale image to extract the edges
    grayImage = cv2.cvtColor(originalImage,cv2.COLOR_BGR2GRAY)

        # resize to show effects
    resize2 = cv2.resize(grayImage,(960,540))
    plt.imshow(resize2,cmap='gray')

        # To smoothen an image, we apply a blur effect.
        # This is done using medianBlur() function, where the middle pixel is assigned a mean value
        # of all the pixels which fall under the kernel. In turn, creating a blur effect
    smoothenImage = cv2.medianBlur(grayImage,5)

    resize3 = cv2.resize(smoothenImage,(960,540))
    plt.imshow(resize2, cmap='gray')

        # To show animation effect, we have to
        # 1. highlight the edges  2. smoothen the colors

        # The threshold value is the mean of the neighborhood pixel values area minus the constant C.
        # C is a constant that is subtracted from the mean or weighted sum of the neighborhood pixels.
        # Thresh_binary is the type of threshold applied, and the remaining parameters determine the block size

    edgeImage = cv2.adaptiveThreshold(smoothenImage,255,
                    cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9,9)

    resize4 = cv2.resize(edgeImage,(960, 540))
    plt.imshow(resize4,cmap='gray')

        # We add bilateral filter to smoothen the color to an extent(keeping edges masked so that they are intact)

    colorImage = cv2.bilateralFilter(originalImage,12,300,300)

    resize5 = cv2.resize(colorImage,(960, 540))
    plt.imshow(resize5,cmap='gray')

        # mask edged image on color Image using bitwise-and

    animatedImage = cv2.bitwise_and(colorImage,colorImage,mask=edgeImage)

    resize6 = cv2.resize(animatedImage,(960, 540))
    plt.imshow(resize6,cmap='gray')

        # Plotting all resized images in a single frame-
    images = [resize1,resize2,resize3,resize4,resize5,resize6]
    fig, axes = plt.subplots(3, 2, figsize=(8, 8), subplot_kw={'xticks': [], 'yticks': []},
                                 gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')
    save1=Button(top,text="Save cartoon image",command=saveButton(resize6,image_path),padx=30,pady=5)
    save1.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
    save1.pack(side=TOP, pady=50)
    plt.show()


# After the image is animated, below will be called to save the image in original image's directory
def saveButton(resizeI,image_path):
    newName = 'animated_Image'
    path1 = os.path.dirname(image_path)
    extension=os.path.splitext(image_path)[1]
    path= os.path.join(path1,newName+extension)

        #cvtColor is used to assure that no color get extracted or highlighted while we save our image
    cv2.imwrite(path,cv2.cvtColor(resizeI,cv2.COLOR_RGB2BGR))
    msg = 'Image: '+ path+ ' saved.'
    tk.messagebox.showinfo(title=None,message=msg)

upload=Button(top,text="Animate an Image",command=upload(),padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
upload.pack(side=TOP,pady=50)

top.mainloop()
