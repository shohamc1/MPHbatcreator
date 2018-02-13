from tkinter import *
from tkinter import messagebox

file = open ("start.bat", "w")

s = ""

def goEU():
    global s
    s = "EthDcrMiner64.exe -epool europe.ethash-hub.miningpoolhub.com:20535 -ewal " + name1 + "." + name2 + " -eworker " + name1 + "." + name2 + " -esm 2 -epsw x"

def goUS():
    global s
    s = "EthDcrMiner64.exe -epool us-east.ethash-hub.miningpoolhub.com:20535 -ewal " + name1 + "." + name2 + " -eworker " + name1 + "." + name2 + " -esm 2 -epsw x"

def goAS():
    global s
    s = "EthDcrMiner64.exe -epool asia.ethash-hub.miningpoolhub.com:20535 -ewal " + name1 + "." + name2 + " -eworker " + name1 + "." + name2 + " -esm 2 -epsw x"


def get_value():
    global name1
    global name2
    name1 = text1.get ("1.0", "end-1c")
    name2 = text2.get ("1.0", "end-1c")
    if sel_option.get() == "Europe":
        goEU()
    if sel_option.get() == "Asia":
        goAS()
    if sel_option.get() == "US":
        goUS()
    messagebox.showinfo ("Success", "Batch file has been generated!")

name1 = ""
name2 = ""
choices = {"US", "Europe", "Asia"}


root = Tk()
root.title ("MPHbatcreator")


sel_option = StringVar (root)
sel_option.set("Asia")

label1 = Label (root, text = "Username: ")
label2 = Label (root, text = "Worker name: ")
text1 = Text (root, height = 1, width = 10)
text2 = Text (root, height = 1, width = 10)
commit = Button (root,text="Generate .bat!", command=lambda: get_value())
popup = OptionMenu (root, sel_option, *choices)


label1.grid (row=0, column=0)
label2.grid (row=1, column=0)
text1.grid (row=0, column=2)
text2.grid (row=1, column=2)
commit.grid (row=3,column=1)
popup.grid (row = 2, column=1)

root.mainloop()

print(s)
file.write(s)