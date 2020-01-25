#Design patterns used are Builder for creating and Chain of Responsibility for Behaviour 

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import sys
import os
from AugmentedImageData import AugmentedData
from HistrogramApproach import HistrogramApproch
import UnetApproach
import time
# Inheritance from Class Tk which is the window class
class MainApplication(tk.Tk):                                            
    selc_im_path=""
    grnd_path=""
    save_path=""
    save_path_btn={}
    input_path_btn={}
    def selc_orignal_im():
        InteractionElements.sel_orignal_im['bg'] = 'blue'
        # Composition relationship between Class Filedialog and Class Tk
        selc = filedialog.askopenfilename()                                    
        ext_sel = selc.split(".")
        check_sel = ext_sel[-1]
        MainApplication.selc_im_path=selc
        if check_sel != "tif":
            # Composition relationship between Class messagebox and Class Tk 
            messagebox.showerror("Error", "Wrong Input File Extension")        
            InteractionElements.sel_im['bg'] = 'black'
            MainApplication.selc_im_path =""

    def selc_grnd_im():
        InteractionElements.sel_grd_im['bg'] = 'blue'
        grnd_path = filedialog.askopenfilename()
        ext_grd = grnd_path.split(".")
        check_grd = ext_grd[-1]
        MainApplication.grnd_path=grnd_path
        if check_grd != "tif":
            messagebox.showerror("Error", "Wrong Ground thruth File Extension")
            InteractionElements.sel_grd_im['bg'] = 'black'
            MainApplication.grnd_path=""

    def savePathFun (event):
        MainApplication.save_path_btn['bg'] = 'blue'
        MainApplication.save_path = filedialog.askdirectory()


    def selectInputPath (event):
       # print("Inselect pathjS")
        MainApplication.input_path_btn['bg'] = 'blue'
        MainApplication.selc_im_path = filedialog.askdirectory()
        
    ########### Main process will go here ##############
    def processHistrogramImage(ImagePath,grd_path, savePath):
        Process = HistrogramApproch(ImagePath,grd_path,savePath)
        Process.get_Images()
        messagebox.showinfo("Success Message", "Task Done")
     
    def processUnetImage(ImagePath,grd_path, savePath):
        UnetApproach.Initialize_Unet_paths(ImagePath, savePath)
        messagebox.showinfo("Success Message","Task Done")

    def processSplitImage(ImagePath,grd_path, savePath):
        data=AugmentedData(ImagePath,grd_path,savePath)
        data.crop_Color_Images()
        data.crop_Orignal_Images()
        messagebox.showinfo("Success Message","Task Done")
    ####################### END of Main Operation ###############

    def hide(x):
        #print("Hide")
        x.pack_forget()

    def Return_To_Main():
        python = sys.executable
        os.execl(python, python, *sys.argv)
        # os.execl(python, python, "\"{}\"".format(sys.argv[0]))

# Composition relationship between Class Frame and Class Tk

root = tk.Tk() #main
root.geometry("650x650")
var = tk.IntVar()
save_path = tk.StringVar()
separator = tk.Frame(root,height=2, bd=2, relief=tk.SUNKEN)                  
separator.pack(fill=tk.Y, padx=5, pady=50)
title = tk.Label(separator, text = "Micro Structure Segmentation Tool", fg = "black" , font=("Courier", 20)) # Composition relationship between Class Label and Class Tk
title.pack(fill= tk.Y, padx = 10)

body_frame = tk.Frame(root)
body_frame.pack(fill = tk.X, padx = 100, pady=5)

meth_win = tk.Frame(root)
meth_win.pack(fill = tk.X, padx = 100, pady=5)
HistogramButton= tk.Button(body_frame, text = "Image Processing Technique(Histrogram)", activebackground = "green",   height = 2, width =25, bg = "black", fg = "white" , command=lambda:InteractionElements.next_Histogram(InteractionElements))
HistogramButton.pack(fill = tk.X, padx = 100, pady=5)

