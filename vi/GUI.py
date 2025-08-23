from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("MosaqAI-Assistant")
root.geometry("550x675")
root.resizable(False,False)
root.config(bg="#6F8FAF")

#frame
frame=LabelFrame(root,padx=100,pady=7,borderwidth=3,relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0,column=1,padx=55,pady=10)

#texetable

text_label= Label(frame,text="MosaqAI-Assistant",font=("comic Sans MS",14,"bold"),highlightthickness=2, highlightbackground="#356696")
text_label.grid(row=0,column=0,padx=20,pady=10)

#image
image=ImageTk.PhotoImage(Image.open("image/sed.jpeg"))
image_label=Label(frame,image=image)
image_label.grid(row=1,column=0,pady=20)

#adding A Text widget
text=Text(root,font=('courier 10 bold'),bg="#356696")
text.grid(row=2,column=0)
text.place(x=10,y=300,height=90)

#adding entry widgit

entry=Entry(root,justify=CENTER)
entry.place(x=100,y=450,width=350,height=30)


root.tk.mainloop()