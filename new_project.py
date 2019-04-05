#<----------------   import modules ---------------->
# random.randint(0,257)
import os
from tkinter import *
from tkinter import messagebox as mbox
from PIL import Image,ImageDraw,ImageFont,ImageTk
import random 

def create_captch():
    characters="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    global c1,c2,c3,c4
    c1=characters[random.randint(0,len(characters)-1)]
    c2=characters[random.randint(0,len(characters)-1)]
    c3=characters[random.randint(0,len(characters)-1)]
    c4=characters[random.randint(0,len(characters)-1)]
    img = Image.new('RGB', (400,100), color = (255,255,255))
    d = ImageDraw.Draw(img)
    t = ImageDraw.Draw(img)
    character = []
    font1 = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf",35)
    font2 = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf",40)
    font3 = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf",43)
    font4 = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSerif.ttf",45)
    t.text((160,30), c1, font=font1 ,fill=(random.randint(0,257),random.randint(0,257),random.randint(0,257),10))
    t.text((180,30), c2, font=font2 ,fill=(random.randint(0,257),random.randint(0,257),random.randint(0,257),10))
    t.text((200,30), c3, font=font3 ,fill=(random.randint(0,257),random.randint(0,257),random.randint(0,257),10))
    t.text((220,30), c4, font=font4 ,fill=(random.randint(0,257),random.randint(0,257),random.randint(0,257),10))
    d.line((150,30) + (240,60), fill=random.randint(0,257))
    d.line((150,60) + (240,40), fill=random.randint(0,257))
    d.line((180,70) + (160,30), fill=random.randint(0,257))
    d.line((220,70) + (240,30), fill=random.randint(0,257))
    img.save('pil.png')

def create_gui():
    create_captch()
    master=Tk()
    master.title("captcha")
    master.config(width=1000, height=1000)
    images=ImageTk.PhotoImage(Image.open("pil.png"))
    reload_img=ImageTk.PhotoImage(Image.open("reload.jpg"))
    os.remove("pil.png")
    captcha=Label(master, image=images, )
    captcha.config(width=420, height=150)
    captcha.pack()
    entry=Entry(master)
    entry.pack() 
    def check():
        global ran
        if entry.get() == c1+c2+c3+c4:
            mbox.showinfo('Congratulations..!!','Have a nice day!')
            master.destroy()
        else: 
            entry.delete(0, 'end')
            mbox.showerror('Try again.!!!!','Wrong Captcha')
            master.destroy()
            create_gui()
    def refresh():
        master.destroy()
        create_gui()
    refresh_button=Button(master,command = refresh)
    refresh_button.config(image=reload_img)
    refresh_button.pack(side=RIGHT)
    button=Button(master,text="Submit", command = check)
    button.pack()
    master.mainloop()

c1,c2,c3,c4=0,0,0,0
create_gui()
