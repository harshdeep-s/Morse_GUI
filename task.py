import time
from tkinter import*
from array import*
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)


win = Tk()

win.title('morse code')
win.geometry("400x250")

time1 = 0.5
time2 = 1.5

alpha = "abcdefghijklmnopqrstuvwxyz"

morse = [["d","s"],["s","d","d","d"],["s","d","s","d"],["s","d","d"],["d"],
["d","d","s","d"],["s","s","d"],["d","d","d","d"],["d","d"],["d","s","s","s"],["s","d","s"],["d","s","d","d"],["s","s"],
["s","d"],["s","s","s"],["d","s","s","d"],["s","s","d","s"],["d","s","d"],["d","d","d"],["s"],["d","d","s"],
["d","d","d","s"],["d","s","s"],["s","d","d","s"],["s","d","s","s"],["s","s","d","d"]]

def glow():
    var1 = str(e.get())
    morsecall(var1)
    e.delete(0, END)
    
   

def exit():
    win.destroy()



def dash():
    GPIO.output(10, GPIO.HIGH)
    time.sleep(time2)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.1)

def dot():
    GPIO.output(10, GPIO.HIGH)
    time.sleep(time1)
    GPIO.output(10, GPIO.LOW)
    time.sleep(0.1)


def checkalpha(words):
    i= 0
    while(i < len(alpha)):
        if(alpha[i] == words):
            return i
        i=i+1
        
        
label1 = Label(win)
label1.grid(row = 2, column = 3)

label2 = Label(win)
label2.grid(row=3, column = 3)

name = Label(win, text = "enter your name:").grid(row= 1, column=0)
name1 = Button(win, text = "submit", command = glow).grid(row=2, column=0)

exit = Button(win, text = "EXIT", command=exit).grid(row = 4, column = 3)

e = Entry(win, width = 30, textvariable = StringVar())
e.grid(row = 1, column=3)

def morsecall(name):
    print(name)
    label1.config(text = "morse code for name: " + name)
    i= 0
    if(len(name) > 1 and len(name) < 12):
        while(i< len(name)):              
            l = checkalpha(name[i])
            label2.config(text = "glowing led for word: "+name[i])
            win.update()
            i=i+1
            j=0
            while(j < len(morse[l])):
                light = morse[l][j]
                if(light == "d"):
                    dot()
                elif(light == "s"):
                    dash()
                j=j+1
            time.sleep(2)

win.mainloop()


            
            
            
            
