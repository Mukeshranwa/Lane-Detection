import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import os
import numpy as np
import main

global last_frame1                                   
last_frame1 = np.zeros((480, 640, 3), dtype=np.uint8)
global last_frame2                                      
last_frame2 = np.zeros((480, 640, 3), dtype=np.uint8)
global cap1
global cap2

# Enter path of lane.mp4 file in sample folder as follows
cap1 = cv2.VideoCapture("D:\\Atharva\\VIT Bhopal\\4. Winter Semester 2022-23\\DSN2099\\Lane Detection OpenCV Final\\Sample\\Lane.mp4")

# Enter path of output.mp4 file in sample folder as follows
cap2 = cv2.VideoCapture("D:\\Atharva\\VIT Bhopal\\4. Winter Semester 2022-23\\DSN2099\\Lane Detection OpenCV Final\\Sample\\output.mp4")

def show_vid():                                   
    if not cap1.isOpened():                             
        print("cant open the camera1")
    
    flag1, frame1 = cap1.read()
    frame1 = cv2.resize(frame1,(675,475))
    if flag1 is None:
        print ("Major error!")
    elif flag1:
        global last_frame1
        last_frame1 = frame1.copy()
        pic = cv2.cvtColor(last_frame1, cv2.COLOR_BGR2RGB)     
        img = Image.fromarray(pic)
        imgtk = ImageTk.PhotoImage(image=img)
        before.imgtk = imgtk
        before.configure(image=imgtk)
        root.update_idletasks()
        root.update()
        before.after(10, show_vid)

def show_vid2():
    if not cap2.isOpened():                             
        print("cant open the camera2")
    
    flag2, frame2 = cap2.read()
    frame2 = cv2.resize(frame2,(675,475))
    if flag2 is None:
        print ("Major error2!")
    elif flag2:
        global last_frame2
        last_frame2 = frame2.copy()
        pic2 = cv2.cvtColor(last_frame2, cv2.COLOR_BGR2RGB)
        img2 = Image.fromarray(pic2)
        img2tk = ImageTk.PhotoImage(image=img2)
        after.img2tk = img2tk
        after.configure(image=img2tk)
        root.update_idletasks()
        root.update()
        after.after(10, show_vid2)

if __name__ == '__main__':

    exec(open('main.py').read())
    
    root = tk.Tk()
    root.update_idletasks()
    root.update()                               
    before = tk.Label(master=root)
    after = tk.Label(master=root)
    
    font14 = "-family {Segoe UI} -size 20 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
    font16 = "-family {Swis721 BlkCn BT} -size 20 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
    font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
    _bgcolor = '#A9A9A9'
    _fgcolor = '#FFFFFF'
    before.place(relx = 0.04, rely = 0.2)
    after.place(relx = 0.52, rely = 0.2)
    root.title("Lane-line detection")            
    root.geometry("1011x750+100+10") 
    root.configure(background = "#000000")
    root.configure(highlightbackground = "#A9A9A9")
    root.configure(highlightcolor = "black")
    root.attributes('-fullscreen', True)
    root.attributes("-topmost", True)
    root.bind('<Escape>', lambda e: root.destroy())

    Message1 = Message(root)
    Message1.place(relx = 0.11, rely = 0.1, relheight = 0.10, relwidth = 0.3)
    Message1.configure(relief = "raised")
    Message1.configure(borderwidth = 8)
    Message1.configure(background = "#000000")
    Message1.configure(font = font16)
    Message1.configure(foreground = "#FFFFFF")
    Message1.configure(highlightbackground = "#308014")
    Message1.configure(highlightcolor = "black")
    Message1.configure(text = '''ORIGINAL''')
    Message1.configure(width = 791)

    Message2 = Message(root)
    Message2.place(relx = 0.6, rely = 0.1, relheight = 0.10, relwidth = 0.3)
    Message2.configure(relief = "raised")
    Message2.configure(borderwidth = 8)
    Message2.configure(background = "#000000")
    Message2.configure(font = font16)
    Message2.configure(foreground = "#FFFFFF")
    Message2.configure(highlightbackground = "#308014")
    Message2.configure(highlightcolor = "black")
    Message2.configure(text = '''AFTER LANE DETECTION''')
    Message2.configure(width = 791)

    Button = Button(root)
    Button.place(relx = 0.455, rely = 0.90, height = 50, width = 150)
    Button.configure(fg = "black")
    Button.configure(text = "QUIT")
    Button.configure(command = root.destroy)
    Button.configure(font = font14)
    
    show_vid()
    show_vid2()
    root.mainloop()