import tkinter as tk
import cx_Oracle

def view_challan():
    # Get user input
    challan_id = challan_number_entry.get()
    license_number = license_plate_entry.get()

    # Database connection
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xepdb1') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    connection = cx_Oracle.connect(user=r'system', password='MAAmaa@1', dsn=dsn_tns)
    cursor = connection.cursor()

    # Create and execute SQL query based on user input
    query = "SELECT * FROM challan WHERE 1=1"
    if challan_id:
        query += f" AND challan_id = '{challan_id}'"
    if license_number:
        query += f" AND license_number = '{license_number}'"

    cursor.execute(query)
    data = cursor.fetchall()

    # Display data in a text box
    display_text.delete(1.0, tk.END)  # Clear previous data
    for row in data:
        display_text.insert(tk.END, str(row) + '\n')

    cursor.close()
    connection.close()

# Creating the Tkinter window
root = tk.Tk()
root.title("Traffic Challan Management System")

# Labels and entry fields
challan_number_label = tk.Label(root, text="Challan id:")
challan_number_label.pack()
challan_number_entry = tk.Entry(root)
challan_number_entry.pack()

license_plate_label = tk.Label(root, text="License number:")
license_plate_label.pack()
license_plate_entry = tk.Entry(root)
license_plate_entry.pack()

view_button = tk.Button(root, text="View Challan", command=view_challan)
view_button.pack()

# Display area for fetched data
display_text = tk.Text(root, height=20, width=50)
display_text.pack()

root.mainloop()