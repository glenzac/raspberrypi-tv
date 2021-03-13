# YouTube TV using the Raspberry Pi on Raspberry Pi OS with HDMI-CEC

**This is my attempt at creating a YouTube Media device using the Raspberry pi running the Raspberry Pi OS and a simple Python based GUI - in short it is a very crude implementation of the bare minimum features**

Chromium browser came pre-installed and YouTube videos worked fine in it. Though, I don’t think it’s **not** going to throw up heating issues once continuous HD playback happens. This is mostly because the in-browser process is not hardware accelerated by the GPU. Using external players is the best way to go about achieving hardware acceleration for YouTube videos. Most tutorials on the internet refer to using youtube-dl and omxplayer. [YouTube-dl](https://github.com/ytdl-org/youtube-dl) to extract the videofile’s link and [omxplayer](https://www.raspberrypi.org/documentation/raspbian/applications/omxplayer.md) is the inbuilt commandline video player in Raspberry Pi OS. I tried all these. My issue was identical to the one someone posted on [reddit](https://www.reddit.com/r/raspberry_pi/comments/8jfl5n/how_do_i_play_a_youtube_live_stream_full_screen).

Streamplayer worked for me.
```bash
sudo apt install git python-setuptools
git clone https://github.com/streamlink/streamlink
cd streamlink/
sudo python3 setup.py install
```

I was able to play videos using omxplayer but I couldn’t turn it off without killing the script using the Ctrl-C or Alt-F4. The q button didn’t work. Several attempts to make it work failed and I ended up switching to the much user friendly VLC media player.

Streamlink uses VLC as the default player. Hence a separate player need not be specified with the `-p` parameter. Additionally you may use appropriate network and file caching to not see any buffering.
```	
streamlink --player "vlc --file-caching=5000 --network-caching=5000" https://www.youtube.com/watch?v={}
```

Once I had stream function set up, I wanted to control and select things on the Rpi using the TV’s remote. I found a recent [guide](https://pimylifeup.com/raspberrypi-hdmi-cec/) to setting up HDMI-CEC on Raspberry Pi OS using the cec-utils package.

Follow the installation given in the guide linked above to setup and verify your HDMI-CEC connection. 
A [user](https://ubuntu-mate.community/u/GizmoXomziG) on the Ubuntu-mate community had created an extensive script to control the Rpi using the TV remote. Here’s the link to the [post](https://ubuntu-mate.community/t/controlling-raspberry-pi-with-tv-remote-using-hdmi-cec/4250).

Do not install the cec-client again as we already installed the whole cec-utils package earlier.

Simply install just the [xdotools](http://manpages.ubuntu.com/manpages/trusty/man1/xdotool.1.html) for controlling the mouse and sending keystrokes on the Rpi :
`sudo apt-get install xdotool`

Follow rest of the guide to make the executable script and also check out the updated code found in one of the [replies](https://ubuntu-mate.community/t/controlling-raspberry-pi-with-tv-remote-using-hdmi-cec/4250/4) – try and check which one works fine. You need not have the exact same remote so you’ll have the change the code based on specific remote that you have.

I also followed another reply on the post to get a virtual onscreen keyboard.
1
	
sudo apt-get install xvkbd

To make it run at boot I tried using the [crontab](https://www.raspberrypi.org/documentation/linux/usage/cron.md) command and using [systemd](https://www.raspberrypi.org/documentation/linux/usage/systemd.md) both of it didn’t work properly. systemd was running the program too early in boot and waiting for `graphical.target` or `network.target` didn’t work. So in order to make it work after the desktop is loaded I did the following:

`sudo nano /etc/xdg/lxsession/LXDE-pi/autostart`

To the above file added the startup script as follows:

`@ sudo /home/pi/start.sh`

Make sure to specify the full path to the file and also convert the start.sh script into an executable using the following command:

`sudo chmod +x /home/pi/start.sh`

My `start.sh` script contains the scripts I want to run at startup. The custom remote code that I use for the SONY remote is also present in the repository.

## Recommendations for the Rpi
- change GPU allocation in [raspi-config](https://www.raspberrypi.org/documentation/configuration/raspi-config.md) to at least 128MB. I use 256MB for GPU.
- [change default python to python3](https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux) for best compatibility with streamlink when the command is executed as a script
- use the modern [subprocess](https://docs.python.org/3/library/subprocess.html#subprocess-replacements) module instead of os.system call to run bash scripts within python
- to wake a raspberry pi from the halt state (i.e after a shutdown with only the red light) simply connect a pushbutton in between board pins 5 and 6 on the pi. When the button is pressed the pin is shorted to ground and this triggers a boot on the Rpi
- Power cycling can also be achieved by shorting the onboard RUN pins on the RPI. Note that no connections are soldered onto the pins. If you need to use it you have to manually solder header pins to it.
- Also checkout this [one button halt and restart circuit](https://www.raspberrypi.org/forums/viewtopic.php?t=140994)
- Set up a watchdog on Rpi to reboot it whenever it freezes or crashes this way you don’t have to keep pulling the plug every time it crashes. I used the answer [here](https://raspberrypi.stackexchange.com/questions/99584/rpi-freezes-every-now-and-then-how-to-fix-it-with-a-watchdog). For my use-case I set the time to 20sec.
- add cooling fan — link to the post of power supply build 🔴🔴🔴
- Added following commands to /boot/cmdline.txt to turn off network boost mode `smsc95xx.turbo_mode=N`
- Run [Rpi diagnostics](https://www.raspberrypi.org/blog/sd-card-speed-test/) to check the speed of your SD card. I have a class 10 card but still it fared well in the speed test.

![Rpi diagnostics](https://github.com/glenzac/raspberrypi-tv/blob/master/rpi_diagnostics.jpg)

## Fetching YouTube live links and streams

The main purpose of this build is to watch live YouTube streams, especially news channels. The problem here is that different YouTube channels keep changing their live video links from time to time. Some channels change it after a couple of months. Some change it every few days. To not painstakingly find links each time we need to play something we need to use the YouTube API to fetch live links.

- First get the [channel ID](https://stackoverflow.com/questions/14366648/how-can-i-get-a-channel-id-from-youtube)
- Use YouTube API calls to [fetch links to the live](https://stackoverflow.com/questions/37521853/how-to-get-youtube-live-stream-by-channel-id-in-youtube-api-v3-in-android) playback 

Here is the python program to fetch links automatically and save it to a file `links.txt` This needs your Google YouTube API key in the `api-key.txt` file in the same location. Also find the channel IDs manually as a one time process and add it to the list. Then this python code automatically fetches links to live streams:

```python
import requests
 
# List of Channel ID (asianetnews,manorama,news24,mathrubhumi,kairali,mediaone,NDTV News,CNN Live,Parumala,Reporter,news18,jeevan,janam)
CHANNEL_ID = ["UCf8w5m0YsRa8MHQ5bwSGmbw","UCP0uG-mcMImgKnJz-VjJZmQ","UCup3etEdjyF1L3sRbU-rKLw","UCwXrBBZnIh2ER4lal6WbAHw","UCkCWitaToNG1_lR-Si1oMrg","UC-f7r46JhYv78q5pGrO6ivA","UCZFMm1mMw0F81Z37aaEzTUA","UCef1-8eOpJgud7szVPlZQAQ","UC8ebJ_anG4byfhC_2hT7eKw","UCFx1nseXKTc1Culiu3neeSQ","UC-mMi78WJST4N5o8_i1FoXw","UCjX2Z1XGWEbKEGgKMACbhkw","UCNVkxRPqsBNejO6B9thG9Xw"]

# Fetching the API Key
file = open("api-key.txt", "r")
YOUR_API_KEY = file.readline()
file.close()
 
#Defined empty Links array
Links=[];
 
# For each Channel Id, updating the channel Links 
for channel in CHANNEL_ID:
    URL = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={}&eventType=live&type=video&key={}".format(channel,YOUR_API_KEY);
    req = requests.get(url = URL);
    data = req.json()
    try:
        link = data['items'][0]['snippet']['thumbnails']['default']['url'].split("/")[4];
        print(link)
    except:
        print("Link Not Found")
        link="404"
    finally:
        Links.append(link)
 
#Links File opened to write
file2 = open(r"links.txt","w+")
for link in Links:
    file2.write(link+"\n")
file2.close()
```


Creating a custom GUI for the raspberry pi

I looked at all the options available for creating a GUI in python on a Rpi. Here are the best ones I found
- Tkinter (standard GUI application for Python)
- guizero (simple GUI library based on Tkinter)
- kivy
- remi
- GTK+
- PyQT

I chose guizero as it appeared to be very simple to implement and had good beginner friendly documentation.

The GUI looks as shown here:

Ignore the channel names, they are just YouTube live channels in my local language.

![GUI](https://github.com/glenzac/raspberrypi-tv/blob/master/gui_rpi.png)

The blank grey portion at the bottom displays the terminal output when buttons are pressed. Only the current line of the terminal output appears in the space.
The python code for the custom GUI can be found in the repository.



### ⚠️ Note:
I do not find the Raspberry Pi to be 100% **reliable**. It’s hard to make such systems perfect. To make it totally foolproof one has to mount the drive as read-only and re-write all the code in such a way that all the temporary data is fetched at startup and stored into the RAM. Doing this will ensure that you don’t corrupt your boot files when somebody simply pulls the cord off the pi without shutting it down.

After about 1.5 months of good use, it so happened that the pi boot partition got corrupt after a dirty shutdown. By then I didn’t have much time to spend on configuring this all over again. I just bought a new streaming device. But overall it has been a great learning experience. I got to push the pi to its limits. 
