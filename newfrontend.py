import tkinter as tk
import cx_Oracle
from tkinter import messagebox

# Establishing a connection to the Oracle database
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xepdb1')
connection = cx_Oracle.connect(user='system', password='MAAmaa@1', dsn=dsn_tns)
cursor = connection.cursor()

# Function to view challan details
def view_challan():
    challan_id = entry_challan_id.get()
    query = f"BEGIN :cur := Challan_Pkg.Get_Challan_Details(:challan_id); END;"
    cur = connection.cursor()
    result = cur.var(cx_Oracle.CURSOR)
    cur.execute(query, (result, challan_id))
    data = result.getvalue().fetchall()
    cur.close()
    display_data(data)

# Function to display data in the description box
def display_data(data):
    description_box.delete(1.0, tk.END)  # Clear previous content
    if data:
        for row in data:
            description_box.insert(tk.END, f"Challan ID: {row[0]}\n")  # Assuming data structure
            description_box.insert(tk.END, f"Vehicle Reg: {row[1]}\n") 
            description_box.insert(tk.END, f"Driver License: {row[2]}\n")
            description_box.insert(tk.END, f"Date Time: {row[3]}\n")
            description_box.insert(tk.END, f"Location ID: {row[4]}\n")
            description_box.insert(tk.END, f"Offence ID: {row[5]}\n")
            description_box.insert(tk.END, f"Offence Type: {row[6]}\n")# Assuming data structure
            # Add other details as needed


# Function to add a new challan
def add_vehicle():
    vehicle_reg = entry_vehicle_reg.get()
    vehicle_type = entry_vehicle_type.get()
    query = f"INSERT INTO Vehicle (Reg_number, vehicle_type) VALUES (:vehicle_reg, :vehicle_type)"
    cursor.execute(query, {
        'vehicle_reg': vehicle_reg,
        'vehicle_type': vehicle_type
    })
    connection.commit()
    messagebox.showinfo("Success", "Vehicle added successfully!")

def update_payment_status():
    payment_id = entry_payment_id.get()
    new_payment_status = entry_new_payment_status.get()
    query = f"BEGIN Payment_Pkg.Update_Payment_Status(:payment_id, :new_payment_status); END;"
    cursor.execute(query, {
        'payment_id': payment_id,
        'new_payment_status': new_payment_status
    })
    connection.commit()
    messagebox.showinfo("Success", "Payment status updated successfully!")

# Function to show the view section
def show_view_section():
    hide_all_sections()
    label_view_challan_id.pack()
    entry_challan_id.pack()
    button_execute_view.pack()
    description_box.pack()


# Function to show the insert section
def show_add_section():
    hide_all_sections()
    label_vehicle_reg.pack()
    entry_vehicle_reg.pack()
    label_vehicle_type.pack()
    entry_vehicle_type.pack()
    button_execute_insert_vehicle.pack()

def show_update_payment_section():
    hide_all_sections()
    label_payment_id.pack()
    entry_payment_id.pack()
    label_new_payment_status.pack()
    entry_new_payment_status.pack()
    button_execute_update_payment.pack()


# Function to hide all sections
def hide_all_sections():
    for widget in root.winfo_children():
        widget.pack_forget()

# Function to handle different actions based on the selected option
def handle_action():
    selected_action = option_var.get()
    if selected_action == "View":
        show_view_section()
    elif selected_action == "Add":
        show_add_section()
    elif selected_action == "Update Payment Status":
        show_update_payment_section()

# Create the tkinter window and widgets
root = tk.Tk()
root.title("Challan Management System")

# Create a dropdown menu for selecting the action
actions = ["View", "Add","Update Payment Status"]
option_var = tk.StringVar(root)
option_var.set(actions[0])  # Default value
option_menu = tk.OptionMenu(root, option_var, *actions)
option_menu.pack()

# Widgets for the view section
label_view_challan_id = tk.Label(root, text="Enter Challan ID to View:")
entry_challan_id = tk.Entry(root)
button_execute_view = tk.Button(root, text="Execute", command=view_challan)
description_box = tk.Text(root, height=10, width=40)

label_vehicle_reg = tk.Label(root, text="Enter Vehicle Registration:")
entry_vehicle_reg = tk.Entry(root)
label_vehicle_type = tk.Label(root, text="Enter Vehicle Type:")
entry_vehicle_type = tk.Entry(root)
button_execute_insert_vehicle = tk.Button(root, text="Add Vehicle", command=add_vehicle)

label_payment_id = tk.Label(root, text="Enter Payment ID to Update:")
entry_payment_id = tk.Entry(root)
label_new_payment_status = tk.Label(root, text="Enter New Payment Status:")
entry_new_payment_status = tk.Entry(root)
button_execute_update_payment = tk.Button(root, text="Execute", command=update_payment_status)
button_execute = tk.Button(root, text="Execute", command=handle_action)
button_execute.pack()

# Run the tkinter main loop
root.mainloop()

# Close cursor and connection after using them
cursor.close()
connection.close()