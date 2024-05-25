#================================卐===========================================
import customtkinter
from win32api import GetSystemMetrics
import shutil
import os
from tkinter import*
from time import*
from tkinter import filedialog
ff=("sunken",25)
ffread=("sunken",35)
fs="sunken",20
widthh=GetSystemMetrics(0)
heightt=GetSystemMetrics(1)
#works
#time funtion UPDATE===========================================================
def update ():
    timestr=strftime("%I:%M:%S %p")
    timelab=customtkinter.CTkLabel(text=timestr,master=root,font=("sunken",30))
    timelab.grid(row=3,column=1)
    timelab.after(1000,update)
#root window===================================================================
root=customtkinter.CTk()
root.geometry("390x150")
root.resizable(False,False)
root.title("helper")
welcome=customtkinter.CTkLabel(master=root,text="🙏namaste!🙏",font=("sunken",35))
welcome.grid(row=1,column=2)
#time button===================================================================
timebutton=customtkinter.CTkButton(text="⏰time",command=update,master=root,font=ff)
timebutton.grid(row=2,column=1)
#quick note===================================================================
def quicknote():
    rot=customtkinter.CTk()
    rot.geometry("700x500")
    notel=customtkinter.CTkLabel(text="📝Quicknote",master=rot,font=ff)
    notel.grid(row=1,column=2)
    note=customtkinter.CTkTextbox(font=(fs),master=rot,width=widthh,height=550)
    note.grid(row=3,column=2)
    notetext=note.get("1.0", "end-1c")
    title=customtkinter.CTkEntry(font=("sunken",25),master=rot,placeholder_text="⚠️Set Title or file wont be saved",width=500)
    title.grid(row=2,column=2)
    rot.title("quicknote")
#save=========================================================================
    def save():
        savebtn.configure(text="Done")
        file=open(f"Quick notes/Quick note={title.get()}.txt","w")
        file.write(note.get("1.0", "end-1c"))
        file.close()
#savebtn=====================================================================
    savebtn=customtkinter.CTkButton(command=save,text="Save✔️",master=rot,font=ff)
    savebtn.grid(row=4,column=2)
#rot mainloop================================================================ 
    rot.mainloop()
# writequick note button===============================================================
quicknotebutton=customtkinter.CTkButton(command=quicknote,font=ff,text="📝write quick note",master=root)
quicknotebutton.grid(row=2,column=2)
#read and write==================================================================
def run_read():  
    read=customtkinter.CTk()
    read.geometry("500x650")
    read.title("Read")
    ff=("sunken",10)
    def open_text():
        text_file1=filedialog.askopenfilename(initialdir="Helper2.0/Quick notes",title="open text file",filetypes=(("Text Files","*.txt"),))
        text_file=open(text_file1,'r')
        stuff=text_file.read()
        my_text.insert(END,stuff)
        text_file.close()
        def save_txt():
            text_file=open(text_file1,'w')
            text_file.write(my_text.get(1.0,END))
            savebtn.configure(text="Done")
        savebtn=customtkinter.CTkButton(text="Save",font=ffread,command=save_txt,master=read)
        savebtn.pack(pady=20)
    
    
    openbtn=customtkinter.CTkButton(text="open text",font=ff,command=open_text,master=read)
    openbtn.pack(pady=5,anchor=N)
    my_text=customtkinter.CTkTextbox(master=read,font=fs,width=widthh,height=500)
    my_text.pack(pady=5)
    read.mainloop()
#btn==================================================================================
readbtn=customtkinter.CTkButton(font=ff,text="Read notes",master=root,command=run_read)
readbtn.grid(row=3,column=2)
#mp3 player====================================================================

#root mainloop=================================================================
root.mainloop()