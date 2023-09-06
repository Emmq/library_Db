from tkinter import *
import sqlite3

root = Tk()
root.title("Database with Sqlite")
root.geometry('450x400')

# to create or connect to an exiting database
dbconnect = sqlite3.connect('address_book.db')



    #create a cursor
c = dbconnect.cursor()

#create a cursor
c = dbconnect.cursor()
#create table
'''
c.execute("""CREATE TABLE addresses (
          firs_name text,
          last_name text,
          address text,
          city text,
          state text,
          zipcode integer
        )""")
'''

def update_table():
    update = Tk()
    update.title("Database with Sqlite")
    root.geometry('450x400')

    # to create or connect to an exiting database
    dbconnect = sqlite3.connect('address_book.db')

    #create a cursor
    c = dbconnect.cursor()


    def update_func():
        
        # to create or connect to an exiting database
        dbconnect = sqlite3.connect('address_book.db')

        #create a cursor
        c = dbconnect.cursor()

        label_fnameupdate= Label(root, text="First Name").grid(row="0", column="0", pady=(10, 0))
        f_nameupdate= Entry(root, width="30")
        f_nameupdate.grid(row="0", column="1",padx="20", pady=(10, 0))

        label_lnameupdate= Label(root, text="Last Name").grid(row="1", column="0")
        l_nameupdate= Entry(root, width="30")
        l_nameupdate.grid(row="1", column="1",padx="20")

        label_addressupdate= Label(root, text="Address").grid(row="2", column="0")
        addressupdate= Entry(root, width="30")
        addressupdate.grid(row="2", column="1",padx="20")

        label_cityupdate= Label(root, text="City").grid(row="3", column="0")
        cityupdate= Entry(root, width="30")
        cityupdate.grid(row="3", column="1",padx="20")

        labelupdate_state= Label(root, text=" State").grid(row="4", column="0")
        stateupdate= Entry(root, width="30")
        stateupdate.grid(row="4", column="1",padx="20")

        label_zipcodeupdate= Label(root, text="Zipcode").grid(row="5", column="0")
        zipcodeupdate= Entry(root, width="30")
        zipcodeupdate.grid(row="5", column="1", padx="20")

        c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address,  :city, :state, :zipcode)",
                {
                    'f_name': f_nameupdate.get(),
                    'l_name': l_nameupdate.get(),
                    'address': addressupdate.get(),
                    'city': cityupdate.get(),
                    'state': stateupdate.get(),
                    'zipcode': label_zipcodeupdate.get()
                })
    
        # to commit changes
        dbconnect.commit()

        # to close connection
        dbconnect.close() 

        #select
    def select():
    # to create or connect to an exiting database
        dbconnect = sqlite3.connect('address_book.db')

        #create a cursor
        c = dbconnect.cursor()

        c.execute("SELECT*,oid from addresses WHERE oid = " + label_id.get())
        records = c.fetchall()
        #print(records)
        print_record = ""

        for record in records:
            print_record += str(record[6])+". "+str(record[0]) + '\n'

        record_label = Label(update, text=print_record)
        record_label.grid(row="4", column="0", columnspan=2)

        # to commit changes
        dbconnect.commit()

        # to close connection
        dbconnect.close()
        label_id.delete(0, END)

    #delete function
    def delete():
        # to create or connect to an exiting database
        dbconnect = sqlite3.connect('address_book.db')

        #create a cursor
        c = dbconnect.cursor()

        c.execute("DELETE from addresses WHERE oid = " + label_id.get())

        # to commit changes
        dbconnect.commit()

        # to close connection
        dbconnect.close()
        label_id.delete(0, END)


    #c.execute(""" UPDATE*,oid from addresses WHERE oid = " + label_id.get()""")
    label_id= Label(update, text="Record ID").grid(row="0", column="0")
    label_id = Entry(update, width="30")
    label_id.grid(row="0", column="1", padx="20")
    #select button
    select_button = Button (update, text = "Select record", command=select)
    select_button.grid(row="1", column="0", padx="10", pady="10", ipadx="50")

    #delete button
    delete_button = Button (update, text = "Delete record", command=delete)
    delete_button.grid(row="2", column="0", padx="10", pady="10", ipadx="50")

    #update button
    update_button = Button (update, text = "update record", command=update_func)
    update_button.grid(row="3", column="0", columnspan="2", padx="10", pady="10", ipadx="100")

  # to commit changes
    dbconnect.commit()

    # to close connection
    dbconnect.close()
    label_id.delete(0, END)
    update.mainloop()
    


def submit():
    
    # to create or connect to an exiting database
    dbconnect = sqlite3.connect('address_book.db')

    #create a cursor
    c = dbconnect.cursor()

    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address,  :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })
   
    # to commit changes
    dbconnect.commit()

    # to close connection
    dbconnect.close() 

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


#creating query function
def query():
  # to create or connect to an exiting database
  dbconnect = sqlite3.connect('address_book.db')

  #create a cursor
  c = dbconnect.cursor()

  c.execute("SELECT *, oid FROM addresses")
  records = c.fetchall()
  #print(records)
  print_record = ""

  for record in records:
     print_record += str(record[6])+". "+str(record[0]) + '\n'

  record_label = Label(root, text=print_record)
  record_label.grid(row="11", column="0", columnspan=2)


  # to commit changes
  dbconnect.commit()

  # to close connection
  dbconnect.close()

#create label and boxes
label_fname= Label(root, text="First Name").grid(row="0", column="0", pady=(10, 0))
f_name= Entry(root, width="30")
f_name.grid(row="0", column="1",padx="20", pady=(10, 0))

label_lname= Label(root, text="Last Name").grid(row="1", column="0")
l_name= Entry(root, width="30")
l_name.grid(row="1", column="1",padx="20")

label_address= Label(root, text="Address").grid(row="2", column="0")
address= Entry(root, width="30")
address.grid(row="2", column="1",padx="20")

label_city= Label(root, text="City").grid(row="3", column="0")
city= Entry(root, width="30")
city.grid(row="3", column="1",padx="20")

label_state= Label(root, text=" State").grid(row="4", column="0")
state= Entry(root, width="30")
state.grid(row="4", column="1",padx="20")

label_zipcode= Label(root, text="Zipcode").grid(row="5", column="0")
zipcode= Entry(root, width="30")
zipcode.grid(row="5", column="1", padx="20")


#create a submit button
submit_button = Button (root, text = "Add records", command=submit)
submit_button.grid(row="6", column="0", columnspan="2", padx="10", pady="10", ipadx="100")

#query button
query_button = Button (root, text = "show records", command=query)
query_button.grid(row="7", column="0", columnspan="2", padx="10", pady="10", ipadx="100")


#update button
update_button = Button (root, text = "update record", command=update_table)
update_button.grid(row="10", column="0", columnspan="2", padx="10", pady="10", ipadx="100")

# to commit changes
dbconnect.commit()

# to close connection
dbconnect.close()



root.mainloop()