UnetButton = tk.Button(body_frame, text = "Deep Learning Technique(U-net)", activebackground = "green",   height = 2, width = 25, bg = "black", fg = "white" , command=lambda:InteractionElements.next_Unet(InteractionElements))
UnetButton.pack(fill = tk.X, padx = 100, pady=5)

SplitImageButton = tk.Button(body_frame, text = "Make samples from image", activebackground = "green",   height = 2, width = 15, bg = "black", fg = "white" , command=lambda:InteractionElements.next_splitImage(InteractionElements))
SplitImageButton.pack(fill = tk.X, padx = 100, pady=5)

quit_main_btn = tk.Button(body_frame, text = "Quit",  height = 2, width = 15, bg = "black", fg = "white", command = root.quit)
quit_main_btn.pack(fill = tk.X, padx = 100, pady=5)

class InteractionElements(tk.Tk):   #Inheritance from Class Tk which is the window class

    sel_grd_im=None
    sel_orignal_im=None
    proceed_Histogram_btn=None



    def __init__(self,frame_loc):
        self.frame_loc=tk.Frame(root)
        self.frame_loc.pack(fill = tk.X, padx = 100, pady=5)
        self.frame_loc=frame_loc

    def selc_orignal_im(self):
        sel_im['bg'] = 'blue'
        selc = filedialog.askopenfilename()                                    #Composition relationship between Class Filedialog and Class Tk
        ext_sel = selc.split(".")
        check_sel = ext_sel[-1]
        MainApplication.selc_im_path=selc
        if check_sel != "jpg":
            messagebox.showerror("Error", "Wrong Target File Extension")       #Composition relationship between Class messagebox and Class Tk  
            sel_im['bg'] = 'black'
            MainApplication.selc_im_path =""
    def selc_grnd_im(self):
        sel_grd_im['bg'] = 'blue'
        grnd_path = filedialog.askopenfilename()
        ext_grd = grnd_path.split(".")
        check_grd = ext_grd[-1]
        MainApplication.grnd_path=grnd_path
        if check_grd != "jpg":
            messagebox.showerror("Error", "Wrong Ground thruth File Extension")
            sel_grd_im['bg'] = 'black'
            MainApplication.grnd_path=""
    def savePathFun (self, event):
        #self.save_path_btn['bg'] = 'blue'
        MainApplication.save_path = filedialog.askdirectory()

    def next_fun():
        target = MainApplication.selc_im_path
        #print(target)
        ground = MainApplication.grnd_path
        #print(ground)
        if target != "":
            if ground != "":
                    MainApplication.show(sel_im)
                    MainApplication.show(quit_btn)
                    MainApplication.hide(sel_grd_im)
                    MainApplication.hide(next_win_btn)
                    
                    SelectOption.on_click1()
                    SelectOption.on_click2()

                    MainApplication.save_path_btn = SelectButton.on_save()

                    MainApplication.save_path_btn.bind("<Button-1>",MainApplication.savePathFun)
                    MainApplication.save_path_btn.pack(fill = tk.X, padx = 100, pady=5)
            
                    proc = SelectButton.on_proceed()
                    proc.pack(fill = tk.X, padx = 100, pady=5)
            
                    quit_btn_n = SelectButton.on_quit()
                    quit_btn_n.pack(fill = tk.X, padx = 100, pady=5)
            else:
                messagebox.showerror("Error", "No Ground File Selected")
        else:
            messagebox.showerror("Error", "No  Target File Selected")  

    def next_Histogram(self):
        MainApplication.selc_im_path=""
        MainApplication.grnd_path=""
        MainApplication.save_path=""
        MainApplication.hide(SplitImageButton)
        MainApplication.hide(HistogramButton)
        MainApplication.hide(UnetButton)
        MainApplication.hide(quit_main_btn)
  
        title = tk.Label(body_frame, text = "Histrogram Approach", fg = "black" , font=("Courier", 16, 'bold')) # Composition relationship between Class Label and Class Tk
        title.pack(fill= tk.Y, padx = 10)

        self.sel_grd_im = tk.Button(body_frame, text = "Select Ground truth Image", activebackground = "green",   height = 2, width = 15, bg = "black", fg = "white" , command=lambda:MainApplication.selc_grnd_im())
        self.sel_grd_im.pack(fill = tk.X, padx = 100, pady=5)
        #sel_grd_im.bind("<Button-1>",selc_grnd_im)

        self.sel_orignal_im = tk.Button(body_frame, text = "Select Orignal Image", activebackground = "green",  height = 2, width = 15, bg = "black", fg = "white",command=lambda:MainApplication.selc_orignal_im())
        self.sel_orignal_im.pack(fill = tk.X, padx = 100, pady=5)
        #sel_im.bind("<Button-1>",selc_im)
        MainApplication.save_path_btn = SelectButton.on_save()

        MainApplication.save_path_btn.bind("<Button-1>", MainApplication.savePathFun)
        MainApplication.save_path_btn.pack(fill=tk.X, padx=100, pady=5)

        self.proceed_Histogram_btn = SelectButton.on_proceed()
        self.proceed_Histogram_btn.pack(fill = tk.X, padx = 100, pady=5)
        
        self.ReturnButton =SelectButton.Main_Menu()
        self.ReturnButton.pack(fill = tk.X, padx = 100, pady=5)

        self.quit_btn =SelectButton.on_quit()
        self.quit_btn.pack(fill = tk.X, padx = 100, pady=5)



    def next_Unet(self):
        MainApplication.selc_im_path=""
        MainApplication.grnd_path=""
        MainApplication.save_path=""
        MainApplication.hide(SplitImageButton)
        MainApplication.hide(HistogramButton)
        MainApplication.hide(UnetButton)
        MainApplication.hide(quit_main_btn)
        title = tk.Label(body_frame, text = "Deep Learning Technique(U-net)", fg = "black" , font=("Courier", 16, 'bold')) # Composition relationship between Class Label and Class Tk
        title.pack(fill= tk.Y, padx = 10)
        #  self.sel_orignal_im = tk.Button(body_frame, text = "Select Image", activebackground = "green",  height = 2, width = 15, bg = "black", fg = "white",command=lambda:MainApplication.selc_orignal_im())
        #  self.sel_orignal_im.pack(fill = tk.X, padx = 100, pady=5)


        MainApplication.input_path_btn = SelectButton.on_inputbutton()
        MainApplication.input_path_btn.bind("<Button-1>",MainApplication.selectInputPath)
        MainApplication.input_path_btn.pack(fill = tk.X, padx = 100, pady=5)
        #sel_im.bind("<Button-1>",selc_im)

        MainApplication.save_path_btn = SelectButton.on_save()
        MainApplication.save_path_btn.bind("<Button-1>", MainApplication.savePathFun)
        MainApplication.save_path_btn.pack(fill=tk.X, padx=100, pady=5)

        self.proceed_Histogram_btn = SelectButton.on_proceedUnet()
        self.proceed_Histogram_btn.pack(fill = tk.X, padx = 100, pady=5)

        self.ReturnButton =SelectButton.Main_Menu()
        self.ReturnButton.pack(fill = tk.X, padx = 100, pady=5)

        self.quit_btn =SelectButton.on_quit()
        self.quit_btn.pack(fill = tk.X, padx = 100, pady=5)




    def next_splitImage(self):
        MainApplication.selc_im_path=""
        MainApplication.grnd_path=""
        MainApplication.save_path=""
        MainApplication.hide(SplitImageButton)
        MainApplication.hide(HistogramButton)
        MainApplication.hide(UnetButton)
        MainApplication.hide(quit_main_btn)
        
        title = tk.Label(body_frame, text = "Making Sample of Images", fg = "black" , font=("Courier", 16, 'bold')) # Composition relationship between Class Label and Class Tk
        title.pack(fill= tk.Y, padx = 10)
        self.sel_grd_im = tk.Button(body_frame, text = "Select Ground truth Image", activebackground = "green",   height = 2, width = 15, bg = "black", fg = "white" , command=lambda:MainApplication.selc_grnd_im())
        self.sel_grd_im.pack(fill = tk.X, padx = 100, pady=5)
        #sel_grd_im.bind("<Button-1>",selc_grnd_im)

        self.sel_orignal_im = tk.Button(body_frame, text = "Select Orignal Image", activebackground = "green",  height = 2, width = 15, bg = "black", fg = "white",command=lambda:MainApplication.selc_orignal_im())
        self.sel_orignal_im.pack(fill = tk.X, padx = 100, pady=5)
        #sel_im.bind("<Button-1>",selc_im)

        MainApplication.save_path_btn = SelectButton.on_save()
        MainApplication.save_path_btn.bind("<Button-1>",MainApplication.savePathFun)
        MainApplication.save_path_btn.pack(fill = tk.X, padx = 100, pady=5)

        self.proceed_Histogram_btn = SelectButton.on_proceedSplitImage()
        self.proceed_Histogram_btn.pack(fill = tk.X, padx = 100, pady=5)
        
        self.ReturnButton =SelectButton.Main_Menu()
        self.ReturnButton.pack(fill = tk.X, padx = 100, pady=5)

        self.quit_btn =SelectButton.on_quit()
        self.quit_btn.pack(fill = tk.X, padx = 100, pady=5)

       
        
        

