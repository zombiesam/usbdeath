#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Coded by Sam (info@sam3.se)

import subprocess, time
from os import system

usb_whitelist =[]

p = subprocess.Popen('lsusb', stdout=subprocess.PIPE)
while True:
    line = p.stdout.readline()
    if line != '':
        usb_whitelist.append(line.strip('\n'))
    else:
        break        

while True:
    live_usbs = []
    p = subprocess.Popen('lsusb', stdout=subprocess.PIPE)
    intruder = True
    while True:
        line = p.stdout.readline()
        if line != '':
            live_usbs.append(line.strip('\n'))
        else:
            break       
    
    for usb in live_usbs:
        if not usb in usb_whitelist:
            system('echo 1 > /proc/sys/kernel/sysrq && echo o > /proc/sysrq-trigger')
    time.sleep(1)