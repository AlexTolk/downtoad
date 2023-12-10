# подключаем библиотеки
from tkinter import *
import pytube
from tkinter import messagebox

# main window
root=Tk()
root.geometry("750x350")
root.resizable(False,False)
# window title
root.title("DownToad")
# background color
root.config(bg='#D3D3D3')

# Download button
def download():
    # try to download a video using a link
    try:
        # forming an address
        ytlink=link1.get()
        # converting it into a suitable format
        youtubelink=pytube.YouTube(ytlink)
        # getting a link to the video with the highest resolution
        video=youtubelink.streams.get_highest_resolution()
        # downloading a video
        video.download()
        # outputing the result
        Result="Download complete"
        messagebox.showinfo("Done",Result)
    # if download failed
    except:
        # outputing error
        Result="The link isn't working"
        messagebox.showerror("Error",Result)

# reseting the link
def reset():
    link1.set("")

# exit button
def Exit():
    root.destroy()

# form label
lb=Label(root,text="Downtoad - YT downloader",font=('Arial,15,bold'),bg='#D3D3D3')
lb.pack(pady=15)
lb1=Label(root,text="Link to the video",font=('Arial,15,bold'),bg='#D3D3D3')
lb1.place(x=10,y=80)

# video address input
link1=StringVar()
En1=Entry(root,textvariable=link1,font=('Arial,15,bold'))
En1.place(x=230,y=80)

# download button
btn1=Button(root,text="Download",font=('Arial,10,bold'),bd=4,command=download)
btn1.place(x=330,y=130)

# Clear and exit buttons
btn2=Button(root,text="Clear",font=('Arial,10,bold'),bd=4,command=reset)
btn2.place(x=160,y=190)
btn3=Button(root,text=" Exit ",font=('Arial,10,bold'),bd=4,command=Exit)
btn3.place(x=250,y=190)

# start window
root.mainloop()
