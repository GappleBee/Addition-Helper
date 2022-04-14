def Submit():  # Function for submitting the user's answer
    answer = entryBox.get()
    if num + num2 == int(answer):
        picture = PhotoImage(
            file="C:/Users/User/Documents/Coding Documents/Images For Programming/Tick.ppm"  # IMPORTANT: Change this directory to wherever you're storing the "Tick.ppm" file otherwise the program will not work properly
        )
        pictureBox.image = picture
    else:
        picture = PhotoImage(
            file="C:/Users/User/Documents/Coding Documents/Images For Programming/Cross.ppm"  # IMPORTANT: Change this directory to wherever you're storing the "Cross.ppm" file otherwise the program will not work properly
        )
        pictureBox.image = picture
    pictureBox["image"] = picture
    pictureBox.update()


def Next():  # Function for going to the next question (and resetting the image to nothing)
    global num
    global num2
    num = random.randint(10, 50)
    num2 = random.randint(10, 50)
    label["text"] = "Add " + str(num) + " and " + str(num2) + " together"

    picture = PhotoImage(file="")
    pictureBox.image = picture
    pictureBox["image"] = picture
    pictureBox.update()


# Setting up the window
window = Tk()
window.title("Addition Helper")
window.geometry("600x400")
window.wm_iconbitmap(
    "C:/Users/User/Documents/Coding Documents/Images For Programming/Plus Sign.ico"
)

# Getting the two numbers to get the user to add together
num = random.randint(10, 50)
num2 = random.randint(10, 50)

# Setting up the suitable buttons and messages
label = Label(window, text="Add " + str(num) + " and " + str(num2) + " together")
label.pack()

entryBox = Entry(window, text="")
entryBox.pack()

button = Button(window, text="Submit Answer", command=Submit)
button.pack()

button2 = Button(window, text="Next Question", command=Next)
button2.pack()

# Setting up the 'picture box' so that the 'picture box' can be changed depending on the user's answer rather than adding to the end of another image
picture = PhotoImage(file="")
pictureBox = Label(window, image=picture)
pictureBox.image = picture
pictureBox.pack()

window.mainloop()
