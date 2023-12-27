from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

root = Tk()
root.state('zoomed')
root.title("Airport Management System")
root.config(bg='grey')
Label(root, text='Airport Management system', font='aerial 45 bold', bg='blue', fg='white').pack(fill=X)



def pd():
    if (
        e1.get() == "" or e2.get() == "" or e3.get() == "" or e4.get() == "" or e5.get() == ""
        or e6.get() == "" or e7.get() == "" or e9.get() == "" or e10.get() == "" or e11.get() == "" or e12.get() == "" or e13.get() == ""
        or e14.get() == "" or e15.get() == "" or e16.get() == "" or e17.get() == "" or e18.get() == "" or e19.get() == "" or e20.get() == "" or e21.get() == ""
    ):
        messagebox.showerror("Error", "All fields are required")
    else:
        con = mysql.connector.connect(
            host="localhost", username="root", password="Ganu#$0706", database='airport_management'
        )
        my_cursor = con.cursor()

        try:
            # Insert data into PASSENGER2
            my_cursor.execute(
                "INSERT INTO PASSENGER2 (PASSPORTNO, FNAME, MNAME, LNAME, ADDRESS, PHONE, AGE, SEX) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    PASSPORTNO.get(),
                    FNAME.get(),
                    MNAME.get(),
                    LNAME.get(),
                    ADDRESS.get(),
                    PHONE.get(),
                    AGE.get(),
                    SEX.get(),
                )
            )

            # Insert data into PASSENGER1
            my_cursor.execute("INSERT INTO PASSENGER1 (PASSPORTNO) VALUES (%s)", (PASSPORTNO.get(),))

            # Insert data into FLIGHT
            my_cursor.execute(
                "INSERT INTO FLIGHT (FLIGHT_CODE, SOURCE, DESTINATION, ARRIVAL, DEPARTURE, STATUS, DURATION, FLIGHTTYPE, AIRLINEID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    FLIGHT_CODE.get(),
                    SOURCE.get(),
                    DESTINATION.get(),
                    ARRIVAL.get(),
                    DEPARTURE.get(),
                    STATUS.get(),
                    DURATION.get(),
                    FLIGHTTYPE.get(),
                    AIRLINEID.get(),
                )
            )

            # Insert data into PASSENGER3
            my_cursor.execute("INSERT INTO PASSENGER3 (FLIGHT_CODE) VALUES (%s)", (FLIGHT_CODE.get(),))

            # Insert data into TICKET1
            date_of_booking_value = datetime.now().date()
            my_cursor.execute(
                "INSERT INTO TICKET1 (TICKET_NUMBER, SOURCE, DESTINATION, DATE_OF_BOOKING, DATE_OF_TRAVEL, SEATNO, CLASS, PASSPORTNO) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    TICKET_NUMBER.get(),
                    SOURCE.get(),
                    DESTINATION.get(),
                    date_of_booking_value,
                    DEPARTURE.get(),
                    SEATNO.get(),
                    CLASS.get(),
                    PASSPORTNO.get(),
                )
            )

            # Insert data into TICKET2
            my_cursor.execute(
                "INSERT INTO TICKET2 (DATE_OF_BOOKING, SOURCE, DESTINATION, CLASS, PRICE) VALUES (%s,%s,%s,%s,%s)",
                (
                    date_of_booking_value,
                    SOURCE.get(),
                    DESTINATION.get(),
                    CLASS.get(),
                    PRICE.get(),
                )
            )
            
            my_cursor.execute(
                "INSERT INTO SERVES (SSN, PASSPORTNO) VALUES (%s,%s)",
                (
                    SSN1.get(),
                    PASSPORTNO.get()
                )
            )

            # Commit the changes
            con.commit()
            fetch_data()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to insert data: {str(e)}")
            
            




# thiss fetch function also for the tree part dont change
def fetch_data():
    con = mysql.connector.connect(
        host="localhost", username="root", password="Ganu#$0706", database='airport_management'
    )
    my_cursor = con.cursor()
    my_cursor.execute('select * from PASSENGER2')
    rows = my_cursor.fetchall()
    if len(rows) != 0:
        table.delete(*table.get_children())
        for items in rows:
            table.insert('', END, values=items)
    con.commit()
    con.close()



         
