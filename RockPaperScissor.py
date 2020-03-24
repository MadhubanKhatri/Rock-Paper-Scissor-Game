from tkinter import *
from random import choice
root = Tk()
root.geometry("400x300")
root.title("Rock-Paper-Scissor")

def rock():
    userChoice["text"] = "User choice is: Rock"

    com_list = ["Rock", "Paper", "Scissor","Rock", "Paper", "Scissor"]
    com_list_choice = choice(com_list)
    comChoice["text"] = f"Computer choice is: {com_list_choice}"

    rock_btn["state"] = "disabled"
    paper_btn["state"] = "disabled"
    scissor_btn["state"] = "disabled"

    if com_list_choice == "Paper":
        msg["text"] = "Computer wins"
    if com_list_choice == "Scissor":
        msg["text"] = "User wins"
    if com_list_choice == "Rock":
        msg["text"] = "It is Draw"

def paper():
    userChoice["text"] = "User choice is: Paper"

    com_list = ["Rock", "Paper", "Scissor"]
    com_list_choice = choice(com_list)
    comChoice["text"] = f"Computer choice is: {com_list_choice}"

    rock_btn["state"] = "disabled"
    paper_btn["state"] = "disabled"
    scissor_btn["state"] = "disabled"

    if com_list_choice == "Paper":
        msg["text"] = "It is Draw"
    if com_list_choice == "Scissor":
        msg["text"] = "Computer wins"
    if com_list_choice == "Rock":
        msg["text"] = "User wins"

def scissor():
    userChoice["text"] = "User choice is: Scissor"

    com_list = ["Rock", "Paper", "Scissor"]
    com_list_choice = choice(com_list)
    comChoice["text"] = f"Computer choice is: {com_list_choice}"

    rock_btn["state"] = "disabled"
    paper_btn["state"] = "disabled"
    scissor_btn["state"] = "disabled"

    if com_list_choice == "Paper":
        msg["text"] = "User wins"
    if com_list_choice == "Scissor":
        msg["text"] = "It is Draw"
    if com_list_choice == "Rock":
        msg["text"] = "Computer wins"

def active():
    rock_btn["state"] = "normal"
    paper_btn["state"] = "normal"
    scissor_btn["state"] = "normal"
    userChoice["text"] = ""
    comChoice["text"] = ""
    msg["text"] = ""

userChoice = Label(root, text="")
userChoice.pack()



rock_btn = Button(root, text="Rock",width=50,height=2,relief=RIDGE,font=("bold"), command=rock)
rock_btn.pack()

paper_btn = Button(root, text="Paper",width=50,height=2,relief=RIDGE,font=("bold"), command=paper)
paper_btn.pack()

scissor_btn = Button(root, text="Scissor",width=50,height=2,relief=RIDGE,font=("bold"), command=scissor)
scissor_btn.pack()

comChoice = Label(root,text="")
comChoice.pack()

msg  = Label(root,text="", font=("Helvetica", 17, "bold"))
msg.pack()


active_btn = Button(root, text="Play Agian",bg="black",fg="white",
                    width=50,height=2,relief=RIDGE,font=("bold"),command=active)
active_btn.pack()

root.mainloop()