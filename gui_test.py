#!/usr/bin/python
"""
- read output from a subprocess in a background thread
- show the output in the GUI
"""
from tkinter import *
#import time  #required for sleep 
import socket #required for getting IP Address
import os  #required to get IP Address
import subprocess  #required to run shell commands
import webbrowser

from guizero import App, Text, TextBox, PushButton, Box


####################### To display the output of shell commands as a window #####################
import sys
from itertools import islice
from subprocess import Popen, PIPE
from textwrap import dedent
from threading import Thread

try:
    import Tkinter as tk
    from Queue import Queue, Empty
except ImportError:
    import tkinter as tk # Python 3
    from queue import Queue, Empty # Python 3

def iter_except(function, exception):
    """Works like builtin 2-argument `iter()`, but stops on `exception`."""
    try:
        while True:
            yield function()
    except exception:
        return

class DisplaySubprocessOutputDemo:
    def __init__(self, root, query):
        self.root = root

        # start dummy subprocess to generate some output
        self.process = Popen([sys.executable, "-u", "-c", dedent("""
            import subprocess
            subprocess.call('"""+query+"""', shell=True)
            """)], stdout=PIPE)

        # launch thread to read the subprocess output
        #   (put the subprocess output into the queue in a background thread,
        #    get output from the queue in the GUI thread.
        #    Output chain: process.readline -> queue -> label)
        q = Queue(maxsize=1024)  # limit output buffering (may stall subprocess)
        t = Thread(target=self.reader_thread, args=[q])
        t.daemon = True # close pipe if GUI process exits
        t.start()

        # show subprocess' stdout in GUI
        self.label = tk.Label(root, text="  ", font=(None, 15))
        self.label.pack(ipadx=4, padx=4, ipady=4, pady=4, fill='both')
        self.update(q) # start update loop

    def reader_thread(self, q):
        """Read subprocess output and put it into the queue."""
        try:
            with self.process.stdout as pipe:
                for line in iter(pipe.readline, b''):
                    q.put(line)
        finally:
            q.put(None)

    def update(self, q):
        """Update GUI with items from the queue."""
        for line in iter_except(q.get_nowait, Empty): # display all content
            if line is None:
                self.quit()
                return
            else:
                self.label['text'] = line # update GUI
                break # display no more than one line per 40 milliseconds
        self.root.after(40, self.update, q) # schedule next update

    def quit(self):
        self.process.kill() # exit subprocess if GUI is closed (zombie!)
        self.root.destroy()
        
################################### Main Code #########################################################


# List of Channel in this order (asianetnews,manorama,news24,mathrubhumi,kairali,mediaone,NDTV News,CNN Live,Parumala,Reporter,news18,jeevan,janam)
Links=[];


def loadLinks():
    with open("links.txt") as file:
        lines = file.readlines()
        last = lines[-1]
        Links.clear()
        for line in lines[:-1]:
            Links.append(line[:-1])
        Links.append(last[:-1])
loadLinks();

def highlight(widget): #use to indicate button press 
    widget.bg = "lightblue"

def lowlight(widget): #use to indicate button press 
    widget.bg = "white"

def search_yt_query():
    url = "https://www.youtube.com/results?search_query={}".format(search_query_box.value)    
    webbrowser.open(url)
    search_query_box.clear()
     
