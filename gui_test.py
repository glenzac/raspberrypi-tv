#!/usr/bin/python
from tkinter import *
#import time  #required for sleep 
import socket #required for getting IP Address
import os  #required to get IP Address
import subprocess  #required to run shell commands
import webbrowser #required to open Chromium

from guizero import App, Text, TextBox, PushButton, Box

####################### To display the output of shell commands as a window #####################
####################### Credits : https://stackoverflow.com/a/32682520      #####################


"""
- read output from a subprocess in a background thread
- show the output in the GUI
"""
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
        self.label = tk.Label(root, text="  ", font=(None, 20))
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

Links=[];

def loadLinks(): # used to load the live video IDs from the links.txt file to an array
    with open("/home/pi/GUI/links.txt") as file:
        lines = file.readlines()
        last = lines[-1]
        Links.clear()
        for line in lines[:-1]:
            Links.append(line[:-1])
        Links.append(last[:-1])
loadLinks();

def highlight1(event_data): #change channel button colour when_clicked
    event_data.widget.bg = "#bdc3c7"

def lowlight1(event_data): #change channel button colour when_mouse_leaves
    event_data.widget.bg = "#ecf0f1"

def highlight2(event_data): #change button colour when_clicked
    event_data.widget.bg = "#27ae60"

def lowlight2(event_data): #change channel button colour when_mouse_leaves
    event_data.widget.bg = "#3498db"

def search_yt_query(): # Run YouTube search based on a query 
    url = "https://www.youtube.com/results?search_query={}".format(search_query_box.value)    
    webbrowser.open(url)
    search_query_box.clear()

### -------------------------------- channel defintions -------------------------------------------###
     
