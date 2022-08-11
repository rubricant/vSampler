import pygame as pg
import pygame._sdl2 as sdl2
import pygame._sdl2.audio as sdl2_audio
import midicontroller as mc
from decimal import Decimal



class Buttonclass:

    def __init__(self, sizex, sizey, posx, posy, vol, screen):
        self.sizex = sizex
        self.sizey = sizey
        self.posx = posx
        self.posy = posy
        self.vol = vol
        self.screen = screen
        self.midibuttonstatus = False
        self.buttonsurf = pg.Surface((self.sizex, self.sizey))
        self.buttonrect = self.buttonsurf.get_rect(x=self.posx,y=self.posy)

        
    #Draw the button and check if the mouse is over
    def buttonDraw(self):
        self.volumesurf = pg.Surface((int(self.sizex/4), int(self.sizey*self.vol)))
        self.volumerect = self.volumesurf.get_rect(x=(self.posx+self.sizex+5), y=self.posy)
        self.volumecontsurf = pg.Surface((int(self.sizex/4), int(self.sizey*1.01)))
        self.volumecontrect = self.volumecontsurf.get_rect(x=(self.posx+self.sizex+5), y=self.posy)

        #Update button if mouse is on
        if self.buttonrect.collidepoint(pg.mouse.get_pos()):
            self.midibuttonstatus= True
        if self.midibuttonstatus == True:
            self.buttonsurf.fill((255,255,0))
        if self.midibuttonstatus == False:
            self.buttonsurf.fill((120,0,0))
        self.screen.blit(self.buttonsurf,self.buttonrect)
        #Update container for volume bar
        self.volumecontsurf.fill((0,0,0))
        self.screen.blit(self.volumecontsurf, self.volumecontrect)
        #Update volume bar
        self.volumesurf.fill((120,0,0))
        self.screen.blit(self.volumesurf, self.volumerect)
        

    def buttonSound(self, file):

        pg.mixer.music.set_volume(self.vol)
        pg.mixer.music.load(file)
        pg.mixer.music.play()
        
    def buttonVolume(self):
        if pg.mouse.get_pos()[1] < (self.posy+(self.sizey*self.vol)) and self.vol >=0.10:
            self.vol = ((pg.mouse.get_pos()[1]-self.posy)*1)/self.sizey
            print(self.vol)
            self.volumesurf.fill((0,0,0))
            screen.blit(self.volumesurf, self.volumerect)
        elif pg.mouse.get_pos()[1] > (self.posy+(self.sizey*self.vol)) and self.vol <=1:
            volinc = pg.mouse.get_pos()[1] - self.posy
            self.vol = volinc/self.sizey
            print("volinc is {}".format(volinc))
            print("vol is {}".format(self.vol))
            self.volumesurf.fill((120,0,0))
            screen.blit(self.volumesurf, self.volumerect)

#List sound playback devices
def initSoundDevice():
    pg.mixer.init()
    devices = sdl2_audio.get_audio_device_names(False) #false to request playback device, true for recording devices
    print(devices)
    pg.mixer.quit
    return devices



# initializing the general settings
pg.init() 
FPS = 30
hitcounter = 0
vol = 1
fpsClock = pg.time.Clock()
devices = initSoundDevice()
pg.mixer.pre_init(devicename=devices[0])
font = pg.font.SysFont("console", 12)
text = font.render("1: {}".format(devices[0]), 0, (255, 255, 255))
device_input = mc.midi_device_select()
#print(len(devices))
pg.mixer.init()


#set the width and height of the screen
size = [500, 500]
screen = pg.display.set_mode(size)
pg.display.set_caption("vSampler")

button1 = Buttonclass(50,50, 50, 50, vol, screen)
button2 = Buttonclass(50,50, 140, 50, vol, screen)
button3 = Buttonclass(50,50, 230, 50, vol, screen)
button4 = Buttonclass(50,50, 50, 120, vol, screen)
button5 = Buttonclass(50,50, 140, 120, vol, screen)
button6 = Buttonclass(50,50, 230, 120, vol, screen)
button7 = Buttonclass(190,150, 50, 185, vol, screen)

#Variable for loops
done = 1