def get_data(event=''):
    cursor_row = table.focus()
    data = table.item(cursor_row)
    row = data['values']
    if row and len(row) >= 9:
        PASSPORTNO.set(row[0])
        FNAME.set(row[1])
        MNAME.set(row[2])
        LNAME.set(row[3])
        ADDRESS.set(row[4])
        PHONE.set(row[5])
        AGE.set(row[6])
        SEX.set(row[7])



def delete():
    if e1.get() != "":
        # Delete passenger data
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Ganu#$0706", database='airport_management'
        )
        my_cursor = conn.cursor()

        my_cursor.execute("SELECT PID FROM PASSENGER1 WHERE PASSPORTNO = %s", (PASSPORTNO.get(),))
        pid_result = my_cursor.fetchone()

        if pid_result:
            pid = pid_result[0]

            querry_passenger2 = "DELETE FROM PASSENGER2 WHERE PASSPORTNO = %s"
            value_passenger2 = (PASSPORTNO.get(),)
            my_cursor.execute(querry_passenger2, value_passenger2)

            querry_passenger1 = "DELETE FROM PASSENGER1 WHERE PID = %s AND PASSPORTNO = %s"
            value_passenger1 = (pid, PASSPORTNO.get())
            my_cursor.execute(querry_passenger1, value_passenger1)

            conn.commit()
            conn.close()
            fetch_data()
            messagebox.showinfo("Deleted", "Passenger data has been deleted")
        else:
            messagebox.showerror("Error", "Passenger not found in PASSENGER1")
    elif e9.get() != "":
        
        # Delete flight data
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Ganu#$0706", database='airport_management'
        )
        my_cursor = conn.cursor()

        querry_flight = "DELETE FROM FLIGHT WHERE FLIGHT_CODE = %s"
        value_flight = (FLIGHT_CODE.get(),)
        my_cursor.execute(querry_flight, value_flight)

        querry_passenger3 = "DELETE FROM PASSENGER3 WHERE FLIGHT_CODE = %s"
        value_passenger3 = (FLIGHT_CODE.get(),)
        my_cursor.execute(querry_passenger3, value_passenger3)

        conn.commit()
        conn.close()
        messagebox.showinfo("Deleted", "Flight data has been deleted")
    else:
        messagebox.showerror("Error", "Please enter either PASSPORTNO or FLIGHT_CODE to delete")




# ... (previous code)

