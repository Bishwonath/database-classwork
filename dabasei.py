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
    print('Deleted Successfully')

    # c.execute("SELECT *, oid FROM addresses")

    # records = c.fetchall()
    # print(records)

    # print_record=''
    # for record in records:
    #     print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + '\n'
    
    # query_label = Label(win, text = print_record)
    # query_label.grid(row = 8, column=0, columnspan=2)

    conn.commit()
    conn.close()

def update():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET
         first_name = :first,
         last_name = :address,
         address = :address,
         city = :city,
         state = :state,
         zipcode = :zipcode
         WHERE oid = :oid""",
         {'first': f_name_editor.get(),
         'last': l_name_editor.get(),
         'address': address_editor.get(),
         'city': city_editor.get(),
         'state':state_editor.get(),
         'zipcode':zipcode_editor.get(),
         'oid': record_id
          }
    )
    conn.commit()
    conn.close()
    editor.destroy()

def edit():

    global editor

    editor =Tk()
    editor.title('Update Data')

    editor.geometry('300x400')
    conn = sqlite3.connect('Address_Book.db')

    c = conn.cursor()
    
    record_id = delete_box.get()

    c.execute("SELECT * FROM addresses WHERE oid="+record_id)

    records = c.fetchall()
    print(records)

    #====Createing global variable for all text boxes===
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    #======Create text box=========
    f_name_editor = Entry(editor,width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1)

    address_editor = Entry(editor,width=30)
    address_editor.grid(row=2, column=1)

    city_editor = Entry(editor,width=30)
    city_editor.grid(row=3, column=1)

    state_editor = Entry(editor,width=30)
    state_editor.grid(row=4, column=1)

    zipcode_editor = Entry(editor,width=30)
    zipcode_editor.grid(row=5, column=1)


    #====Create textbox labels======
    f_name_label = Label(editor, text='First Name')
    f_name_label.grid(row=0, column=0, pady=(10, 0))

    l_name_label = Label(editor, text='Last Name')
    l_name_label.grid(row=1, column=0)

    address_label = Label(editor, text='Address')
    address_label.grid(row=2, column=0)

    city_label = Label(editor, text='City')
    city_label.grid(row=3, column=0)

    state_label = Label(editor, text='State')
    state_label.grid(row=4, column=0)

    zipcode_label = Label(editor, text='Zip Code')
    zipcode_label.grid(row=5,column=0)

    # ====loop through the results=====
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

        edit_btn = Button(editor,text='SAVE',command=update)
        edit_btn.grid(row=6,column=0, columnspan=2,pady=10,padx=10,ipadx=125)

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

query_btn = Button(win, text = "Show Records",command = query)
query_btn.grid(row = 7, column = 0, columnspan=2, padx=10, pady=10,ipadx= 100)

delete_btn = Button(win, text = "Delete",command=delete)
delete_btn.grid(row = 10, column = 0, columnspan=2, padx=10, pady=10,ipadx= 120)

edit_btn = Button(win, text = "Update",command=edit)
edit_btn.grid(row = 11, column = 0, columnspan=2, padx=10, pady=10,ipadx= 120)

delete_boxlabel=Label(win, text="Delete Id")
delete_boxlabel.grid(row = 9, column = 0)


conn.commit()

conn.close()

win.mainloop()