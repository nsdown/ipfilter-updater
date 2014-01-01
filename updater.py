#!/usr/bin/env python

import gzip
import tempfile
import sys
import os
import urllib2
from datetime import datetime

homeDirPath = os.path.expanduser("~")
logFilePath = os.path.join(homeDirPath, '.ipfilter-updater.log')
logFile = open(logFilePath, 'a')

def log(s):
    dt = datetime.now()
    str = dt.strftime("%Y-%m-%d %H:%M:%S")
    print str + "> " + s
    logFile.write(str + "> " + s + "\n")
    logFile.flush()
    os.fsync(logFile.fileno())

def download(tmpFile):
    response = urllib2.urlopen('http://tbg.iblocklist.com/Lists/ipfilter.dat.gz')
    ipfilterDataGz = response.read()
    response.close()

    os.write(tmpFile, ipfilterDataGz)
    os.close(tmpFile)
     
def update():
    log('Downloading ipfilter data...')
    tmpFile, tmpFilePath = tempfile.mkstemp('.gz', 'ipfilter-updater-')

    try:
        download(tmpFile)
        log('ipfilter data downloaded to '+tmpFilePath)
        
        f = gzip.open(tmpFilePath, 'rb')
        ipfilterData = f.read()
        f.close()
    finally:
        os.remove(tmpFilePath)

    uTorrentDirPath = os.path.join(homeDirPath, 'Library', \
                      'Application Support', \
                      'uTorrent')
    added = False

    if os.path.isdir(uTorrentDirPath):
        targetFile = open(os.path.join(uTorrentDirPath, 'ipfilter.dat'),'wb')
        targetFile.write(ipfilterData)
        targetFile.close()
        log('Added to uTorrent')
        added = True

    if not added:
        log('WARNING: not added to any app')

def main():
    log('---------Session started-----------')
    update()
    log('---------Session ended----------')
    logFile.close()

if __name__ == '__main__':
    main()