def open_employee_page():
    # Create a new window for employee information
    employee_window = Toplevel(root)
    employee_window.title("Employee Information")
    employee_window.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    employee_window.configure(bg='lightblue')
    # Add widgets and functionality for the employee page
    Label(employee_window, text="Employee Information", font='aerial 20 bold').pack()

    # Entry for Employee Name
    Label(employee_window, text='SSN', bg='white', font='aerial 15').place(x=10, y=100)
    Label(employee_window, text='FNAME', bg='white', font='aerial 15').place(x=10, y=140)
    Label(employee_window, text='MNAME', bg='white', font='aerial 15').place(x=10, y=180)
    Label(employee_window, text='LNAME', bg='white', font='aerial 15').place(x=10, y=220)
    Label(employee_window, text='ADDRESS', bg='white', font='aerial 15').place(x=10, y=260)
    Label(employee_window, text='PHONE', bg='white', font='aerial 15').place(x=10, y=300)
    Label(employee_window, text='AGE', bg='white', font='aerial 15').place(x=10, y=340)
    Label(employee_window, text='SEX', bg='white', font='aerial 15').place(x=10, y=380)
    Label(employee_window, text='JOBTYPE', bg='white', font='aerial 15').place(x=10, y=420)
    Label(employee_window, text='AP NAME', bg='white', font='aerial 15').place(x=10, y=460)

    SSN = StringVar()
    FNAME1 = StringVar()
    MNAME1 = StringVar()
    LNAME1 = StringVar()
    ADDRESS1 = StringVar()
    PHONE1 = StringVar()
    AGE1 = StringVar()
    SEX1 = StringVar()
    JOBTYPE = StringVar()
    AP_NAME = StringVar()

    e31 = Entry(employee_window, bd=4, textvariable=SSN)
    e31.place(x=130, y=95, width=200)
    e22 = Entry(employee_window, bd=4, textvariable=FNAME1)
    e22.place(x=130, y=135, width=200)
    e23 = Entry(employee_window, bd=4, textvariable=MNAME1)
    e23.place(x=130, y=175, width=200)
    e24 = Entry(employee_window, bd=4, textvariable=LNAME1)
    e24.place(x=130, y=215, width=200)
    e25 = Entry(employee_window, bd=4, textvariable=ADDRESS1)
    e25.place(x=130, y=255, width=200)
    e26 = Entry(employee_window, bd=4, textvariable=PHONE1)
    e26.place(x=130, y=295, width=200)
    e27 = Entry(employee_window, bd=4, textvariable=AGE1)
    e27.place(x=130, y=335, width=200)
    e28 = Entry(employee_window, bd=4, textvariable=SEX1)
    e28.place(x=130, y=375, width=200)
    e29 = Entry(employee_window, bd=4, textvariable=JOBTYPE)
    e29.place(x=130, y=415, width=200)
    e30 = Entry(employee_window, bd=4, textvariable=AP_NAME)
    e30.place(x=130, y=455, width=200)

    
    def save_employee_data():
        # Retrieve values from entry widgets
        ssn = SSN.get()
        fname2 = FNAME1.get()
        mname2 = MNAME1.get()
        lname2 = LNAME1.get()
        address2 = ADDRESS1.get()
        phone2 = PHONE1.get()
        age2 = AGE1.get()
        sex2 = SEX1.get()
        jobtype = JOBTYPE.get()
        ap_name = AP_NAME.get()

        # Insert data into EMPLOYEE1
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Ganu#$0706", database='airport_management'
        )
        my_cursor = conn.cursor()

        try:
            my_cursor.execute(
                "INSERT INTO EMPLOYEE1 (SSN, FNAME, MNAME, LNAME, ADDRESS, PHONE, AGE, SEX, JOBTYPE, AP_NAME) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (ssn, fname2, mname2, lname2, address2, phone2, age2, sex2, jobtype, ap_name)
            )

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Employee data has been saved")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save employee data: {str(e)}")
            
            
    save_employee_btn = Button(employee_window, text='Save Employee Data', font='ariel 20 bold', bg='black', fg='green', bd=5, cursor='hand2', command=save_employee_data)
    save_employee_btn.place(x=130, y=550, width=200)    


employee_btn = Button(root, text='Employee Page', font='ariel 20 bold', bg='black', fg='green', bd=5, cursor='hand2', command=open_employee_page)
employee_btn.place(x=0, y=0, width=350)

    


def clear():
    PASSPORTNO.set('')
    FNAME.set('')
    MNAME.set('')
    LNAME.set('')
    ADDRESS.set('')
    PHONE.set('')
    AGE.set('')
    SEX.set('')
    FLIGHT_CODE.set('')
    SOURCE.set('')
    DESTINATION.set('')
    ARRIVAL.set('')
    DEPARTURE.set('')
    STATUS.set('')
    DURATION.set('')
    FLIGHTTYPE.set('')
    AIRLINEID.set('')
    TICKET_NUMBER.set('')
    SEATNO.set('')
    CLASS.set('')
    PRICE.set('')
    SSN1.set('')


def ext():
    confirm = messagebox.askyesno('confirmation', "are you sure you want to exit?")
    if confirm > 0:
        root.destroy()
        return

# Labeling part from here

frame1 = Frame(root, bd=15, relief=RIDGE)
frame1.place(x=0, y=54, width=1440, height=650)

label_fr1 = LabelFrame(frame1, text='Passenger Information', font='ariel 20 bold', bd=10, bg='white')
label_fr1.place(x=0, y=0, width=1420, height=360)

# For frame  labels at Top

