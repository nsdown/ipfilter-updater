ipfilter-updater
================

ipfilter updater for Unix, Mac OS, Linux

Currently, this only works for uTorrent in Mac OS X, but it can be easily 
modified to work on any system.
This is only tested for Mac OS X 10.8 (Mountain Lion), although it should also
work for Snow Leopard.

Requirements
============
This requires Python 2.3 and above.


Installing
==========
1) Clone this repo to your local machine
2) Do "crontab -e". This will bring up an editor.
3) Enter "00 21 * * * path/to/updater.py" without the quotes and save.
   This means run the updater at 9 PM (21:00) every day.
   To start typing in vim, press i
   To save in vim, press Escape and then :wq (colon w q) and Enter.

4) Do "crontab -l" to verify you have entered the cronjob correctly.

