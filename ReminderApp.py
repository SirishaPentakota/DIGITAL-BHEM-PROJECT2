import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import threading

# Function to add a reminder
def add_reminder():
    reminder_text = entry.get()
    try:
        reminder_date = datetime.strptime(date_entry.get(), "%Y-%m-%d")
        reminder_time = datetime.strptime(time_entry.get(), "%H:%M")
        reminder_datetime = reminder_date.replace(hour=reminder_time.hour, minute=reminder_time.minute)
        reminders.append((reminder_text, reminder_datetime))
        entry.delete(0, tk.END)  # Clear the entry widget
        date_entry.delete(0, tk.END)  # Clear the date entry
        time_entry.delete(0, tk.END)  # Clear the time entry
        update_reminder_list()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid date and time format (YYYY-MM-DD HH:MM).")

# Function to check and show reminders
def check_reminders():
    while True:
        current_time = datetime.now()
        for reminder in reminders:
            if current_time >= reminder[1]:
                messagebox.showinfo("Reminder", reminder[0])
                reminders.remove(reminder)
                update_reminder_list()

# Function to update the list of reminders
def update_reminder_list():
    reminder_list.delete(0, tk.END)
    for reminder in reminders:
        reminder_list.insert(tk.END, f"{reminder[0]} - {reminder[1].strftime('%Y-%m-%d %H:%M')}")

# Initialize the main window
root = tk.Tk()
root.title("Reminder App")

# Create a list to store reminders
reminders = []

# Customize colors and styles
root.configure(bg="blue")  # Set background color

# Create and pack widgets with updated colors and styles
label = tk.Label(root, text="Enter Reminder:", bg="yellow", fg="black", font=("Helvetica", 12))
label.pack(fill='both', padx=10, pady=5)

entry = tk.Entry(root, width=40, font=("Helvetica", 12))
entry.pack(fill='both', padx=10, pady=5)

date_label = tk.Label(root, text="Enter Date (YYYY-MM-DD):", bg="yellow", fg="black", font=("Helvetica", 12))
date_label.pack(fill='both', padx=10, pady=5)

date_entry = tk.Entry(root, width=20, font=("Helvetica", 12))
date_entry.pack(fill='both', padx=10, pady=5)

time_label = tk.Label(root, text="Enter Time (HH:MM):", bg="yellow", fg="black", font=("Helvetica", 12))
time_label.pack(fill='both', padx=10, pady=5)

time_entry = tk.Entry(root, width=10, font=("Helvetica", 12))
time_entry.pack(fill='both', padx=10, pady=5)

add_button = tk.Button(root, text="Add Reminder", command=add_reminder, bg="orange", fg="black", font=("Helvetica", 12))
add_button.pack(fill='both', padx=8, pady=3)

reminder_list = tk.Listbox(root, height=10, width=30, bg="lightyellow", fg="navy", font=("Helvetica", 12))
reminder_list.pack(fill='both', padx=10, pady=10)

# Start the thread for checking reminders
reminder_thread = threading.Thread(target=check_reminders)
reminder_thread.daemon = True  # Allow the thread to exit when the main program exits
reminder_thread.start()

root.mainloop()
