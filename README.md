# raspberrypi-tv

Chromium browser came pre-installed and YouTube videos worked fine in it. Though, I don’t think it’s not going to throw up heating issues once continuous HD playback happens. This is mostly because the in-browser process is not hardware accelerated by the GPU. Using external players is the best way to go about achieving hardware acceleration for YouTube videos. Most tutorials on the internet refer to using youtube-dl and omxplayer. [YouTube-dl](https://github.com/ytdl-org/youtube-dl) to extract the videofile’s link and [omxplayer](https://www.raspberrypi.org/documentation/raspbian/applications/omxplayer.md) is the inbuilt commandline video player in Raspberry Pi OS. I tried all these. My issue was identical to the one someone posted on [reddit](https://www.reddit.com/r/raspberry_pi/comments/8jfl5n/how_do_i_play_a_youtube_live_stream_full_screen).

Streamplayer worked for me.
```
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

My `start.sh` script contains the scripts I want to run at startup. The custom remote code that I use for the SONY remote. 
