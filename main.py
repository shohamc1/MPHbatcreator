from tkinter import *

file = open ("start.bat", "w")

name1 = ""
name2 = ""

root = Tk()

def get_value():
    global name1
    global name2
    name1 = text1.get ("1.0", "end-1c")
    name2 = text2.get ("1.0", "end-1c")

label1 = Label (root, text = "Username: ")
label2 = Label (root, text = "Worker name: ")
text1 = Text (root, height = 1, width = 10)
text2 = Text (root, height = 1, width = 10)
commit = Button (root,text="Generate .bat!", command=lambda: get_value())

label1.grid (row=0, column=0)
label2.grid (row=1, column=0)
text1.grid (row=0, column=2)
text2.grid (row=1, column=2)
commit.grid (row=2,column=1)

mainloop()

s = "EthDcrMiner64.exe -epool asia.ethash-hub.miningpoolhub.com:20535 -ewal " + name1 + "." + name2 + " -eworker " + name1 + "." + name2 + " -esm 2 -epsw x"

file.write(s)