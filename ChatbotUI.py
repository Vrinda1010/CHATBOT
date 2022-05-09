from tkinter import *
from main1 import abc
from main1 import get_response

    
root =Tk()
root.title('Chat Bot')

root.geometry('400x500')
def send_message():
    chatWindow.delete(1.0,"end")
    chatWindow.insert(1.0,get_response(messageWindow.get(1.0,"end")))

main_menu= Menu(root)

file_menu = Menu(root)
file_menu.add_command(label='New')
file_menu.add_command(label='Save As')
file_menu.add_command(label='Exit')

main_menu.add_cascade(label='File', menu= file_menu)
main_menu.add_command(label="Edit")
main_menu.add_command(label="Quit")
root.config(menu=main_menu)

chatWindow= Text(root, bd=1,bg='gray', width=50,height=8)
chatWindow.place(x=6,y=6,height=385,width=370)

messageWindow= Text(root,bg='gray', width=30,height=4)
messageWindow.place(x=128,y=400, height= 88, width=260)

#def myClick():
    #myLabel=Label(root,text=e.get())
    #myLabel.pack()
    
#Button=Button(root,text="Enter your name:",activebackground='light blue',width=12,height=5,command= myClick)

Button= Button(root, text='Send',bg='blue',activebackground='light blue',width=12,height=5,command=send_message)
Button.place(x=6,y=400, height=88,width=120)



scrollbar=Scrollbar(root,command=chatWindow.yview())
scrollbar.place(x=375,y=5,height=385)
root.mainloop()