def load_channel_asianet(): # function that opens required channel live links
    root = tk.Tk()
    root.geometry('1920x80+0+850')
    root.title('Running Process')
    app = DisplaySubprocessOutputDemo(root,'streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[0]))
    root.protocol("WM_DELETE_WINDOW", app.quit)


def load_channel_manorama(): # function that opens required channel live links
    root = tk.Tk()
    root.geometry('1920x80+0+850') 
    root.title('Running Process')
    app = DisplaySubprocessOutputDemo(root,'streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[1]))
    root.protocol("WM_DELETE_WINDOW", app.quit)


def load_channel_24news(): # function that opens required channel live links
    root = tk.Tk()
    root.geometry('1920x80+0+850') 
    root.title('Running Process')
    app = DisplaySubprocessOutputDemo(root,'streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[2]))
    root.protocol("WM_DELETE_WINDOW", app.quit)


def load_channel_mathrubhumi(): # function that opens required channel live links
    root = tk.Tk()
    root.geometry('1920x80+0+850') 
    root.title('Running Process')
    app = DisplaySubprocessOutputDemo(root,'streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[3]))
    root.protocol("WM_DELETE_WINDOW", app.quit)


def load_channel_kairali(): # function that opens required channel live links
    root = tk.Tk()
    root.geometry('1920x80+0+850') 
    root.title('Running Process')
    app = DisplaySubprocessOutputDemo(root,'streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[4]))
    root.protocol("WM_DELETE_WINDOW", app.quit)


def load_channel_mediaone(): # function that opens required channel live links
    root = tk.Tk()
    root.geometry('1920x80+0+850') 
    root.title('Running Process')
    app = DisplaySubprocessOutputDemo(root,'streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[5]))
    root.protocol("WM_DELETE_WINDOW", app.quit)


def load_channel_ndtv(): # function that opens required channel live links
    root = tk.Tk()
    root.geometry('1920x80+0+850') 
    root.title('Running Process')
    app = DisplaySubprocessOutputDemo(root,'streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[6]))
    root.protocol("WM_DELETE_WINDOW", app.quit)


def load_channel_cnn(): # function that opens required channel live links
    root = tk.Tk()
    root.geometry('1920x80+0+850') 
    root.title('Running Process')
    app = DisplaySubprocessOutputDemo(root,'streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[7]))
    root.protocol("WM_DELETE_WINDOW", app.quit)


def load_channel_parumala(): # function that opens required channel live links
    root = tk.Tk()
    root.geometry('1920x80+0+850') 
    root.title('Running Process')
    app = DisplaySubprocessOutputDemo(root,'streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[8]))
    root.protocol("WM_DELETE_WINDOW", app.quit)


def load_channel_reporter(): # function that opens required channel live links
    root = tk.Tk()
    root.geometry('1920x80+0+850') 
    root.title('Running Process')
    app = DisplaySubprocessOutputDemo(root,'streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[9]))
    root.protocol("WM_DELETE_WINDOW", app.quit)


def load_channel_news18(): # function that opens required channel live links
    root = tk.Tk()
    root.geometry('1920x80+0+850') 
    root.title('Running Process')
    app = DisplaySubprocessOutputDemo(root,'streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[10]))
    root.protocol("WM_DELETE_WINDOW", app.quit)


def load_channel_jeevan(): # function that opens required channel live links
    root = tk.Tk()
    root.geometry('1920x80+0+850') 
    root.title('Running Process')
    app = DisplaySubprocessOutputDemo(root,'streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[11]))
    root.protocol("WM_DELETE_WINDOW", app.quit)


def load_channel_janam(): # function that opens required channel live links
    root = tk.Tk()
    root.geometry('1920x80+0+850') 
    root.title('Running Process')
    app = DisplaySubprocessOutputDemo(root,'streamlink https://www.youtube.com/watch?v={} 240p &'.format(Links[12]))
    root.protocol("WM_DELETE_WINDOW", app.quit)


### -------------------------------------------------------------------------------------------------------###


def get_ip(): # Fetches the local IP Address of the Rpi
    gw = os.popen("ip -4 route show default").read().split()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gw[2], 0))
    ipaddr = s.getsockname()[0]
    ipdisplay.value = ipaddr

def launch_kodi(): # Launch KODI
    subprocess.call('kodi', shell=True)

def stop_video(): # Stop all video playback in vlc 
    subprocess.call('sudo killall vlc', shell=True)
    
def stop_all(): # Kill the browser 
    subprocess.call('sudo pkill chromium-browse', shell=True)
    
def update_firmware(): #  Runs a script that updates the Rpi
    root = tk.Tk()
    root.geometry('1920x80+0+850') 
    root.title('Running Process')
    app = DisplaySubprocessOutputDemo(root,'sudo /home/pi/GUI/auto-update.sh')
    root.protocol("WM_DELETE_WINDOW", app.quit)

def refresh_links(): # Runs a script that fetches links to live YouTube video
    root = tk.Tk()
    root.geometry('1920x80+0+850') 
    root.title('Running Process')
    app = DisplaySubprocessOutputDemo(root,'sudo python3 /home/pi/GUI/update_channel.py')
    loadLinks()
    root.protocol("WM_DELETE_WINDOW", app.quit)
    
def launch_hotstar(): # run www.hotsar.com popular movies on Chromium
    subprocess.call('chromium-browser https://www.hotstar.com/in/movies/languages/malayalam', shell=True)


### -------------------------------------  Main GUI interface ---------------------------------------- ###

app = App(title="TV GUI",width=1920, height=1050) # not full HD dimensions to give space to the taskbar 

# Contains the buttons for the different channels
channel_box = Box(app, width="fill",layout="grid", align="top", border=False)
channel_box.bg="#ecf0f1"
# Defining the channel buttons
button1 = PushButton(channel_box, command=load_channel_asianet, text="Asianet News", grid=[0,0],width=27, height=5)
button1.text_size=19
button1.when_clicked = highlight1
button1.when_mouse_leaves = lowlight1
button2 = PushButton(channel_box, command=load_channel_manorama, text="Manorama News",grid=[1,0],width=27, height=5)
button2.text_size=19
button2.when_clicked = highlight1
button2.when_mouse_leaves = lowlight1
button3 = PushButton(channel_box, command=load_channel_24news, text="24 News",grid=[2,0],width=27, height=5)
button3.text_size=19
button3.when_clicked = highlight1
button3.when_mouse_leaves = lowlight1
button4 = PushButton(channel_box, command=load_channel_mathrubhumi, text="Mathrubhumi News",grid=[3,0],width=27, height=5)
button4.text_size=19
button4.when_clicked = highlight1
button4.when_mouse_leaves = lowlight1
button5 = PushButton(channel_box, command=load_channel_kairali, text="Kairali News",grid=[0,1],width=27, height=5)
button5.text_size=19
button5.when_clicked = highlight1
button5.when_mouse_leaves = lowlight1
button6 = PushButton(channel_box, command=load_channel_mediaone, text="Media One",grid=[1,1],width=27, height=5)
button6.text_size=19
button6.when_clicked = highlight1
button6.when_mouse_leaves = lowlight1
button7 = PushButton(channel_box, command=load_channel_ndtv, text="NDTV Live",grid=[2,1],width=27, height=5)
button7.text_size=19
button7.when_clicked = highlight1
button7.when_mouse_leaves = lowlight1
button8 = PushButton(channel_box, command=load_channel_cnn, text="CNN Live",grid=[3,1],width=27, height=5)
button8.text_size=19
button8.when_clicked = highlight1
button8.when_mouse_leaves = lowlight1
button9 = PushButton(channel_box, command=load_channel_parumala, text="Parumala Live",grid=[0,2],width=27, height=5)
button9.text_size=19
button9.when_clicked = highlight1
button9.when_mouse_leaves = lowlight1
button10 = PushButton(channel_box, command=load_channel_reporter, text="Reporter TV",grid=[1,2],width=27, height=5)
button10.text_size=19
button10.when_clicked = highlight1
button10.when_mouse_leaves = lowlight1
button11 = PushButton(channel_box, command=load_channel_news18, text="News 18",grid=[2,2],width=27, height=5)
button11.text_size=19
button11.when_clicked = highlight1
button11.when_mouse_leaves = lowlight1
button12 = PushButton(channel_box, command=load_channel_jeevan, text="Jeevan TV",grid=[3,2],width=27, height=5)
button12.text_size=19
button12.when_clicked = highlight1
button12.when_mouse_leaves = lowlight1

# Contains the button and Text area for printing IP address
ip_box = Box(app, width="fill", align="top", border=False)
ip_box.bg = "#34495e"
ip_box.text_color="white"
ip_button = PushButton(ip_box, command=get_ip, text="Get IP Address",width=30, align="right")
ip_button.text_size=15
ipdisplay = Text(ip_box, text="  ",size=20,font="Lato",color="white")

# Contains the button and TextBox for YouTube search based on entered query
youtube_box = Box(app, width="fill", align="top", border=False)
youtube_box.bg="#e74c3c"
search_query_box = TextBox(youtube_box, width ="fill",align="left",multiline=False)
search_query_box.text_size = 25
search_query_box.bg = "#dfe6e9"
search_button = PushButton(youtube_box, command=search_yt_query, text="Search YouTube", align="right",width=30, height=3)
search_button.text_size = 20
search_button.text_color="white"

# Contains the buttons for executing system functions
buttons_box = Box(app, width="fill",layout="grid", align="top", border=False)
buttons_box.bg="#3498db"
buttons_box.text_color="white"
button13 = PushButton(buttons_box, command=launch_kodi, text="Launch KODI", grid=[0,0],width=27, height=1)
button13.text_size=20
button13.when_clicked = highlight2
button13.when_mouse_leaves = lowlight2
button14 = PushButton(buttons_box, command=stop_video, text="Stop Video",grid=[1,0],width=27, height=1)
button14.text_size=20
button14.when_clicked = highlight2
button14.when_mouse_leaves = lowlight2
button15 = PushButton(buttons_box, command=stop_all, text="Stop all",grid=[2,0],width=27, height=1)
button15.text_size=20
button15.when_clicked = highlight2
button15.when_mouse_leaves = lowlight2
button16 = PushButton(buttons_box, command=update_firmware, text="Run Update",grid=[3,0],width=27, height=1)
button16.text_size=20
button16.when_clicked = highlight2
button16.when_mouse_leaves = lowlight2
button17 = PushButton(buttons_box, command=stop_all, text="Button",grid=[0,1],width=27, height=1)
button17.text_size=20
button17.when_clicked = highlight2
button17.when_mouse_leaves = lowlight2
button18 = PushButton(buttons_box, command=refresh_links, text="Refresh Links",grid=[1,1],width=27, height=1)
button18.text_size=20
button18.when_clicked = highlight2
button18.when_mouse_leaves = lowlight2
button19 = PushButton(buttons_box, command=launch_hotstar, text="Hotstar Movies",grid=[2,1],width=27, height=1)
button19.text_size=20
button19.when_clicked = highlight2
button19.when_mouse_leaves = lowlight2
button20 = PushButton(buttons_box, command=stop_all, text="Button",grid=[3,1],width=27, height=1)
button20.text_size=20
button20.when_clicked = highlight2
button20.when_mouse_leaves = lowlight2

#extra buttons left for future upgrades
#button = PushButton(buttons_box, command=load_channel_reporter, text="Button",grid=[0,2],width=27, height=1)
#button.text_size=19
#button = PushButton(buttons_box, command=load_channel_news18, text="Button",grid=[1,2],width=27, height=1)
#button.text_size=19
#button = PushButton(buttons_box, command=load_channel_jeevan, text="Button",grid=[2,2],width=27, height=1)
#button.text_size=19
#button = PushButton(buttons_box, command=load_channel_ndtv, text="Button",grid=[3,2],width=27, height=1)
#button.text_size=19

app.display()