while done == 1:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.mixer.quit()
            done = 0
        if event.type == pg.MOUSEBUTTONDOWN:
            # Play sound clicking on buttons
            if button1.buttonrect.collidepoint(mousepos):
                button1.buttonSound("ULTRAPOBRE.MP3")  
            if button2.buttonrect.collidepoint(mousepos):
                button2.buttonSound("AIRHORN.WAV")
            if button3.buttonrect.collidepoint(mousepos):
                button3.buttonSound("AIRHORN.WAV")              
            if button4.buttonrect.collidepoint(mousepos):
                button4.buttonSound("AIRHORN.WAV")
            if button5.buttonrect.collidepoint(mousepos):
                button5.buttonSound("AIRHORN.WAV")
            if button6.buttonrect.collidepoint(mousepos):
                button6.buttonSound("AIRHORN.WAV")
            if button7.buttonrect.collidepoint(mousepos):
                button7.buttonSound("AIRHORN.WAV")
            #changing volume clicking on it
            if button1.volumecontrect.collidepoint(mousepos):
                button1.buttonVolume()
            if button2.volumecontrect.collidepoint(mousepos):
                button2.buttonVolume()
            if button3.volumecontrect.collidepoint(mousepos):
                button3.buttonVolume()
            if button4.volumecontrect.collidepoint(mousepos):
                button4.buttonVolume()
            if button5.volumecontrect.collidepoint(mousepos):
                button5.buttonVolume()
            if button6.volumecontrect.collidepoint(mousepos):
                button6.buttonVolume()
            if button7.volumecontrect.collidepoint(mousepos):
                button7.buttonVolume()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:     
                pg.mixer.quit()
                pg.mixer.pre_init(devicename=devices[0])
                pg.mixer.init()
                print(devices[0])
            if event.key == pg.K_2:
                pg.mixer.quit()
                pg.mixer.pre_init(devicename=devices[1])
                pg.mixer.init()
                print(devices[1])
            if event.key == pg.K_3:
                pg.mixer.quit()
                pg.mixer.pre_init(devicename=devices[2])
                print(devices[2])
                pg.mixer.init()      
            if event.key == pg.K_4:
                pg.mixer.quit()
                pg.mixer.pre_init(devicename=devices[3])
                print(devices[3])
                pg.mixer.init()
            if event.key == pg.K_8:
                hitcounter += 1
                if hitcounter > (len(devices)-1):
                    hitcounter = 0
                pg.mixer.quit()
                pg.mixer.pre_init(devicename=devices[hitcounter])
                print(devices[hitcounter])
                text = font.render("1: {}".format(devices[hitcounter-1]), 0, (0,0,0))
                screen.blit(text, (50,400))
                text = font.render("1: {}".format(devices[hitcounter]), 0, (255, 255, 255))
                pg.mixer.init()

    if device_input != None:
        if device_input.poll():
            midi_events = device_input.read(100)

            for midi_event in midi_events:
                print(midi_event)
                if midi_event[0][1] == 48 and midi_event[0][0] == 144:
                    button1.buttonSound("ULTRAPOBRE.MP3")
                    button1.midibuttonstatus = True
                if midi_event[0][1] == 48 and midi_event[0][0] == 128:
                    button1.midibuttonstatus = False

                if midi_event[0][1] == 49 and midi_event[0][0] == 144:
                    button2.buttonSound("AIRHORN.WAV")
                    button2.midibuttonstatus = True
                if midi_event[0][1] == 49 and midi_event[0][0] == 128:
                    button2.midibuttonstatus = False

                if midi_event[0][1] == 50 and midi_event[0][0] == 144:
                    button3.buttonSound("AIRHORN.WAV")
                    button3.midibuttonstatus = True
                if midi_event[0][1] == 50 and midi_event[0][0] == 128:
                    button3.midibuttonstatus = False

                if midi_event[0][1] == 51 and midi_event[0][0] == 144:
                    button4.buttonSound("AIRHORN.WAV")  
                    button4.midibuttonstatus = True
                if midi_event[0][1] == 51 and midi_event[0][0] == 128:
                    button4.midibuttonstatus = False

                if midi_event[0][1] == 52 and midi_event[0][0] == 144:
                    button5.buttonSound("AIRHORN.WAV")
                    button5.midibuttonstatus = True
                if midi_event[0][1] == 52 and midi_event[0][0] == 128:
                    button5.midibuttonstatus = False

                if midi_event[0][1] == 53 and midi_event[0][0] == 144:
                    button6.buttonSound("AIRHORN.WAV")
                    button6.midibuttonstatus = True
                if midi_event[0][1] == 53 and midi_event[0][0] == 128:
                    button6.midibuttonstatus = False

                if midi_event[0][1] == 54 and midi_event[0][0] == 144:
                    button7.buttonSound("AIRHORN.WAV") 
                    button7.midibuttonstatus = True
                if midi_event[0][1] == 54 and midi_event[0][0] == 128:
                    button7.midibuttonstatus = False                                                                                 
    
                              

    button1.buttonDraw()
    button2.buttonDraw()
    button3.buttonDraw()
    button4.buttonDraw()
    button5.buttonDraw()
    button6.buttonDraw()
    button7.buttonDraw()
    button1.midibuttonstatus = False
    button2.midibuttonstatus = False 
    button3.midibuttonstatus = False
    button4.midibuttonstatus = False  
    button5.midibuttonstatus = False
    button6.midibuttonstatus = False
    button7.midibuttonstatus = False          
    screen.blit(text, (50,400))
    mousepos = pg.mouse.get_pos()
    pg.display.update()
    fpsClock.tick(FPS)
del device_input