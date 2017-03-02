# dota2_automation

Collection of tools which helps with common Dota tasks (only tested on Arch with KDE).
You use it on your own risk!

## autoaccept

system.d service which plays sound when matchmaking game is found and dota runs in background
(eg. on another desktop), than activates dota2 window and clicks enter to accept game.

DISCLAIMER: Be sure to not shift+tab in dota when relaying on script

### requirements

    python
    wmctrl
    xdotool
    aplay

### installation & usage

1 clone repo

    git clone git@github.com:pawelma/dota2_automation.git

2a run script

    dota2_automation/autoaccept.py

2b start/stop script

    sudo make install
    d2_automation start

2c
last solution doesn't work yet because there is a problem with PolicyKit and dBus

### configuration options

Script can be configured via following environment variables (examples are given with defaults):

* accepts matchmaking game automaticly

      D2_AUTOACCEPT=1

* sets time.sleep before autoaccepts (you can increase on older or high loaded PCs when window switch longer than given value)

      D2_AUTOACCEPTDELAY=1

* plays sound notification when game runs in backround (you're alt+tab or on different workspace)

      D2_NOTIFY=1

### TODO:

install as system.d service:

    cd dota2_automation
    make
    sudo make install
    sudo systemctl start d2_automation.service