Label(label_fr1, text='PASSPORTNO', bg='white', font='aerial 15').place(x=5, y=10)
Label(label_fr1, text='FNAME', bg='white', font='aerial 15').place(x=5, y=50)
Label(label_fr1, text='MNAME', bg='white', font='aerial 15').place(x=5, y=90)
Label(label_fr1, text='LNAME', bg='white', font='aerial 15').place(x=5, y=130)
Label(label_fr1, text='ADDRESS', bg='white', font='aerial 15').place(x=5, y=170)
Label(label_fr1, text='PHONE', bg='white', font='aerial 15').place(x=5, y=210)
Label(label_fr1, text='AGE', bg='white', font='aerial 15').place(x=5, y=250)
Label(label_fr1, text='SEX(M/F)', bg='white', font='aerial 15').place(x=5, y=290)

PASSPORTNO = StringVar()
FNAME = StringVar()
MNAME = StringVar()
LNAME = StringVar()
ADDRESS = StringVar()
PHONE = StringVar()
AGE = StringVar()
SEX = StringVar()

# For Frame 1 at top

e1 = Entry(label_fr1, bd=4, textvariable=PASSPORTNO)
e1.place(x=130, y=10, width=200)
e2 = Entry(label_fr1, bd=4, textvariable=FNAME)
e2.place(x=130, y=50, width=200,)
e3 = Entry(label_fr1, bd=4, textvariable=MNAME)
e3.place(x=130, y=90, width=200)
e4 = Entry(label_fr1, bd=4, textvariable=LNAME)
e4.place(x=130, y=130, width=200)
e5 = Entry(label_fr1, bd=4, textvariable=ADDRESS)
e5.place(x=130, y=170, width=200)
e6 = Entry(label_fr1, bd=4, textvariable=PHONE)
e6.place(x=130, y=210, width=200)
e7 = Entry(label_fr1, bd=4, textvariable=AGE)
e7.place(x=130, y=250, width=200)
e8 = Entry(label_fr1, bd=4, textvariable=SEX)
e8.place(x=130, y=290, width=200)


# New Frame 2 (label) FOR TICKET

frame2 = Frame(root, bd=15, relief=RIDGE, bg='black')
frame2.place(x=0, y=670, width=1440, height=180)

label_fr2 = LabelFrame(frame1, text='Flight Information', font='ariel 20 bold', bd=10, bg='white')
label_fr2.place(x=0, y=355, width=1420, height=253)

# For frame label 2 at Mid
Label(label_fr2, text='FLIGHT_CODE', bg='white', font='aerial 15').place(x=5, y=10)
Label(label_fr2, text='SOURCE', bg='white', font='aerial 15').place(x=5, y=50)
Label(label_fr2, text='DESTINATION', bg='white', font='aerial 15').place(x=5, y=90)
Label(label_fr2, text='ARRIVAL', bg='white', font='aerial 15').place(x=5, y=130)
Label(label_fr2, text='DEPARTURE', bg='white', font='aerial 15').place(x=5, y=170)
Label(label_fr2, text='STATUS', bg='white', font='aerial 15').place(x=350, y=10)
Label(label_fr2, text='DURATION', bg='white', font='aerial 15').place(x=350, y=50)
Label(label_fr2, text='FLIGHTTYPE', bg='white', font='aerial 15').place(x=350, y=90)
Label(label_fr2, text='AIRLINEID', bg='white', font='aerial 15').place(x=350, y=130)

Label(label_fr2, text='TICKET_NUMBER', bg='white', font='aerial 15').place(x=700, y=10)
Label(label_fr2, text='SEATNO', bg='white', font='aerial 15').place(x=700, y=50)
Label(label_fr2, text='CLASS', bg='white', font='aerial 15').place(x=700, y=90)
Label(label_fr2, text='PRICE', bg='white', font='aerial 15').place(x=700, y=130)
Label(label_fr2, text='SSN', bg='white', font='aerial 15').place(x=700, y=170)
 
FLIGHT_CODE = StringVar()
SOURCE = StringVar()
DESTINATION = StringVar()
ARRIVAL = StringVar()
DEPARTURE = StringVar()
STATUS = StringVar()
DURATION = StringVar()
FLIGHTTYPE = StringVar()
AIRLINEID = StringVar()
TICKET_NUMBER= StringVar()
SEATNO= StringVar()
CLASS = StringVar()
PRICE = StringVar()
SSN1 = StringVar()