class SelectOption(InteractionElements):                             #Class SelectOption inherited from InteractionElements
    def __init__(self, frame_loc,text,padx,variable,value):
        super().__init__(body_frame)
        self.text=text
        self.padx=padx
        self.variable=variable
        self.value=value  
        
    def on_click1():
        return tk.Radiobutton(body_frame,text="Image Processing Technique",padx=5,variable=var,value=1).pack()

    def on_click2():
        return tk.Radiobutton(body_frame,text="Deep Learning Technique(U-net)",padx=20,variable=var,value=2).pack()

class SelectButton(InteractionElements):                             #Class SelectButton inherited from InteractionElements
    def __init__(self, frame_loc,text,height,width,bg,fg,command):
            super().__init__(body_frame)
            self.text=text
            self.height=height
            self.width=width
            self.bg=bg
            self.fg=fg
            self.command=command
    def on_save():
        return tk.Button(meth_win, text = "Select Folder to Save",   height = 2, width = 15, bg = "black", fg = "white")
            
    def on_proceed():
        return tk.Button(meth_win, text = "Proceed",  height = 2, width = 15, bg = "black", fg = "white", command=lambda:MainApplication.processHistrogramImage(MainApplication.selc_im_path,MainApplication.grnd_path,MainApplication.save_path))
  
    def on_quit():
        return tk.Button(meth_win, text = "Quit",  height = 2, width = 15, bg = "black", fg = "white", command=lambda:root.quit())

    def on_proceedUnet():
        return tk.Button(meth_win, text = "Proceed",  height = 2, width = 15, bg = "black", fg = "white", command=lambda:MainApplication.processUnetImage(MainApplication.selc_im_path,MainApplication.grnd_path,MainApplication.save_path))

    def on_proceedSplitImage():
        return tk.Button(meth_win, text = "Proceed",  height = 2, width = 15, bg = "black", fg = "white", command=lambda:MainApplication.processSplitImage(MainApplication.selc_im_path,MainApplication.grnd_path,MainApplication.save_path))


    def on_inputbutton():
        return tk.Button(meth_win, text = "Select Input Image Folder",   height = 2, width = 15, bg = "black", fg = "white")

    def Main_Menu():
        return tk.Button(meth_win, text = "Return To Main Page",  height = 2, width = 15, bg = "black", fg = "white", command=lambda:MainApplication.Return_To_Main())



     
tk.mainloop()
