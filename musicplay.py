from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from utils.controls import *
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# itens da tela para editar

ITENS = {
    
    'playbutton':None,
    'cover':None,
    'artist':None,
    'album':None,
    'title': None,
    'backbutton':None,
    'gobutton':None,
    'duration':None,
    'musicr':None
}



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("520x413")
window.configure(bg = "#decafe")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 413,
    width = 520,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
ITENS['musicr'] = canvas.create_rectangle(
    0.0,
    0.0,
    520.0,
    413.0,
    fill="#decafe",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    223.82916259765625,
    413.0,
    fill="#1C2123",
    outline="")

ITENS['title'] = canvas.create_text(
    272.0,
    237.0,
    anchor="nw",
    text="Song name",
    fill="#0F0E0E",
    font=("FontAwesome5Brands Regular", 14 * -1)
)

ITENS['album'] = canvas.create_text(
    272.0,
    278.0,
    anchor="nw",
    text="Album name",
    fill="#0C0C0C",
    font=("FontAwesome5Brands Regular", 14 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:LoadMetadata(canvas,window, ITENS, mx),
    relief="flat"
)
button_1.place(
    x=52.0,
    y=167.0,
    width=119.31350708007812,
    height=39.0
)

canvas.create_text(
    62.0,
    30.0,
    anchor="nw",
    text="MusicPlay",
    fill="#FFFFFF",
    font=("Karma Regular", 20 * -1)
)

ITENS['artist'] = canvas.create_text(
    272.0,
    318.0,
    anchor="nw",
    text="Artist",
    fill="#0F0E0E",
    font=("FontAwesome5Brands Regular", 14 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("musiclogo.png"))
image_1 = canvas.create_image(
    372.0,
    92.0,
    image=image_image_1,
    tag='cover'
)

ITENS['cover'] = image_1

canvas.create_rectangle(
    414.0,
    150.0,
    472.0,
    172.0,
    fill="#292A2B",
    outline="")

ITENS['duration'] = canvas.create_text(
    431.0,
    152.0,
    anchor="nw",
    text="00:00",
    fill="#FFFFFF",
    font=("Kanit Bold", 10 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("music-controls-play.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mx.pause(),
    relief="flat"
)

ITENS['playbutton'] = button_2
button_2.place(
    x=349.0,
    y=188.0,
    width=36.0,
    height=20.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("music-controls-go.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:mx.advanceS(),
    relief="flat"
)
button_3.place(
    x=405.0,
    y=188.0,
    width=36.0,
    height=20.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("music-controls-back.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mx.rewindS(),
    relief="flat"
)
button_4.place(
    x=288.0,
    y=188.0,
    width=36.0,
    height=20.0
)

mx = Music(window, canvas, ITENS)
window.title('MusicPlay')
window.iconbitmap(relative_to_assets('ico.ico'))
window.resizable(False, False)
window.mainloop()