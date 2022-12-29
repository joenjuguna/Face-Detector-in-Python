
import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import numpy

from PIL import ImageTk, Image
font=cv2.FONT_HERSHEY_COMPLEX_SMALL

top = tk.Tk()
top.geometry('1000x600')
top.title('Face Capture')
top.configure(background='cyan')
def show_convert_button(filepath):
    convert_b = Button(top, text="Capture Face", command=lambda:getimage(filepath), padx=10, pady=5)
    convert_b.place(relx=0.79, rely=0.46)
def show_save_button(imagetaken):
    save_b=Button(top,text='Save', command=lambda:save_button(imagetaken),padx=10,pady=5)
    save_b.place(relx=0.69,rely=0.86)
def save_button(imagetaken):
    where=filedialog.asksaveasfilename(filetypes=(('JPEG Files','*.jpg'),('PNG Files','*.png'),('All Files','*.*')),defaultextension="jpg")
    imagetaken.save(where)
def getimage(filepath):
    imagetaken=cv2.imread(filepath)
    gray=cv2.cvtColor(imagetaken, cv2.COLOR_BGR2GRAY)
    haardata = cv2.CascadeClassifier("data.xml")
    faces=haardata.detectMultiScale(gray,1.1,9)

    for x,y,w,h in faces:
        cv2.rectangle(imagetaken,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(imagetaken,"Face",(x,y),font,1,(244,250,250),1)



    label=Label(top,image=cv2.imshow("FACE",imagetaken))
    label.image=cv2.imshow("FACE",imagetaken)
    label.pack(side="right",expand="yes")

    imagetaken=Image.fromarray(imagetaken)

    show_save_button(imagetaken)


def upload_image():
    filepath = filedialog.askopenfilename()
    uploaded = Image.open(filepath)
    uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
    im = ImageTk.PhotoImage(uploaded)
    label = Label(top, image=im)
    label.image = im
    label.pack(side="left", expand='yes')

    show_convert_button(filepath)


upload = Button(top, text="UPLOAD IMAGE", command=lambda:upload_image(), padx=10, pady=5)
upload.configure(background='black', foreground='white', font=('arial', 10, 'bold'))
upload.place(relx=0.44, rely=0.86)

top.mainloop()


