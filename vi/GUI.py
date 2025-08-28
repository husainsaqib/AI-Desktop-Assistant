from tkinter import *
from PIL import Image,ImageTk
import speech_to_text
import action
root=Tk()
root.title("MosaqAI-Assistant")
root.geometry("550x675")
root.resizable(False,False)
root.config(bg="#6F8FAF")

#ask fun
def ask():
    ask_val=speech_to_text.speech_to_text()
    user_val=action.Action(ask_val)
    text.insert(END,'User-->'+ask_val+"\n")
    if user_val!=None:
        text.insert(END,"BOT<--"+str(user_val)+"\n")
    if user_val=="ok sir":
        root.destroy()
 
#send fun
def send():
    print("send")

#del_text
def del_text():
    print("delete")

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
entry.place(x=100,y=430,width=350,height=30)

#button1

Button1=Button(root,text="ASK",bg="#356696",pady=16,padx=30,borderwidth=3,relief=SOLID,command=ask)
Button1.place(x=70,y=500)

#button 2
Button2=Button(root,text="SEND",bg="#356696",pady=16,padx=30,borderwidth=3,relief=SOLID,command=send)
Button2.place(x=400,y=500)

#button 3
Button3=Button(root,text="DELETE",bg="#356696",pady=16,padx=30,borderwidth=3,relief=SOLID,command=del_text)
Button3.place(x=225,y=500)

root.tk.mainloop()