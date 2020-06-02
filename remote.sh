#!/bin/bash


#   Exports GPIO pin to userspace
echo "21" > /sys/class/gpio/export                  

# Sets pin 21 as an output
echo "out" > /sys/class/gpio/gpio21/direction

# Sets pin 21 to high
echo "0" > /sys/class/gpio/gpio21/value

# Sets pin 18 to low
#echo "0" > /sys/class/gpio/gpio18/value 


function keychar {
    parin1=$1 #first param; abc1
    parin2=$2 #second param; 0=a, 1=b, 2=c, 3=1, 4=a, ...
    parin2=$((parin2)) #convert to numeric
    parin1len=${#parin1} #length of parin1
    parin2pos=$((parin2 % parin1len)) #position mod
    char=${parin1:parin2pos:1} #char key to simulate
    if [ "$parin2" -gt 0 ]; then #if same key pressed multiple times, delete previous char; write a, delete a write b, delete b write c, ...
        xdotool key "BackSpace"
    fi
    #special cases for xdotool ( X Keysyms )
    if [ "$char" = " " ]; then char="space"; fi
    if [ "$char" = "." ]; then char="period"; fi
    if [ "$char" = "-" ]; then char="minus"; fi
    xdotool key $char
}
datlastkey=$(date +%s%N)
strlastkey=""
strlastid=""
intkeychar=0
intmsbetweenkeys=2000 #two presses of a key sooner that this makes it delete previous key and write the next one (a->b->c->1->a->...)
intmousestartspeed=15 #mouse starts moving at this speed (pixels per key press)
intmouseacc=15 #added to the mouse speed for each key press (while holding down key, more key presses are sent from the remote)
intmousespeed=15

#   Exports GPIO pin to userspace
echo "20" > /sys/class/gpio/export                  

# Sets pin 20 as an output
echo "out" > /sys/class/gpio/gpio20/direction

# Sets pin 20 to high
echo "1" > /sys/class/gpio/gpio20/value

# Sets pin 18 to low
#echo "0" > /sys/class/gpio/gpio18/value 





while read oneline
do
    keyline=$(echo $oneline | grep " key ")
    echo $keyline --- debugAllLines
    if [ -n "$keyline" ]; then
        datnow=$(date +%s%N)
        datdiff=$((($datnow - $datlastkey) / 1000000)) #bla bla key pressed: previous channel (123)
        strkey=$(grep -oP '(?<=sed: ).*?(?= \()' <<< "$keyline") #bla bla key pres-->sed: >>previous channel<< (<--123)
        strstat=$(grep -oP '(?<=key ).*?(?=:)' <<< "$keyline") #bla bla -->key >>pressed<<:<-- previous channel (123)
        strpressed=$(echo $strstat | grep "pressed")
        strreleased=$(echo $strstat | grep "released")
        if [ -n "$strpressed" ]; then
            strid=$(grep -oP '(\[ ).*?(\])' <<< "$keyline") # get the id from the debug line to ingnore dupe detection.
            #echo $keyline --- debug
            if [ "$strkey" = "$strlastkey" ] && [ "$datdiff" -lt "$intmsbetweenkeys" ]; then
                intkeychar=$((intkeychar + 1)) #same key pressed for a different char
            else
                intkeychar=0 #different key / too far apart
            fi
            datlastkey=$datnow
            strlastkey=$strkey
            if [ "$strid" != "$strlastid" ]; then
                case "$strkey" in
                    "1")
                        xdotool key "BackSpace"
                        ;;
                    "2")
                        keychar "abc2" intkeychar
                        ;;
                    "3")
                        keychar "def3" intkeychar
                        ;;
                    "4")
                        keychar "ghi4" intkeychar
                        ;;
                    "5")
                        keychar "jkl5" intkeychar
                        ;;
                    "6")
                        keychar "mno6" intkeychar
                        ;;
                    "7")
                        keychar "pqrs7" intkeychar
                        ;;
                    "8")
                        keychar "tuv8" intkeychar
                        ;;
                    "9")
                        keychar "wxyz9" intkeychar
                        ;;
                    "0")
                        keychar " 0.-" intkeychar
                        ;;
                    "previous channel")
                        xdotool key "Return" #Enter
                        ;;
                    "electronic program guide")
                        xdotool click 4 #mouse scroll up
                        ;;
                    "setup menu")
                        xdotool click 5 #mouse scroll down
                        ;;
                    "channels list")
                        xdotool click 3 #right mouse button click
                        ;;
                    "up")
                        intpixels=$((-1 * intmousespeed))
                        xdotool mousemove_relative -- 0 $intpixels #move mouse up
                        intmousespeed=$((intmousespeed + intmouseacc)) #speed up
                        ;;
                    "down")
                        intpixels=$(( 1 * intmousespeed))
                        xdotool mousemove_relative -- 0 $intpixels #move mouse down
                        intmousespeed=$((intmousespeed + intmouseacc)) #speed up
                        ;;
                    "left")
                        intpixels=$((-1 * intmousespeed))
                        xdotool mousemove_relative -- $intpixels 0 #move mouse left
                        intmousespeed=$((intmousespeed + intmouseacc)) #speed up
                        ;;
                    "right")
                        intpixels=$(( 1 * intmousespeed))
                        xdotool mousemove_relative -- $intpixels 0 #move mouse right
                        intmousespeed=$((intmousespeed + intmouseacc)) #speed up
                        ;;
                    "select")
                        xdotool click 1 #left mouse button click
                        ;;
                    "root menu")                        
			killall vlc
			
                        ;;
                    "sub picture")
                        echo Key Pressed: SUB PICTURE
			sync;sync;shutdown -h now
                        ;;
                    "F2")
                        #chromium-browser "https://www.youtube.com" &
			./F2.sh
                        ;;
                    "F3")
                        #chromium-browser "https://www.google.com" &
			#streamlink -p "omxplayer --timeout 20" --player-fifo https://www.youtube.com/watch?v=FIBgrDcQ3lw 240p &
			./F3.sh
                        ;;
                    "F4")
                        #echo Key Pressed: YELLOW C
                        #sync;sync;shutdown -h now
			chromium-browser "https://www.youtube.com" 
                        ;;
                    "F1")  
                    	((xvkbd++))
                    	switch=0
                    	xdotool mousemove 1100 750 
                    	xvkbd -no-keypad  -geometry 1920x350+0-20  &
                    	test $xvkbd -eq 2 && killall xvkbd && xvkbd=0 
                    	;;
                        #chromium-browser --incognito "https://www.google.com" &
                        #;;
                    "rewind")
                        echo Key Pressed: REWIND
                        ;;
                    "pause")
                        echo Key Pressed: PAUSE
                        ;;
                    "Fast forward")
                        echo Key Pressed: FAST FORWARD
                        ;;
                    "play")
                        echo Key Pressed: PLAY
                        ;;
                    "stop")
                        ## with my remote I only got "STOP" as key released (auto-released), not as key pressed; see below
                        echo Key Pressed: STOP
                        ;;
                    *)
                        echo Unrecognized Key Pressed: $strkey ; CEC Line: $keyline
                        ;;

                esac
            else
                echo Ignoring key $strkey with duplicate id $strid
            fi
            # store the id of the keypress to check for duplicate press count.
            strlastid=$strid
        fi
        if [ -n "$strreleased" ]; then
            #echo $keyline --- debug
            case "$strkey" in
                "stop")
                    echo Key Released: STOP
                    ;;
                "up")
                    intmousespeed=$intmousestartspeed #reset mouse speed
                    ;;
                "down")
                    intmousespeed=$intmousestartspeed #reset mouse speed
                    ;;
                "left")
                    intmousespeed=$intmousestartspeed #reset mouse speed
                    ;;
                "right")
                    intmousespeed=$intmousestartspeed #reset mouse speed
                    ;;
            esac
        fi
    fi
done
