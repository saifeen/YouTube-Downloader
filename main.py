from tkinter import *
from pytube import YouTube

gui = Tk()

gui.geometry("600x700")
gui.config(bg="lightyellow")
gui.title("YTB Downloader")

logo = PhotoImage(file="ytb.png")
gui.iconphoto(False, logo)

Label(gui, text="Download your Video", font=("Arial 30 bold"), fg="red", bg="white").pack(padx=5, pady=50)

url = StringVar()

Label(gui, text="Paste your link below : ",font=("Arial 25 bold"), fg="red", bg="white").place(x=120,y=110)
EntryBox = Entry(gui, width=50, font=30, textvariable=url, bd=4).place(x=50, y=200)

def VDownload():
    try:
        v_url = YouTube(str(url))
        videos = v_url.streams.first()
        videos.download()

        Label(gui, text="Download Completed!", font=("Arial 20 bold"), bg="white", fg="black").place(x=120, y=350)
        Label(gui, text="Video saved in your project folder", font=("Arial 15 bold"), fg="black", bg="white").place(x=100, y=400)
    except Exception as e:
        print(e)
        print("Not Recognized...")

Button(gui, text="DOWNLOAD", font=("Arial 25 bold"), bg="white", fg="red", command=VDownload).place(x=180, y=300)
gui.mainloop()