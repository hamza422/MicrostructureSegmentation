import numpy as np
import cv2
from PIL import Image
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
from  tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

class staticClass:
    selc_im_path=""
    grnd_path=""
    save_path=""
    
root = Tk() #main
root.geometry("570x500")

var = IntVar()
save_path = StringVar()

def selc_im():
    sel_im['bg'] = 'blue'
    selc = filedialog.askopenfilename()
    ext_sel = selc.split(".")
    check_sel = ext_sel[-1]
    staticClass.selc_im_path=selc
    if check_sel != "png":
        messagebox.showerror("Error", "Wrong Target File Extension")
        sel_im['bg'] = 'black'
        staticClass.selc_im_path =""
def selc_grnd_im():
    sel_grd_im['bg'] = 'blue'
    grnd_path = filedialog.askopenfilename()
    ext_grd = grnd_path.split(".")
    check_grd = ext_grd[-1]
    staticClass.grnd_path=grnd_path
    if check_grd != "png":
        messagebox.showerror("Error", "Wrong Ground thruth File Extension")
        sel_grd_im['bg'] = 'black'
        staticClass.grnd_path=""
def savePathFun (event):
    staticClass.save_path = filedialog.askdirectory()
    

########### Main process will goes here ##############
def processImage(ImagePath,grd_path, savePath):

    color_img = cv2.imread(grd_path,1)
    original_img = cv2.imread(ImagePath,0)
    path = savePath

    rows_color,cols_color,channels_c = color_img.shape
    rows_original,cols_original,channels_o = color_img.shape
    #output_image = np.zeros([rows_color, cols_color, 3], dtype=np.uint8)
    output_image = cv2.imread(ImagePath,1)
    buf = []
    A = []
    number_of_segments = 0
    count_red = 0
    count_green = 0
    count_blue = 0
    id=0
    for x in range(0, 250, 10):
      for y in range(0, 250, 10):
        for z in range(0, 250, 10):
          sought = [x, y, z]
          # Find all pixels where the 3 RGB values match "sought", and count
          result = np.count_nonzero(np.all(color_img == sought, axis=2))
          if result != 0:
            co_i = []
            co_j = []
            print('\n*******************************')
            print('\n\nsegment found')
            print("\nNumber of pixels in this segment")
            print(result)
            #print("\n")
            number_of_segments = number_of_segments + 1
            for i in range(rows_color):
              for j in range(cols_color):
                if color_img[i,j][0] == sought[0] and color_img[i,j][1] == sought[1] and color_img[i,j][2] == sought[2]:
                    buf.append(original_img[i][j])
                    co_i.append(i)
                    co_j.append(j)

            print("\nLength of buffer")
            print(len(buf))
            print("\nLength of co-ordinate array")
            print(len(co_i))
            A.append(np.mean(buf))
            print("\nMean buffer value of the segment")
            print(np.mean(buf))

            if np.mean(buf) < 130.0:
              for a in range(0, len(co_i), 1):
                #print("Test1")
                #print("pixel co-ordinates are :" )
                #print(co_i[a],co_j[a])
                #output_image.putpixel(((co_i[a]), (co_j[a])), (255, 0, 0, 255))
                output_image[(co_i[a]), (co_j[a])][0] = 255
                output_image[(co_i[a]), (co_j[a])][1] = 0
                output_image[(co_i[a]), (co_j[a])][2] = 0
                count_red = count_red+1
              print("\nSegment colored red")
              print("\nNumber of pixels colored")
              print(count_red)
                        
            elif np.mean(buf) >  130.0 and np.mean(buf) < 180.0:
              for a in range(0, len(co_i), 1):
                #print("Test2")
                #print("pixel co-ordinates are :")
                #print(co_i[a], co_j[a])
                #output_image.putpixel(((co_i[a]), (co_j[a])), (0, 255, 0, 255))
                output_image[(co_i[a]), (co_j[a])][0] = 0
                output_image[(co_i[a]), (co_j[a])][1] = 255
                output_image[(co_i[a]), (co_j[a])][2] = 0
                count_green=count_green+1
              print("\nSegment colored green")
              print("\nNumber of pixels colored")
              print(count_green)
                  
            elif np.mean(buf) > 180.0:
              for a in range(0, len(co_i), 1):
                #print("Test3")
                #print("pixel co-ordinates are :")
                #print(co_i[a], co_j[a])
                #output_image.putpixel(((co_i[a]), (co_j[a])), (0, 0, 255, 255))
                output_image[(co_i[a]), (co_j[a])][0] = 0
                output_image[(co_i[a]), (co_j[a])][1] = 0
                output_image[(co_i[a]), (co_j[a])][2] = 255
                count_blue=count_blue+1
              print("\nSegment colored blue")
              print("\nNumber of pixels colored")
              print(count_blue)

            else:
              print("\nNothing done")

            #A = np.asarray(buf)
            #buf.clear()
            del buf[:]
            del co_i[:]
            del co_j[:]
            count_red = 0
            count_green = 0
            count_blue = 0

    print(A)
    print("\nNumber of segments")
    print(number_of_segments)
    cv2.imshow('color_img',color_img)
    cv2.imshow('original_img',original_img)
    cv2.imshow('output_img',output_image)
    print(path)
    cv2.imwrite(path+"/finalResult.jpg",output_image)
	  #cv2.imwrite(path+'finalResult.jpg',output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


