import sys
import os

import pygame as pg
import pygame.midi

#List midi devices
def midi_device_info():
    pygame.midi.init()
    defaultdevice = None
    for i in range(pygame.midi.get_count()):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r

        in_out = ""
        
        if input:
            in_out = "(input)"
            if defaultdevice == None:
                defaultdevice = i
                print(defaultdevice)
        if output:
            in_out = "(output)"

        print(
            "%2i: interface :%s:, name :%s:, opened :%s:  %s"
            % (i, interf, name, opened, in_out)
        )
    print(defaultdevice)
    return defaultdevice


def midi_device_select(input_id = None):
    i = None
    #Detect if there is a user selection 
    if input_id == None:
        default_dev = midi_device_info()
        #If user selection no found, look for a default device
        if default_dev == None:
            print("No found default midi input device")
            return None
        else:
            input_id = default_dev
    else:
        print("Using Midi Input Device <%s>" % input_id)
    i = pygame.midi.Input(input_id)
    return i
 