# For Frame 2 at Mid
e9 = Entry(label_fr2, bd=4, textvariable=FLIGHT_CODE)
e9.place(x=130, y=10, width=200)
e10 = Entry(label_fr2, bd=4, textvariable=SOURCE)
e10.place(x=130, y=50, width=200,)
e11 = Entry(label_fr2, bd=4, textvariable=DESTINATION)
e11.place(x=130, y=90, width=200)
e12 = Entry(label_fr2, bd=4, textvariable=ARRIVAL)
e12.place(x=130, y=130, width=200)
e13 = Entry(label_fr2, bd=4, textvariable=DEPARTURE)
e13.place(x=130, y=170, width=200)
e14 = Entry(label_fr2, bd=4, textvariable=STATUS)
e14.place(x=475, y=10, width=200)
e15 = Entry(label_fr2, bd=4, textvariable=DURATION)
e15.place(x=475, y=50, width=200)
e16 = Entry(label_fr2, bd=4, textvariable=FLIGHTTYPE)
e16.place(x=475, y=90, width=200)
e17 = Entry(label_fr2, bd=4, textvariable=AIRLINEID)
e17.place(x=475, y=130, width=200)
e18 = Entry(label_fr2, bd=4, textvariable=TICKET_NUMBER)
e18.place(x=850, y=10, width=200)
e19 = Entry(label_fr2, bd=4, textvariable=SEATNO)
e19.place(x=850, y=50, width=200)
e20 = Entry(label_fr2, bd=4, textvariable=CLASS)
e20.place(x=850, y=90, width=200)
e21 = Entry(label_fr2, bd=4, textvariable=PRICE)
e21.place(x=850, y=130, width=200)
e32 = Entry(label_fr2, bd=4, textvariable=SSN1)
e32.place(x=850, y=170, width=200)

d_btn = Button(root, text='Delete', font='ariel 20 bold', bg='red', fg='red', bd=5, cursor='hand2', command=delete)
d_btn.place(x=20, y=850, width=350)

pd_btn = Button(root, text='Save Data', font='ariel 20 bold', bg='black', fg='green', bd=5, cursor='hand2', command=pd)
pd_btn.place(x=370, y=850, width=350)

c_btn = Button(root, text='Clear', font='ariel 20 bold', bg='black', fg='green', bd=5, cursor='hand2', command=clear)
c_btn.place(x=720, y=850, width=350)

e_btn = Button(root, text='Exit', font='ariel 20 bold', bg='black', fg='red', bd=5, cursor='hand2', command=ext)
e_btn.place(x=1070, y=850, width=350)

scroll_x = ttk.Scrollbar(frame2, orient=HORIZONTAL)
scroll_x.pack(side="bottom", fill='x')

scroll_y = ttk.Scrollbar(frame2, orient=VERTICAL)
scroll_y.pack(side="right", fill='y')

# For Tree View Not Needed For Ticket(Neglet This)

table = ttk.Treeview(
    frame2,
    columns=('psn', 'fname', 'mname', 'lname', 'add', 'ph', 'age', 'sex'),
    xscrollcommand=scroll_y.set,
    yscrollcommand=scroll_x.set
)
scroll_x = ttk.Scrollbar(command=table.xview)
scroll_y = ttk.Scrollbar(command=table.yview)

table.heading('psn', text='PASSPORTNO')
table.heading('fname', text='FNAME')
table.heading('mname', text='MNAME')
table.heading('lname', text='LNAME')
table.heading('add', text='ADDRESS')
table.heading('ph', text='PHONE')
table.heading('age', text='AGE')
table.heading('sex', text='SEX')

table['show'] = 'headings'
table.pack(fill=BOTH, expand=1)
table.column('psn', width=130)
table.column('fname', width=80)
table.column('mname', width=80)
table.column('lname', width=80)
table.column('add', width=100)
table.column('ph', width=70)
table.column('age', width=30)
table.column('sex', width=30)

table.bind('<ButtonRelease-1>', get_data)
fetch_data()

root.mainloop()