def load_channel_asianet():
    #os.system('streamlink =vlc  https://www.youtube.com/watch?v=iL53Y28Rp84 240p &')
    subprocess.call('streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[0]), shell=True)
def load_channel_manorama():
    subprocess.call('streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[1]), shell=True)
def load_channel_24news():
    subprocess.call('streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[2]), shell=True)
def load_channel_mathrubhumi():
    subprocess.call('streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[3]), shell=True)
def load_channel_kairali():
    subprocess.call('streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[4]), shell=True)
def load_channel_mediaone():
    subprocess.call('streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[5]), shell=True)
def load_channel_ndtv():
    subprocess.call('streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[6]), shell=True)
def load_channel_cnn():
    subprocess.call('streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[7]), shell=True)
def load_channel_parumala():
    subprocess.call('streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[8]), shell=True)
def load_channel_reporter():
    subprocess.call('streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[9]), shell=True)
def load_channel_news18():
    subprocess.call('streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[10]), shell=True)
def load_channel_jeevan():
    subprocess.call('streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[11]), shell=True)
def load_channel_janam():
    subprocess.call('streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[12]), shell=True)
def get_ip():
    gw = os.popen("ip -4 route show default").read().split()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gw[2], 0))
    ipaddr = s.getsockname()[0]
    ipdisplay.value = ipaddr

def launch_kodi():
    subprocess.call('kodi', shell=True)


def stop_video():
    subprocess.call('sudo killall vlc', shell=True)
    

def stop_all():
    subprocess.call('sudo pkill chromium-browse', shell=True)
    

def update_firmware():
    root = tk.Tk()
    app = DisplaySubprocessOutputDemo(root,'sudo ./auto-update.sh')
    root.protocol("WM_DELETE_WINDOW", app.quit)
    # center window
    root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
    #root.mainloop()
    #subprocess.call('sudo ./auto-update.sh', shell=True)


def run_clean():
    #add more cleaning functions
    subprocess.call('sudo apt-get -y autoremove ', shell=True)
    m = subprocess.call('sudo apt-get -y autoclean', shell=True)
    label = Label(app, text = m)
    #this creates a new label to the GUI
    label.pack() 
    
def printSomething():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label = Label(app, text = m)
    #this creates a new label to the GUI
    label.pack() 

   


def refresh_links():
    # run updatelink python
    subprocess.call('sudo python update_channel.py',shell=True)
    loadLinks()
    
def launch_hotstar():
    # run www.hotsar.com popular movies
    subprocess.call('chromium-browser https://www.hotstar.com/in/movies/languages/malayalam', shell=True)

app = App(title="TV GUI",width=1920, height=1050)

title_box = Box(app, width="fill", align="top", border=True)
Text(title_box, text="Rpi TV Menu",size=20,font="Lato",color="black", align="top")
Text(title_box, text="          ",size=20,font="Lato",color="black", align="top")


channel_box = Box(app, width="fill",layout="grid", align="top", border=False)
channel_box.bg="#ffcc80"

button1 = PushButton(channel_box, command=load_channel_asianet, text="Asianet News", grid=[0,0],width=27, height=5)
button1.text_size=19
button1.when_mouse_enters = highlight
button1.when_mouse_leaves = lowlight
button = PushButton(channel_box, command=load_channel_manorama, text="Manorama News",grid=[1,0],width=27, height=5)
button.text_size=19
button = PushButton(channel_box, command=load_channel_24news, text="24 News",grid=[2,0],width=27, height=5)
button.text_size=19
button = PushButton(channel_box, command=load_channel_mathrubhumi, text="Mathrubhumi News",grid=[3,0],width=27, height=5)
button.text_size=19
button = PushButton(channel_box, command=load_channel_kairali, text="Kairali News",grid=[0,1],width=27, height=5)
button.text_size=19
button = PushButton(channel_box, command=load_channel_mediaone, text="Media One",grid=[1,1],width=27, height=5)
button.text_size=19
button = PushButton(channel_box, command=load_channel_ndtv, text="NDTV Live",grid=[2,1],width=27, height=5)
button.text_size=19
button = PushButton(channel_box, command=load_channel_cnn, text="CNN Live",grid=[3,1],width=27, height=5)
button.text_size=19
button = PushButton(channel_box, command=load_channel_parumala, text="Parumala Live",grid=[0,2],width=27, height=5)
button.text_size=19
button = PushButton(channel_box, command=load_channel_reporter, text="Reporter TV",grid=[1,2],width=27, height=5)
button.text_size=19
button = PushButton(channel_box, command=load_channel_news18, text="News 18",grid=[2,2],width=27, height=5)
button.text_size=19
button = PushButton(channel_box, command=load_channel_jeevan, text="Jeevan TV",grid=[3,2],width=27, height=5)
button.text_size=19


youtube_box = Box(app, width="fill", align="top", border=False)
youtube_box.bg="#ff5f4e"
search_query_box = TextBox(youtube_box, width ="fill",align="left",multiline=False)
search_query_box.text_size = 30
search_query_box.bg = "#dfe6e9"
search_button = PushButton(youtube_box, command=search_yt_query, text="Search YouTube", align="right",width=30, height=3)
search_button.text_size = 19
search_button.text_color="white"


ip_box = Box(app, width="fill", align="top", border=True)
ip_button = PushButton(ip_box, command=get_ip, text="Get IP Address",width=57, align="left")
ip_button.text_size=15
ipdisplay = Text(ip_box, text="  ",size=20,font="Lato",color="blue")


buttons_box = Box(app, width="fill",layout="grid", align="top", border=False)
buttons_box.bg="#80b3ff"
button = PushButton(buttons_box, command=launch_kodi, text="Launch KODI", grid=[0,0],width=27, height=1)
button.text_size=20
button = PushButton(buttons_box, command=stop_video, text="Stop Video",grid=[1,0],width=27, height=1)
button.text_size=20
button = PushButton(buttons_box, command=stop_all, text="Stop all",grid=[2,0],width=27, height=1)
button.text_size=20
button = PushButton(buttons_box, command=update_firmware, text="Run Update",grid=[3,0],width=27, height=1)
button.text_size=20
button = PushButton(buttons_box, command=run_clean, text="Run Cleanup",grid=[0,1],width=27, height=1)
button.text_size=20
button = PushButton(buttons_box, command=refresh_links, text="Refresh Links",grid=[1,1],width=27, height=1)
button.text_size=20
button = PushButton(buttons_box, command=launch_hotstar, text="Hotstar Movies",grid=[2,1],width=27, height=1)
button.text_size=20
button = PushButton(buttons_box, command=load_channel_parumala, text="Button",grid=[3,1],width=27, height=1)
button.text_size=19
button = PushButton(buttons_box, command=load_channel_reporter, text="Button",grid=[0,2],width=27, height=1)
button.text_size=19
button = PushButton(buttons_box, command=load_channel_news18, text="Button",grid=[1,2],width=27, height=1)
button.text_size=19
button = PushButton(buttons_box, command=load_channel_jeevan, text="Button",grid=[2,2],width=27, height=1)
button.text_size=19
button = PushButton(buttons_box, command=load_channel_ndtv, text="Button",grid=[3,2],width=27, height=1)
button.text_size=19


# buttons_box = Box(app, width="fill", align="bottom", border=True)
# Text(buttons_box, text="buttons")
# 
#options_box = Box(app, height="fill", align="right", border=True)
#Text(options_box, text="options")
# 
# content_box = Box(app, align="top", width="fill", border=True)
# Text(content_box, text="content")
# 
# form_box = Box(content_box, layout="grid", width="fill", align="left", border=True)
# Text(form_box, grid=[0,0], text="form", align="right")
# Text(form_box, grid=[0,1], text="label", align="left")
# TextBox(form_box, grid=[1,1], text="data", width="fill")
# 
# welcome_message = Text(app, text="Rpi TV Menu",size=20,font="Lato",color="black",grid=[2,0], align="center")
# 

# #Text(channel_box, text="Select Channel",size=20,font="Lato",color="black", align="left")
#channel_choice = Combo(channel_box, options=["None","Asianet", "Manorama", "26 News", "Mathurbhumi", "Kairali", "Media One", "Parumala Live", "Amrita"], align="left")

# 
# vip_seat = CheckBox(app, text="VIP seat?", grid=[1,4], align="left")
# 
# 
# 
# 
# text_size = Slider(app, command=change_text_size, start=10, end=50)
# pic_youtube = Picture(app, image="youtube.gif")


app.display()



#app = DisplaySubprocessOutputDemo(root,'sudo apt-get autoremove -y')
#root.protocol("WM_DELETE_WINDOW", app.quit)
# center window
#root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
#root.mainloop()