####################### END of Main Operation ###############

def hide(x):
    #print("Hide")
    x.pack_forget()

separator = Frame(root,height=2, bd=2, relief=SUNKEN)
separator.pack(fill=Y, padx=5, pady=50)
title = Label(separator, text = "Micro Structure Segmentation Tool", fg = "black" , font=("Courier", 20))
title.pack(fill= Y, padx = 10)

body_frame = Frame(root)
body_frame.pack(fill = X, padx = 100, pady=5)

meth_win = Frame(root)
meth_win.pack(fill = X, padx = 100, pady=5)

#### select button function
def next_fun():
    target = staticClass.selc_im_path
    #print(target)
    ground = staticClass.grnd_path
    #print(ground)
    if target != "":
        if ground != "":
                hide(sel_im)
                hide(quit_btn)
                hide(sel_grd_im)
                hide(next_win_btn)
                
                Radiobutton(body_frame, text="Image Processing Technique",padx = 5,  variable = var, value = 1).pack()
                Radiobutton(body_frame, text="Neural Netwrok Technique(U-NET)",padx = 20,  variable = var, value = 2, state = DISABLED).pack()
                
                save_path_btn = Button(meth_win, text = "Select Folder to Save",   height = 2, width = 15, bg = "black", fg = "white")
                save_path_btn.bind("<Button-1>",savePathFun)
                save_path_btn.pack(fill = X, padx = 100, pady=5)
        
                proc = Button(meth_win, text = "Proceed",  height = 2, width = 15, bg = "black", fg = "white", command=lambda:processImage(target,ground,staticClass.save_path))
                proc.pack(fill = X, padx = 100, pady=5)
        
                quit_btn_n = Button(meth_win, text = "Quit",  height = 2, width = 15, bg = "black", fg = "white", command = root.quit)
                quit_btn_n.pack(fill = X, padx = 100, pady=5)
        else:
            messagebox.showerror("Error", "No Ground File Selected")
    else:
        messagebox.showerror("Error", "No  Target File Selected")  
    
            
        
sel_grd_im = Button(body_frame, text = "Select Ground truth Image", activebackground = "green",   height = 2, width = 15, bg = "black", fg = "white" , command=lambda:selc_grnd_im())
sel_grd_im.pack(fill = X, padx = 100, pady=5)
#sel_grd_im.bind("<Button-1>",selc_grnd_im)

sel_im = Button(body_frame, text = "Select Image", activebackground = "green",  height = 2, width = 15, bg = "black", fg = "white",command=lambda:selc_im())
sel_im.pack(fill = X, padx = 100, pady=5)
#sel_im.bind("<Button-1>",selc_im)

next_win_btn = Button(body_frame, text = "Next",  activebackground = "green", height = 2, width = 15, bg = "black", fg = "white", command=lambda:next_fun())
next_win_btn.pack(fill = X, padx = 100, pady=5)

quit_btn = Button(body_frame, text = "Quit",  height = 2, width = 15, bg = "black", fg = "white", command = root.quit)
quit_btn.pack(fill = X, padx = 100, pady=5)


mainloop()