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
image=ImageTk.PhotoImage(Image.open("assistant.jpg"))
image_label=Label(root,image=image)
image_label.grid(row=1,column=0,pady=20)






root.tk.mainloop()