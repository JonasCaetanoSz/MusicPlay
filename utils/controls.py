from tkinter import Tk, Canvas, Entry, Text, Button,  filedialog  ,PhotoImage
from PIL import Image,ImageTk
import io
import os
import eyed3
from eyed3.id3.frames import ImageFrame
import pygame as pg

def duration_from_seconds(s):
    """conveter duração da musica."""
    s = s
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    timelapsed = "{:01d}:{:02d}:{:02d}:{:02d}".format(int(d),int(h),int(m),int(s))
    return timelapsed.replace('0:00:', '')


def LoadMetadata(canvas,window, itens, mx):

    file = filedialog.askopenfilename(filetypes=(("Audio Files", ".wav .ogg .mp3"),   ("All Files", "*.*")))
    if file == '' or file == None:

        return False

    else:

        # carregar metadados

        audiofile = eyed3.load(file)
        if (audiofile.tag == None):

            audiofile.initTag()

        # carregar nome da musica

        if audiofile.tag.title == None:

            canvas.itemconfig(itens['title'], text='uncharted song')
            window.title(f'MusicPlay - uncharted song')

        else:

            canvas.itemconfig(itens['title'], text=audiofile.tag.title)
            window.title(f'MusicPlay - {audiofile.tag.title}')

        # carregar nome do album

        if audiofile.tag.album == None:

            canvas.itemconfig(itens['album'], text='uncharted album')
        else:

            canvas.itemconfig(itens['album'], text=audiofile.tag.album)

        # carregar artista

        if audiofile.tag.artist == None:

            canvas.itemconfig(itens['artist'], text='uncharted artist')

        else:

            canvas.itemconfig(itens['artist'], text=audiofile.tag.artist)

        # carregar album cover

        have_photo_the_album = False
        try: audiofile.tag.images[0];have_photo_the_album = True
        except: have_photo_the_album = False

        if have_photo_the_album:

            img = (io.BytesIO(audiofile.tag.images[0].image_data).getvalue())
            open('assets/cover.png', 'wb').write(img)
            img = Image.open('assets/cover.png')
            img = img.resize((200,160), Image.ANTIALIAS)
            img.save('assets/cover.png')
            img = ImageTk.PhotoImage(file=os.getcwd() + '/assets/cover.png')
            canvas.itemconfigure(itens['cover'], image=img)

        else:

            img = ImageTk.PhotoImage(file=os.getcwd()+ '/assets/musiclogo.png')
            canvas.itemconfig(itens['cover'], image=img )

        # duração da musica

        canvas.itemconfig(itens['duration'], text=duration_from_seconds(audiofile.info.time_secs))

    # aumentar tamanho da janela

    window.geometry("560x413")

    # iniciar reprodução
    mx.play(file)




class Music:

    def __init__(self,window,canvas,itens):

        self.itens = itens
        self.canvas = canvas
        self.window = window
        self.playing = False
        pg.init()

    def play(self,filename):

        # tentar descarregar a ultima reprodução
        try: pg.mixer.music.unload()
        except: pass # nenhuma musica carrega anteriomente

        pg.mixer.music.load(filename)
        # music end 

        MUSIC_END = pg.USEREVENT + 1
        pg.mixer.music.set_endevent(MUSIC_END)
        pg.mixer.music.play()
        self.playing = True
        img = PhotoImage(file=os.getcwd() + '/assets/Media-Controls-pause-icon.png')
        self.itens['playbutton'].configure(image=img)
        self.window.mainloop()


    def pause(self):

        if self.playing:

            pg.mixer.music.pause()
            self.playing = False
            img = PhotoImage(file=os.getcwd() + '/assets/music-controls-play.png')
            self.itens['playbutton'].configure(image=img)

        else:

            pg.mixer.music.unpause()
            self.playing = True
            img = PhotoImage(file=os.getcwd() + '/assets/Media-Controls-pause-icon.png')
            self.itens['playbutton'].configure(image=img)

        self.window.mainloop()

    def rewindS(self):

        print('sorry this function not available.')

    def advanceS(self):

        print('sorry this function not available.')