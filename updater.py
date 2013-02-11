#!/usr/bin/python

import gzip
import tempfile
import sys
import os
import urllib2
from datetime import datetime
from os.path import expanduser

homeDirPath = expanduser("~")

tempDirPath = tempfile.gettempdir()
logFilePath = os.path.join(homeDirPath, 'ipfilter-updater.log')
logFile = open(logFilePath, 'a')

def log(s):
    dt = datetime.now()
    str = dt.strftime("%Y-%m-%d %H:%M:%S")
    print str + "> " + s
    logFile.write(str + "> " + s + "\n")
    logFile.flush()
    os.fsync(logFile.fileno())

def main():
    log('Downloading ipfilter data...')
    tmpFile, tmpFilePath = tempfile.mkstemp('.gz', 'ipfilter-updater-')
    response = urllib2.urlopen('http://tbg.iblocklist.com/Lists/ipfilter.dat.gz')
    ipfilterDataGz = response.read()
    os.write(tmpFile, ipfilterDataGz)
    os.close(tmpFile)
    log('ipfilter data downloaded to '+tmpFilePath)
    
    ipfilterDataGz = ''
    f = gzip.open(tmpFilePath, 'rb')
    ipfilterData = f.read()
    f.close()

    os.remove(tmpFilePath)

    uTorrentDirPath = os.path.join(homeDirPath, 'Library', \
                      'Application Support', \
                      'uTorrent')
    added = 0
    if os.path.isdir(uTorrentDirPath):
        targetFile = open(os.path.join(uTorrentDirPath, 'ipfilter.dat'),'wb')
        targetFile.write(ipfilterData)
        targetFile.close()
        log('Added to uTorrent')
        added = 1

    if not added:
        log('WARNING: not added to any app')

log('---------Session started-----------')
main()
log('---------Session ended----------')
logFile.close()

