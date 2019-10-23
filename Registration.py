#Simple registration app in python with a GUI built from tkinter
# 
#   Created by Robert Zeelie         26\09\19
#
#Just Run program but you can change type of output by changing button1 command between either print1 or print2

from tkinter import *
from PIL import Image, ImageTk

#---------------------------------------------------------------------------------------------------------------------------
#create the window and add size and title to it
window = Tk()
window.geometry("700x500")
window.title(" RAZ Tech")

#---------------------------------------------------------------------------------------------------------------------------
#Adding a logo
#first get the picture then save it in pic
image = Image.open("C:/Python/Python Projects/TKINTER/Exam Registration/pic.jpg")
pic = ImageTk.PhotoImage(image)
#build pic and add it to window
label0 = Label(image = pic)
label0.pack()

#---------------------------------------------------------------------------------------------------------------------------
#functions for the buttons to perform
#exit function
def exit1():
    exit()

#this function prints information to the console 
def print1():
    Name = fullName.get()
    emailAdd = email.get()
    DOB = (placeHolder1.get() + " " + placeHolder2.get() + " " + placeHolder3.get())
    Country = placeHolder4.get()
    info = ("\n\tNew Student Information\n\nName : " + Name + "\nDate Of Birth : " + DOB + "\nCountry : " + Country + "\nEmaiil Address : " + emailAdd)
    print(info)
    exit()

#writes information to a text file
def print2():
    #creating and opening a new write to txt file
    NewFile = open("Registration.txt","w")
    
    #get all the information and organise it
    Name = fullName.get()
    emailAdd = email.get()
    DOB = (placeHolder1.get() + " " + placeHolder2.get() + " " + placeHolder3.get())
    Country = placeHolder4.get()
    info = ("\n\t\t*** New Student Information ***\n\nStudent Name : " + Name + "\nStudent Date Of Birth : " + DOB + "\nStudent Country Of Birth : " + Country + "\nStudent Email Address : " + emailAdd + "\n\n\t\tSuccessfuly Registered For Exams")
    
    #write information to document
    NewFile.write(info)
    #close file
    NewFile.close()
    exit()

#---------------------------------------------------------------------------------------------------------------------------
#add a label to the (window, text displayed in label, foreground(text color), background, relief is the border, font settings(type, size, costomize)) and finally placing it 
label1 = Label(window, text = "   Exam Registration   ", fg = "white", bg = "black", relief = "solid", font = ("arial", 40, "bold"))
#you can use .place(x, y) or .pack(fill = BOTH, padx = 2, pady = 2) at the end for example below
#label1.place(x = 40, y = 10)
#you can also use .grid(row = 50, colum = 50) but we'll use pack for now
label1.pack(fill = BOTH, padx = 15, pady = 1)

label2 = Label(window, text = "   Please Enter Required Information   ", width = 30, font = ("arial", 16, "bold"))
label2.pack(fill = BOTH, padx = 0, pady = 15)

#---------------------------------------------------------------------------------------------------------------------------
label3 = Label(window, text = "   Full Name :  ", font = ("arial", 12))
label3.place(x = 10, y = 270)

#create string variable fullName then creat textbox and config before placing
fullName = StringVar()
textBox1 = Entry(window, textvar = fullName)
textBox1.config(width = 30)
textBox1.place(x = 130, y = 270)

#---------------------------------------------------------------------------------------------------------------------------
label4 = Label(window, text = "   Email :  ", font = ("arial", 12))
label4.place(x = 10, y = 320)

email = StringVar()
textBox2 = Entry(window, textvar = email)
textBox2.config(width = 30)
textBox2.place(x = 130, y = 320)

#---------------------------------------------------------------------------------------------------------------------------
label5 = Label(window, text = "   D.O.B :  ", font = ("arial", 12))
label5.place(x = 340, y = 270)

#drop box menu
placeHolder1 = StringVar()
days = ['1','2','3','4','5','6','7','8','9','10','11']
placeHolder1.set("Day")
dropBox = OptionMenu(window, placeHolder1, *days)
dropBox.place(x = 450, y = 270)

placeHolder2 = StringVar()
months = ['January', 'Febuary', 'March', 'April', 'May']
placeHolder2.set("Month")
dropBox = OptionMenu(window, placeHolder2, *months)
dropBox.place(x = 515, y = 270)

placeHolder3 = StringVar()
years = ['1970', '1971', '1980', '1990', '1997', '1999', '2000', '2010', '2019']
placeHolder3.set("Year")
dropBox = OptionMenu(window, placeHolder3, *years)
dropBox.place(x = 595, y = 270)

#---------------------------------------------------------------------------------------------------------------------------
label6 = Label(window, text = "   Country :  ", font = ("arial", 12))
label6.place(x = 340, y = 320)

#drop box menu creation
placeHolder4 = StringVar()
countries = ['South Africa', 'Zimbabwe', 'Botswana', 'Not In Africa']
placeHolder4.set("Select Country")
dropBox = OptionMenu(window, placeHolder4, *countries)
dropBox.config(width = 30)
dropBox.place(x = 450, y = 320)

#---------------------------------------------------------------------------------------------------------------------------
#add a button using the same styling options        #relief options = ridge , groove , sunken , raised , solid      #command makes the button do something
button1 = Button(window, text = "   Submit   ", fg = "black", bg = "grey", relief = "raised", font = ("arial", 12, "bold"), command = print2)
button1.place(x = 400, y = 450)

button2 = Button(window, text = "   Cancel   ", fg = "black", bg = "grey", relief = "raised", font = ("arial", 12, "bold"), command = exit1)
button2.place(x = 200, y = 450)

#---------------------------------------------------------------------------------------------------------------------------
#display window
window.mainloop()