from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
root=Tk()
root.title("YouTube VIDEO DOWNLOADER")
root.geometry("800x700")
root.grid_columnconfigure(0,weight=1)


folder_name = ""

def openlocation():
	global folder_name
	folder_name=filedialog.askdirectory()
	pathlabel.config(text=folder_name,fg="white")
	location.config(text="")
		
	

def DownloadVideo():
	downloadmsg.config(text="",fg="blue")
	choice = ytdchoices.get()
	url = ytdEntry.get()
	if(len(url)<1):
		ytdError.config(text="please enter link",fg="red")
	if(len(folder_name)<1):
		locationError.config(text="please select path")
	else:
		ytdError.config(text="")
		try:
			yt = YouTube(url)
			try:
				
				if(choice == choices[0]):
					select = yt.streams.filter(progressive=True).first()
				elif(choice == choices[1]):
					select = yt.streams.filter(progressive=True,file_extension='mp4').last()
				elif(choice == choices[2]):
					select = yt.streams.filter(only_audio=True).first()
				try:
					select.download(folder_name)
					ytdEntry.delete(0,"end")
					pathlabel.config(text="\t\t\t            ")
					downloadmsg.config(text="Download Completed!!",fg="blue")
					location.config(text="YOU WILL GET VIDEO AT LOCATION :  "+folder_name)
					
				except :
					downloadmsg.config(text=" DOWNLOAD FAIL",fg="red")
			except :
				ytdError.config(text="Enter path again")

		except :
			ytdError.config(text="Enter valid path")
 


    		

heading=Label(root,text="..YOUTUBE VIDEO DOWNLOADER..",font=("jost",20))
heading.grid()
ytdlabel=Label(root,text="ENTER URL OF VIDEO:",font=("jost",15))
ytdlabel.grid(pady=30)


ytdEntryVar=StringVar()
ytdEntry=Entry(root,width=70,textvariable=ytdEntryVar)
ytdEntry.grid(pady=(0,10))


ytdError=Label(root,text=" ",fg="red",font=("jost",15))
ytdError.grid()


ytdquality=Label(root,text="select qualaity:",font=("jost",15))
ytdquality.grid(pady=(20))


choices=["720p","144","Only Audio"]
ytdchoices=ttk.Combobox(root,values=choices,width=50,)
ytdchoices.grid(pady=(0,10))

savelabel=Label(root,text="select loacation",font=("jost",15))
savelabel.grid(pady=20)


pathlabel=Label(root,text="path",bg="gray",width=50,font=("jost",15))
pathlabel.grid()
saveEntry=Button(root,text="choose path", width=15,fg="white",bg="gray",font=("jost",12),command=openlocation)
saveEntry.grid(pady=10)

locationError=Label(root,text=" ",fg="red",font=("jost",10))
locationError.grid()




download=Button(root,text="Download video", width=20,fg="white",bg="gray", font=("jost",15),command=DownloadVideo)
download.grid(pady=30)

downloadmsg=Label(root,text=" ",fg="black",font=("jost",15))
downloadmsg.grid(pady=20)
location=Label(root,text=" ",font=("jost",10,"bold"))
location.grid(pady=10)
Name=Label(root,text=" ",font=("jost",10,"bold"))
Name.grid(pady=10)

Size=Label(root,text=" ",font=("jost",10,"bold"))
Size.grid(pady=10)







root.mainloop()



