#import necessary packages
import os
from tkinter import *
from tkinter.font import BOLD, ITALIC
#from tkinter import filedialog

#def main_account_screen():
main_screen = Tk()   # create a GUI window 
main_screen.geometry("770x550") # set the configuration of GUI window 
main_screen.title("VRPlot") # set the title of GUI window
main_screen.iconbitmap('vrt.ico') # set the icon of GUI window
dark_brown = '#940506' # color hashcode
light_green= '#90EE95' # color hashcode


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(main_screen)
    user_not_found_screen.title("Warning!")
    user_not_found_screen.iconbitmap('vrt.ico')
    user_not_found_screen.geometry("300x100")
    Label(user_not_found_screen, text="Enter Username First!!!",bg='black',fg='red', width="300", height="2", font=("Calibri", 15, ITALIC)).pack()
    Button(user_not_found_screen, text="OK",width="10",height='1', command=delete_user_not_found_screen).pack(pady=10)

def delete_user_not_found_screen():
    user_not_found_screen.destroy()
def clear_text():
    username_entry.delete(0, 'end')

def userDetails():
    global username
    flag = True
    if len(username.get()) == 0 or username.get() == 'Enter Username:- ':
        user_not_found()
        flag=False
    else:
        import datetime
        time = datetime.datetime.now()
        time = time.strftime('%d-%m-%Y-%H:%M:%S')
        with open('image_name.txt','w+')as f:
            f.write('#'*100)
            f.write('\n')
            f.write('Username: {}, Time {}'.format(username.get(),time))
            f.write('\n')
            f.write('#'*100)
            f.write('\n')
    return flag

def openNewWindow():
    try:
        if userDetails() is True:
            clear_text()
            import cord_labeler
            del cord_labeler
        else:
            pass
    except:
        pass

# call function when we click on entry box
def click(*args):
    username_entry.delete(0, 'end')

# call function when we leave entry box
def leave(*args):
    #username_entry.delete(0, 'end')
    username_entry.insert(0, 'Enter Username:- ')
    main_screen.focus()

# create a Form label 
Label(text="Enter Your Name and Select Image", bg=dark_brown,fg='white', width="700", height="2", font=("Calibri", 30)).pack() 

# Set text variables
username = StringVar()
# Set username label
username_lable = Label(main_screen, text="Username",width="300", height="3",font=("Calibri", 25) )
username_lable.pack()
# Set username entry
# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

username_entry = Entry(main_screen, textvariable=username, width="50")
username_entry.pack(ipady=10)
 
# create a register button

button1 = Button(text="Select Image", bg=dark_brown,fg='white', borderwidth=1, height="2", width="30",command=openNewWindow).pack(padx=10,pady=100)


# Use bind method
username_entry.bind("<Button-1>", click)
username_entry.bind("<Leave>", leave)
#main_account_screen() # call the main_account_screen() function
main_screen.mainloop() # start the GUI


 
 
