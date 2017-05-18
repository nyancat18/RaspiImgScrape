#!/bin/bash
echo "RUN AS ROOT"
cp blogdownloader.service /lib/systemd/system/blogdownloader.service
cp test1.py /home/pi/test1.py
cp reader.sh /home/pi/reader.sh
cp run.sh /home/pi/run.sh 