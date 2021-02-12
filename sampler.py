import pygame as pg
import pygame._sdl2 as sdl2


class Buttonclass:

    def __init__(self, sizex, sizey, posx, posy, vol, screen):
        self.sizex = sizex
        self.sizey = sizey
        self.posx = posx
        self.posy = posy
        self.vol = vol
        self.screen = screen
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
            self.buttonsurf.fill((255,255,255))
        else:
            self.buttonsurf.fill((120,0,0)) 
        self.screen.blit(self.buttonsurf,self.buttonrect)
        #Update container for volume bar
        self.volumecontsurf.fill((0,0,0))
        self.screen.blit(self.volumecontsurf, self.volumecontrect)
        #Update volume bar
        self.volumesurf.fill((120,0,0))
        self.screen.blit(self.volumesurf, self.volumerect)

        

    def buttonSound(self, file):
        pg.mixer.music.load(file)
        pg.mixer.music.play()

#Function for enum and name Sound Device
def initSoundDevice():

    is_capture = 0  # zero to request playback devices, non-zero to request recording devices
    num = sdl2.get_num_audio_devices(is_capture)
    names = [str(sdl2.get_audio_device_name(i, is_capture), encoding="utf-8") for i in range(num)]
    return names


# initializing the general settings
pg.init() 
FPS = 30
hitcounter = 0
vol = 1
fpsClock = pg.time.Clock()
devices = initSoundDevice()
pg.mixer.pre_init(devicename=devices[0])
#print(len(devices))
pg.mixer.init()


#set the width and height of the screen
size = [500, 500]
screen = pg.display.set_mode(size)

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
            if button1.buttonrect.collidepoint(mousepos):
                button1.buttonSound("ULTRAPOBRE.MP3")  
            if button2.buttonrect.collidepoint(mousepos):
                button2.buttonSound("AIRHORN.MP3")
            if button3.buttonrect.collidepoint(mousepos):
                button3.buttonSound("BATERIA.MP3")              
            if button4.buttonrect.collidepoint(mousepos):
                button4.buttonSound("BESTIAS.MP3")
            if button5.buttonrect.collidepoint(mousepos):
                button5.buttonSound("TRANSFORMERS.MP3")
            if button6.buttonrect.collidepoint(mousepos):
                button6.buttonSound("XMEN.MP3")
            if button7.buttonrect.collidepoint(mousepos):
                button7.buttonSound("OOF.WAV")
            #changing volume bar size clicking on it
            if button1.volumecontrect.collidepoint(mousepos):
                if pg.mouse.get_pos()[1] < (button1.posy+(button1.sizey*button1.vol)) and button1.vol >=0.10:
                    button1.vol = ((pg.mouse.get_pos()[1]-button1.posy)*1)/button1.sizey
                    print(button1.vol)
                    button1.volumesurf.fill((0,0,0))
                    screen.blit(button1.volumesurf, button1.volumerect)
                elif pg.mouse.get_pos()[1] > (button1.posy+(button1.sizey*button1.vol)) and button1.vol <=1:
                    volinc = pg.mouse.get_pos()[1] - button1.posy
                    button1.vol = volinc/button1.sizey
                    print("volinc is {}".format(volinc))
                    print("vol is {}".format(button1.vol))
                    button1.volumesurf.fill((120,0,0))
                    screen.blit(button1.volumesurf, button1.volumerect)
            if button7.volumecontrect.collidepoint(mousepos):
                if pg.mouse.get_pos()[1] < (button7.posy+(button7.sizey*button7.vol)) and button7.vol >=0.10:
                    button7.vol = ((pg.mouse.get_pos()[1]-button7.posy)*1)/button7.sizey
                    print(button7.vol)
                    button7.volumesurf.fill((0,0,0))
                    screen.blit(button7.volumesurf, button7.volumerect)
                elif pg.mouse.get_pos()[1] > (button7.posy+(button7.sizey*button7.vol)) and button7.vol <=1:
                    volinc = pg.mouse.get_pos()[1] - button7.posy
                    button7.vol = volinc/button7.sizey
                    print("volinc is {}".format(volinc))
                    print("vol is {}".format(button7.vol))
                    button7.volumesurf.fill((120,0,0))
                    screen.blit(button7.volumesurf, button7.volumerect)


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
                pg.mixer.init()

    button1.buttonDraw()
    button2.buttonDraw()
    button3.buttonDraw()
    button4.buttonDraw()
    button5.buttonDraw()
    button6.buttonDraw()
    button7.buttonDraw()
    mousepos = pg.mouse.get_pos()
    pg.display.update()
    fpsClock.tick(FPS)