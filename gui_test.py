import time
import socket
import os
from guizero import App, Text, TextBox, PushButton, Slider, Picture, Combo, CheckBox, Box

def highlight(widget):
    widget.bg = "lightblue"

def lowlight(widget):
    bg.widget = "white"

def search_yt_query():
    welcome_message.value = my_name.value

def change_text_size(slider_value):
    welcome_message.size = slider_value
    
def load_channel():
    welcome_message.value = my_name.value
    
def load_channel_asianet():
    os.system('streamlink --player=vlc  https://www.youtube.com/watch?v=iL53Y28Rp84 240p &')
def load_channel_manorama():
    welcome_message.value = my_name.value
def load_channel_24news():
    welcome_message.value = my_name.value
def load_channel_mathurbhumi():
    welcome_message.value = my_name.value
def load_channel_kairali():
    welcome_message.value = my_name.value
def load_channel_mediaone():
    welcome_message.value = my_name.value
def load_channel_amrita():
    welcome_message.value = my_name.value
def load_channel_parumala():
    welcome_message.value = my_name.value
def load_channel_reporter():
    welcome_message.value = my_name.value
def load_channel_news18():
    welcome_message.value = my_name.value
def load_channel_jeevan():
    welcome_message.value = my_name.value
def load_channel_janam():
    welcome_message.value = my_name.value
def load_channel_ndtv():
    welcome_message.value = my_name.value
    
def get_ip():
    gw = os.popen("ip -4 route show default").read().split()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gw[2], 0))
    ipaddr = s.getsockname()[0]
    ipdisplay.value = ipaddr

def launch_kodi():
    welcome_message.value = my_name.value


def stop_video():
    welcome_message.value = my_name.value
    

def stop_all():
    welcome_message.value = my_name.value
    

def update_firmware():
    welcome_message.value = my_name.value


def run_clean():
    welcome_message.value = my_name.value


def refresh_links():
    welcome_message.value = my_name.value

app = App(title="TV GUI",width=1920, height=1080)



title_box = Box(app, width="fill", align="top", border=True)
Text(title_box, text="Rpi TV Menu",size=20,font="Lato",color="black", align="top")
Text(title_box, text="          ",size=20,font="Lato",color="black", align="top")

youtube_box = Box(app, width="fill", align="top", border=True)
search_query_box = TextBox(youtube_box, width ="fill",align="left",multiline=False, height=3)
search_query_box.text_size = 30
search_button = PushButton(youtube_box, command=search_yt_query, text="Search YouTube", align="right",width=30, height=3)
search_button.text_size = 20

channel_box = Box(app, width="fill",layout="grid", align="top", border=False)
channel_box.bg="white"


button1 = PushButton(channel_box, command=load_channel_asianet, text="Asianet News", grid=[0,0],width=27, height=5)
button1.text_size=20
button1.when_mouse_enters = highlight
button1.when_mouse_leaves = lowlight
button = PushButton(channel_box, command=load_channel_manorama, text="Manorama News",grid=[1,0],width=27, height=5)
button.text_size=20
button = PushButton(channel_box, command=load_channel_24news, text="24 News",grid=[2,0],width=27, height=5)
button.text_size=20
button = PushButton(channel_box, command=load_channel_mathurbhumi, text="Mathurbhumi News",grid=[3,0],width=27, height=5)
button.text_size=20
button = PushButton(channel_box, command=load_channel_kairali, text="Kairali News",grid=[0,1],width=27, height=5)
button.text_size=20
button = PushButton(channel_box, command=load_channel_mediaone, text="Media One",grid=[1,1],width=27, height=5)
button.text_size=20
button = PushButton(channel_box, command=load_channel_amrita, text="Amrita TV",grid=[2,1],width=27, height=5)
button.text_size=20
button = PushButton(channel_box, command=load_channel_parumala, text="Parumala Live",grid=[3,1],width=27, height=5)
button.text_size=20
button = PushButton(channel_box, command=load_channel_reporter, text="Reporter TV",grid=[0,2],width=27, height=5)
button.text_size=20
button = PushButton(channel_box, command=load_channel_news18, text="News 18",grid=[1,2],width=27, height=5)
button.text_size=20
button = PushButton(channel_box, command=load_channel_jeevan, text="Jeevan TV",grid=[2,2],width=27, height=5)
button.text_size=20
button = PushButton(channel_box, command=load_channel_ndtv, text="NDTV Live",grid=[3,2],width=27, height=5)
button.text_size=20

ip_box = Box(app, width="fill", align="top", border=True)
ip_button = PushButton(ip_box, command=get_ip, text="Get IP Address",width=57, align="left")
ip_button.text_size=15
ipdisplay = Text(ip_box, text="  ",size=20,font="Lato",color="blue")


buttons_box = Box(app, width="fill",layout="grid", align="top", border=False)
buttons_box.bg="blue"
button = PushButton(buttons_box, command=launch_kodi, text="Launch KODI", grid=[0,0],width=27, height=1)
button.text_size=20
button = PushButton(buttons_box, command=stop_video, text="Stop Video",grid=[1,0],width=27, height=1)
button.text_size=20
button = PushButton(buttons_box, command=stop_all, text="Stop all??",grid=[2,0],width=27, height=1)
button.text_size=20
button = PushButton(buttons_box, command=update_firmware, text="Run Update",grid=[3,0],width=27, height=1)
button.text_size=20
button = PushButton(buttons_box, command=run_clean, text="Run Cleanup",grid=[0,1],width=27, height=1)
button.text_size=20
button = PushButton(buttons_box, command=refresh_links, text="Refresh Links",grid=[1,1],width=27, height=1)
button.text_size=20
button = PushButton(buttons_box, command=load_channel_amrita, text="Amrita TV",grid=[2,1],width=27, height=1)
button.text_size=20
button = PushButton(buttons_box, command=load_channel_parumala, text="Parumala Live",grid=[3,1],width=27, height=1)
button.text_size=20
button = PushButton(buttons_box, command=load_channel_reporter, text="Reporter TV",grid=[0,2],width=27, height=1)
button.text_size=20
button = PushButton(buttons_box, command=load_channel_news18, text="News 18",grid=[1,2],width=27, height=1)
button.text_size=20
button = PushButton(buttons_box, command=load_channel_jeevan, text="Jeevan TV",grid=[2,2],width=27, height=1)
button.text_size=20
button = PushButton(buttons_box, command=load_channel_ndtv, text="NDTV Live",grid=[3,2],width=27, height=1)
button.text_size=20


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
#channel_choice = Combo(channel_box, options=["None","Asianet", "Manorama", "24 News", "Mathurbhumi", "Kairali", "Media One", "Parumala Live", "Amrita"], align="left")

# 
# vip_seat = CheckBox(app, text="VIP seat?", grid=[1,4], align="left")
# 
# 
# 
# 
# text_size = Slider(app, command=change_text_size, start=10, end=50)
# pic_youtube = Picture(app, image="youtube.gif")


app.display()








#to update firmware
#sudo apt clean
#sudo apt update
#sudo apt full-upgrade
