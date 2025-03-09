import tkinter as tk
import cx_Oracle
import webbrowser

def insert_data():
   # Get user input
    challan_id = challan_id_entry.get()
    reg_number = reg_number_entry.get()
    license_number = license_entry.get()
    date_and_time = date_time_entry.get()
    location = location_entry.get()
    offence_type = offence_entry.get()

    # Database connection
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xepdb1') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    connection = cx_Oracle.connect(user=r'system', password='-', dsn=dsn_tns)
    cursor = connection.cursor()

    # Insert data into the database
    query = "INSERT INTO challan (challan_id, reg_number, license_number, date_and_time, location, offence_type) VALUES (:1, :2, :3, :4, :5, :6)"
    cursor.execute(query, (challan_id, reg_number, license_number, date_and_time, location, offence_type))
    connection.commit()

    cursor.close()
    connection.close()

    # Display success message
    result_label.config(text="Data inserted successfully!")

def view_data_by_registration_number():
   # Get user input
    reg_number = reg_number_view_entry.get()

    # Database connection
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xepdb1') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    connection = cx_Oracle.connect(user=r'system', password='-', dsn=dsn_tns)
    cursor = connection.cursor()

    # Query data by registration number
    query = f"SELECT * FROM challan WHERE reg_number = '{reg_number}'"
    cursor.execute(query)
    data = cursor.fetchall()

    # Display data in a text box
    display_text.delete(1.0, tk.END)  # Clear previous data
    for row in data:
        display_text.insert(tk.END, str(row) + '\n')

    cursor.close()
    connection.close()
    
def view_data_by_challan_status(status):
    # Database connection
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xepdb1')
    connection = cx_Oracle.connect(user=r'system', password='-', dsn=dsn_tns)
    cursor = connection.cursor()

    # Query data based on challan status
    if status == "filled":
        query = "SELECT * FROM challan WHERE license_number IS NOT NULL"
    elif status == "not_filled":
        query = "SELECT * FROM challan WHERE license_number IS NULL"
    else:
        raise ValueError("Invalid status")

    cursor.execute(query)
    data = cursor.fetchall()

    # Display data in a text box
    display_text.delete(1.0, tk.END)  # Clear previous data
    for row in data:
        display_text.insert(tk.END, str(row) + '\n')

    cursor.close()
    connection.close()

def open_website():
    # Database connection
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xepdb1')
    connection = cx_Oracle.connect(user=r'system', password='-', dsn=dsn_tns)
    cursor = connection.cursor()

    # Query all data
    query = "SELECT * FROM challan"
    cursor.execute(query)
    data = cursor.fetchall()

    # Generate HTML content for the webpage
    html_content = "<html><head><title>Challan Data</title></head><body><table border='1'><tr><th>Challan ID</th><th>Registration Number</th><th>License Number</th><th>Date and Time</th><th>Location</th><th>Offence Type</th></tr>"
    for row in data:
        html_content += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td></tr>"
    html_content += "</table></body></html>"

    # Save HTML content to a file
    with open("challan_data.html", "w") as html_file:
        html_file.write(html_content)

    cursor.close()
    connection.close()

    # Open the generated HTML file in the default web browser
    webbrowser.open("challan_data.html")

# Creating the Tkinter window
root = tk.Tk()
root.title("Traffic Challan Management System")
root.geometry("600x600")  # Set window size

# Style for heading
heading_style = ("Helvetica", 16, "bold")

# Heading label
heading_label = tk.Label(root, text="TRAFFIC CHALLAN MANAGEMENT SYSTEM", font=("Helvetica", 20, "bold"), bg="black", fg="white")
heading_label.pack(fill="x", pady=10)  # fill="x" stretches the label across the window width, pady adds some vertical padding

# Labels and entry fields for data insertion
challan_id_label = tk.Label(root, text="Challan ID:", font=heading_style, bg="white", fg="black")
challan_id_label.pack()
challan_id_entry = tk.Entry(root, bg="dark grey", fg="white")
challan_id_entry.pack()

reg_number_label = tk.Label(root, text="Registration Number:")
reg_number_label.pack()
reg_number_entry = tk.Entry(root)
reg_number_entry.pack()

license_label = tk.Label(root, text="License Number:")
license_label.pack()
license_entry = tk.Entry(root)
license_entry.pack()

date_time_label = tk.Label(root, text="Date and Time:")
date_time_label.pack()
date_time_entry = tk.Entry(root)
date_time_entry.pack()

location_label = tk.Label(root, text="Location:")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

offence_label = tk.Label(root, text="Offence Type:")
offence_label.pack()
offence_entry = tk.Entry(root)
offence_entry.pack()

insert_button = tk.Button(root, text="Insert Data", command=insert_data)
insert_button.pack()

result_label = tk.Label(root, text="", font=heading_style)
result_label.pack()

# Labels and entry fields for data viewing
reg_number_view_label = tk.Label(root, text="Enter Registration Number to View Challans:", font=heading_style)
reg_number_view_label.pack()
reg_number_view_entry = tk.Entry(root)
reg_number_view_entry.pack()

view_button = tk.Button(root, text="View by Registration Number", command=view_data_by_registration_number)
view_button.pack()

# Buttons for arranging the table based on challan status
arrange_label = tk.Label(root, text="Arrange Table by Challan Status:", font=heading_style)
arrange_label.pack()

filled_button = tk.Button(root, text="Filled", command=lambda: view_data_by_challan_status("filled"))
filled_button.pack()

not_filled_button = tk.Button(root, text="Not Filled", command=lambda: view_data_by_challan_status("not_filled"))
not_filled_button.pack()


# Button to open the website with all entered data
open_website_button = tk.Button(root, text="Open Website with Challan Data", command=open_website)
open_website_button.pack()

# Display area for fetched data
display_text = tk.Text(root, height=20, width=50, bg="dark grey", fg="black")
display_text.pack()

# Configure background color
root.configure(bg="black")

root.mainloop()