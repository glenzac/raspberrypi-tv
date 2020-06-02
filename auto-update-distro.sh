#!/bin/bash
echo "**********" >> /logs/update-date
'date' >> /logs/update-date
echo "UPDATING SYSTEM SOFTWARE - UPDATE" >> /logs/update-log
sudo apt-get update
echo "UPGRADING SYSTEM SOFTWARE - UPGRADE" >> /logs/update-log
sudo apt-get –y upgrade
echo "UPGRADING SYSTEM SOFTWARE -DISTRIBUTION" >> /logs/update-log
sudo apt –y dist-upgrade
echo "REMOVING OBSOLETE DEPENDENCIES" >> /logs/update-log
sudo apt-get –y autoremove
echo "REMOVING OBSOLETE FILES" >> /logs/update-log
sudo apt-get autoclean
echo "SYSTEM REBOOT" >> /logs/update-log
sudo reboot