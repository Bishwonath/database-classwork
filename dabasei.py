from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("address_book.db")

c = conn.cursor()

# c.execute(""" CREATE TABLE addresses(
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer
# )""")

# print("Table created succesfully")

win = Tk()
win.title("Database Address Book")

def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zipcode':zipcode.get()
    })
    
    messagebox.showinfo("Address","Inserted Successfully")
    conn.commit()

    conn.close()

def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM addresses")

    records = c.fetchall()
    print(records)

    print_record=''
    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + '\n'
    
    query_label = Label(win, text = print_record)
    query_label.grid(row = 8, column=0, columnspan=2)

    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    records = c.fetchall()
    print(records)

    print_record=''
    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + '\n'
    
    query_label = Label(win, text = print_record)
    query_label.grid(row = 8, column=0, columnspan=2)

    conn.commit()
    conn.close()





f_name = Entry(win,width=30)
f_name.grid(row = 0, column =1, padx = 20)

l_name = Entry(win,width=30)
l_name.grid(row = 1, column =1)

address =  Entry(win, width=30)
address.grid(row=2, column = 1)

city =  Entry(win, width=30)
city.grid(row=3, column = 1)

state =  Entry(win, width=30)
state.grid(row=4, column = 1)

zipcode =  Entry(win, width=30)
zipcode.grid(row=5, column = 1)

delete_box = Entry(win, width = 30)
delete_box.grid(row = 9, column = 1, pady = 5)

f_name1 = Label(win,text = "First Name")
f_name1.grid(row = 0, column =0)

l_name1 = Label(win,text = "Last Name")
l_name1.grid(row = 1, column = 0)

address1 =  Label(win,text = "Address")
address1.grid(row=2, column = 0)

city1 =  Label(win, text = "City")
city1.grid(row=3, column = 0)

state1 =  Label(win, text = "State")
state1.grid(row=4, column = 0)

zipcode1 =  Label(win, text = "ZipCode")
zipcode1.grid(row=5, column = 0)

submit_btn1 = Button(win, text = "Add Records", command = submit)
submit_btn1.grid(row = 6, column = 0, columnspan=2, padx=10, pady=10,ipadx= 100)

# query_btn = Button(win, text = "Show Records",command = query)
# query_btn.grid(row = 7, column = 0, columnspan=2, padx=10, pady=10,ipadx= 100)

delete_btn = Button(win, text = "Delete")
delete_btn.grid(row = 10, column = 0, columnspan=2, padx=10, pady=10,ipadx= 120)

edit_btn = Button(win, text = "Update")
edit_btn.grid(row = 11, column = 0, columnspan=2, padx=10, pady=10,ipadx= 120)

conn.commit()

conn.close()

win.mainloop()