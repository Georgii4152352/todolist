# -------------------Imports---------------------------
from tkinter import *
from tkinter import messagebox as mb,ttk
from tkcalendar import Calendar
import calendar
from db_service import DataBaseService
from task import Task
# -------------------Imports---------------------------

# ----------------tkinter configure--------------------
screen = Tk()
screen.title("To Do List")
screen.geometry("1000x800")

# ----------------tkinter configure--------------------

# -------------------Widgets---------------------------
l1 = Label(text='To-Do List', font="Arial, 20")
l2 = Label(text='Enter task title: ', font="Arial, 20")
e1 = Entry(width=18, font="Arial, 20")
t = Listbox(height=12, width=50, selectmode='SINGLE', bd=4, font="Arial, 15")
b1 = Button(text='Add task', width=20, font="Arial, 17", command=lambda:add_task())
b2 = Button(text='Delete', width=15, font="Arial, 15")
b3 = Button(text='Delete all', width=15, font="Arial, 15")
b4 = Button(text='Done', width=15, font="Arial, 15")
cal = Calendar(selectmode='day', font="Arial, 15")
b5 = Button(text='Sort', width=10, font="Arial, 15")
combo = ttk.Combobox(values=["title", "deadline", "status"], font=("Arial", 15), width=10,state="readonly")
combo.current(0)
# -------------------Widgets---------------------------

# ----------------Place geometry-----------------------
l1.place(x=450, y=10)
l2.place(x=200, y=130)
e1.place(x=150, y=180)
b1.place(x=150, y=230)
b2.place(x=630, y=700)
b3.place(x=250, y=700)
b4.place(x=50, y=500)
cal.place(x=550, y=100)
t.place(x=250, y=400)
combo.place(x=820, y=500)
b5.place(x=820, y=550)
# ----------------Place geometry-----------------------

# -------------Functions and Variables-----------------
task_list = []
db = DataBaseService()
word_for_sort = combo.get()
def add_task():
    title = e1.get()
    deadline = cal.selection_get()
    if len(title) == 0:
        mb.showwarning("Empty entry", "Enter the task name")
    else:
        item = Task(title, deadline, False)
        task_list.append(item)
        db.insert_value(title, deadline, False)
        e1.delete(0, "end")
        list_update()
def date_transform(day, month, year):
    return f"{day},{calendar.month_name[month]},{year}"

def list_update():
    task_list.clear()
    for element in db.select_value(word_for_sort):
        item = Task(element[0], element[1],element[2])
        task_list.append(item)
    clear_list()
    for i in task_list:
        date = i.deadline
        title = i.title
        status = i.status
        row = f"{title} | {date_transform(date.day,date.month,date.year)} | {status}"
        t.insert("end",row)

def del_all():
    ask = mb.askyesno("Delete all", "Are you sure?")
    if ask:
        task_list.clear()
        db.delete_all()
        list_update()



def iter_parse_text(arg):
    index = t.curselection()[0]
    item = task_list[index]
    if arg == "delete":
        db.delete_one(item.title,item.deadline)
        task_list.remove(item)
    list_update()





def clear_list():
    t.delete(0,"end")

# -------------Functions and Variables-----------------

try:
    list_update()
except TypeError:
    print("List is empty")
screen.mainloop()