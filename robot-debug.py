#!/usr/bin/env python
import sys
import serial

if len(sys.argv) == 1:
    exit()

port = sys.argv[1]


def send(data):
    with serial.Serial(port, 115200) as s:
        s.write(data.encode())


def reset():
    send('0:0,0,0')


reset()

while True:
    txt = input(':')
    txt_list = txt.split()
    txt_len = len(txt_list)
    if txt_len < 2:
        reset()
    if txt_len == 1:
        if txt_list[0] == 'q':
            exit()
    elif txt_len == 2:
        send('{}:{},0,0'.format(txt_list[0], txt_list[1]))
    elif txt_len == 3:
        send('{}:{},{},0'.format(txt_list[0], txt_list[1], txt_list[2]))
    elif txt_len > 3:
        send('{}:{},{},{}'.format(txt_list[0], txt_list[1], txt_list[2], txt_list[3]))
