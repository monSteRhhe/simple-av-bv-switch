#!/usr/bin/python3
# -*- coding:utf-8 -*-

# ver ui-0.4

from tkinter import *

root = Tk()
root.title("av-bv Switch")
width = 400
height = 100
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
root.geometry(size)

Label(root, text= "输入：").grid(row=0, column=0)
Label(root, text= "输出：").grid(row=1, column=0)

getin = StringVar()
inbox = Entry(root, textvariable=getin, width = 30)
outbox = Text(root, height = 1, width = 30)
inbox.grid(row=0, column=1)
outbox.grid(row=1, column=1)

anno = Label(root, text = "输入时省略“av”和“BV”")
anno.grid(row =3 ,column =1)

def charcheck(stri):
    import re
    return bool(re.search('[a-z]', stri))

def vswitch():
    from urllib import request
    import json

    outbox.delete('1.0', END)
    stri = inbox.get()
    c = int(charcheck(stri))
    if c:
        html = request.urlopen(r'http://api.bilibili.com/x/web-interface/view?bvid='+stri)
    else:
        html = request.urlopen(r'http://api.bilibili.com/x/web-interface/view?aid='+stri)
    getjson = json.loads(html.read())
    if getjson['code'] == 0:
        if c:
            outbox.insert(INSERT, 'av')
            outbox.insert(END, getjson['data']['aid'])
        else:
            outbox.insert(INSERT, getjson['data']['bvid'])
    else:
       outbox.insert(INSERT, "稿件不可见。")

def clear():
    inbox.delete(0, END)
    outbox.delete('1.0', END)

def touchmain(self):
    vswitch()

btn = Button(root, text = "转换", width = 10, command = vswitch)
btn.grid(row = 3 ,column = 0, padx=10, pady =5)

delbtn = Button(root, text = "清除", width = 8, command = clear)
delbtn.grid(row = 0, column = 2, padx=10, pady =5)

root.bind('<Return>', touchmain)

root.mainloop()
