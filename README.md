ipfilter-updater
================

ipfilter updater for Unix, Mac OS, Linux

The ipfilter list contains the list of IPs that are invalid, i.e., set up by 
anti-p2p organizations. If your torrent client connects to one of these,
you may get corrupted data or even have your IP recorded down by them.

This updater serves to download the list maintained by iblocklist.com
for use by uTorrent.

Currently, this only works for uTorrent in Mac OS X, but it can be easily 
modified to work on any system.
This is only tested for Mac OS X 10.8 (Mountain Lion), although it should also
work for Snow Leopard.

Requirements
============
This requires Python 2.3 and above.

Configuring
===========
1) In the uTorrent window in Mac, press Command+Option+, (yes, comma)
   all three keys at the same time.

2) The options window with the advanced tab should show up. 
   Scroll down to ensure that ipfilter.enable is set to true.

Installing
==========
The aim is to set up a cron job for the updater script.

1) Clone this repo to your local machine

2) Do "crontab -e". This will bring up an editor.

3) Enter "00 21 * * * path/to/updater.py" on a line of its own 
   without the quotes and save.
   Please escape any space in the path.
   This means run the updater at 9 PM (21:00) every day.
   To start typing in vim, press i
   To save in vim, press Escape and then :wq (colon w q) and Enter.

4) Do "crontab -l" to verify you have entered the cronjob correctly.

