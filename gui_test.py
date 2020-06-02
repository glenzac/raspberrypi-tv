#import time  #required for sleep 
import socket #required for getting IP Address
import os  #required to get IP Address
import subprocess  #required to run shell commands
import webbrowser
from guizero import App, Text, TextBox, PushButton, Slider, Picture, Combo, CheckBox, Box


def highlight(widget): #use to indicate button press 
    widget.bg = "lightblue"

def lowlight(widget):
    widget.bg = "white"

def search_yt_query():
    url = "https://www.youtube.com/results?search_query={}".format(search_query_box.value)    
    webbrowser.open(url)
 

def change_text_size(slider_value):
    welcome_message.size = slider_value
    
def load_channel():
    welcome_message.value = my_name.value
    
def load_channel_asianet():
    #os.system('streamlink --player=vlc  https://www.youtube.com/watch?v=iL53Y28Rp84 240p &')
    subprocess.call('streamlink --player "vlc --file-caching=5000 --network-caching=5000" https://www.youtube.com/watch?v=iL53Y28Rp84 240p &', shell=True)
def load_channel_manorama():
    subprocess.call('streamlink --player "vlc --file-caching=5000 --network-caching=5000" https://www.youtube.com/watch?v=jjH6v95z3Nw 240p &', shell=True)
def load_channel_24news():
    subprocess.call('streamlink --player "vlc --file-caching=5000 --network-caching=5000" https://www.youtube.com/watch?v=zcrUCvBD16k 240p &', shell=True)
def load_channel_mathrubhumi():
    subprocess.call('streamlink --player "vlc --file-caching=5000 --network-caching=5000" https://www.youtube.com/watch?v=irF-4N_fHjs 240p &', shell=True)
def load_channel_kairali():
    subprocess.call('streamlink --player "vlc --file-caching=5000 --network-caching=5000" https://www.youtube.com/watch?v=ET5Y3H3Jusc 240p &', shell=True)
def load_channel_mediaone():
    subprocess.call('streamlink --player "vlc --file-caching=5000 --network-caching=5000" https://www.youtube.com/watch?v=d1iwUB9YFnA 240p &', shell=True)
def load_channel_amrita():
    subprocess.call('streamlink --player "vlc --file-caching=5000 --network-caching=5000" https://www.youtube.com/watch?v=iL53Y28Rp84 240p &', shell=True)
def load_channel_parumala():
    subprocess.call('streamlink --player "vlc --file-caching=5000 --network-caching=5000" https://www.youtube.com/watch?v=hjAj_rcbQDU 240p &', shell=True)
def load_channel_reporter():
    subprocess.call('streamlink --player "vlc --file-caching=5000 --network-caching=5000" https://www.youtube.com/watch?v=Qx-f55XBPG4 240p &', shell=True)
def load_channel_news18():
    subprocess.call('streamlink --player "vlc --file-caching=5000 --network-caching=5000" https://www.youtube.com/watch?v=lm-dkwdTDLE 240p &', shell=True)
def load_channel_jeevan():
    subprocess.call('streamlink --player "vlc --file-caching=5000 --network-caching=5000" https://www.youtube.com/watch?v=25Gr0Q2oyuc 240p &', shell=True)
def load_channel_janam():
    subprocess.call('streamlink --player "vlc --file-caching=5000 --network-caching=5000" https://www.youtube.com/watch?v=_WK30gnY3_4 240p &', shell=True)
def load_channel_ndtv():
    subprocess.call('streamlink --player "vlc --file-caching=5000 --network-caching=5000" https://www.youtube.com/watch?v=l9ViElip9q4 240p &', shell=True)
    
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
    subprocess.call('sudo ./auto-update.sh', shell=True)


def run_clean():
    #add more cleaning functions
    subprocess.call('sudo apt autoremove', shell=True)
    subprocess.call('sudo apt autoclean', shell=True)


def refresh_links():
    welcome_message.value = my_name.value

app = App(title="TV GUI",width=1920, height=1080)

title_box = Box(app, width="fill", align="top", border=True)
Text(title_box, text="Rpi TV Menu",size=20,font="Lato",color="black", align="top")
Text(title_box, text="          ",size=20,font="Lato",color="black", align="top")


channel_box = Box(app, width="fill",layout="grid", align="top", border=False)
channel_box.bg="#ffcc80"

button1 = PushButton(channel_box, command=load_channel_asianet, text="Asianet News", grid=[0,0],width=27, height=5)
button1.text_size=20
button1.when_mouse_enters = highlight
button1.when_mouse_leaves = lowlight
button = PushButton(channel_box, command=load_channel_manorama, text="Manorama News",grid=[1,0],width=27, height=5)
button.text_size=20
button = PushButton(channel_box, command=load_channel_24news, text="24 News",grid=[2,0],width=27, height=5)
button.text_size=20
button = PushButton(channel_box, command=load_channel_mathrubhumi, text="Mathrubhumi News",grid=[3,0],width=27, height=5)
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

youtube_box = Box(app, width="fill", align="top", border=False)
youtube_box.bg="#ff5f4e"
search_query_box = TextBox(youtube_box, width ="fill",align="left",multiline=False)
search_query_box.text_size = 30
search_query_box.bg = "#dfe6e9"
search_button = PushButton(youtube_box, command=search_yt_query, text="Search YouTube", align="right",width=30, height=3)
search_button.text_size = 20
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
