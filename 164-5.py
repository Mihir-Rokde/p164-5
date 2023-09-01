from tkinter import*
from tkinter import filedialog
from PIL import ImageTk,Image
root=Tk()
root.geometry("600x600")
root.configure(background="lightblue")
labelimg=Label(root,background="white",highlightthickness=5)
labelimg.place(relx=0.5,rely=0.5,anchor=CENTER)
imgpath=""
def openfile():
    global imgpath
    imgpath=filedialog.askopenfilename(title="open  text  file",filetypes=[("*.jpg *.gif *.jpg *.png *.jpeg")])
    print(imgpath)
    im=Image.open(imgpath)
    img=ImageTk.PhotoImage(im)
    labelimg["image"]=img
    img.close()

def rotateimg():
    global imgpath
    im=Image.open(imgpath)
    img=ImageTk.PhotoImage(im.rotate(180))
    labelimg["image"]=img
    print(imgpath)
    img.close()

btn=Button(root,text="Open Image",command=openfile,relief=SOLID,padx=15,pady=10)
btn.place(relx=0.5,rely=0.1,anchor=CENTER)

btn1=Button(root,text="Rotate Image",command=rotateimg,relief=SOLID,padx=15,pady=10)
btn1.place(relx=0.5,rely=0.85,anchor=CENTER)

footer=Label(root,text="Created by Mihir Rokde")
footer.place(relx=0.5,rely=0.95,anchor=CENTER)

root.mainloop()