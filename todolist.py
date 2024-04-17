from tkinter import *

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry('650x410+300+150')  # Corrected typo

        self.label = Label(self.root, text='To-Do List App',  # Corrected class name
            font='arial 25 bold', width=10, bd=5, bg='pink', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='add task!',  # Corrected class name
            font='arial 18 bold', width=10, bd=5, bg='pink', fg='black')
        self.label2.place(x=40 , y=54)

        self.label3 = Label(self.root, text='task!',  # Corrected class name
            font='arial 18 bold', width=10, bd=5, bg='pink', fg='black')
        self.label3.place(x=320 , y=54)

        self.main_text = Listbox(self.root, height='9', font='arial 20 italic bold')
        self.main_text.place(x=280, y=100)
        
        self.text = Text(self.root, bd =5,height=2,width=30,font = "ariel, 10 bold")
        self.text.place(x=20 , y=120)
        #=================ADDTASK function===================#
        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END,content)
            with open ('data.txt',"w") as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0,END)

        #=================DELETE BUTTON function===================#
        def delete():
            delete_= self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open('data.txt','r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)

        with open("data.txt",'r') as file:
            read = file.readlines()
            for i in read:
               ready = i.split()
               self.main_text.insert(END, ready)
            file.close()

        #=================ADD BUTTON===================#
        self.button = Button(self.root,text = 'add',font = 'sarif, 20 italic',
                 width=10,bd=5,bg="pink",fg="black", command=add)
        self.button.place(x=30, y=180)

        #=================DELETE BUTTON===================#
        self.button2 = Button(self.root,text = 'delete',font = 'sarif, 20 italic',
                 width=10,bd=5,bg="pink",fg="black", command=delete)
        self.button2.place(x=30, y=260)

def main():
    root = Tk()  # Added missing import statement
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
