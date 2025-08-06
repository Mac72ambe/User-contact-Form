
import tkinter as tk

# Create the main application window
window = tk.Tk()
window.title("task1.0 - Contact Form")
window.geometry("400x400")
window.resizable(False, False)

# Labels and Entries
tk.Label(window, text="Full Name:", font=("Arial", 12)).pack(pady=5)
name_entry = tk.Entry(window, width=30, font=("Arial", 12))
name_entry.pack()

tk.Label(window, text="Email:", font=("Arial", 12)).pack(pady=5)
email_entry = tk.Entry(window, width=30, font=("Arial", 12))
email_entry.pack()

# Labels and Entries
tk.Label(window, text="Phone Number:", font=("Arial", 12)).pack(pady=5)
phone_number_entry = tk.Entry(window, width=30, font=("Arial", 12))
name_entry.pack()

tk.Label(window, text="Adress:", font=("Arial", 12)).pack(pady=5)
adress_entry = tk.Entry(window, width=30, font=("Arial", 12))
email_entry.pack()

# Submit button
def submit():
    name = name_entry.get()
    email = email_entry.get()
    phone_number = phone_number_entry.get()
    adress= adress_entry.get()
    

tk.Button(window, text="Submit", command=submit, font=("Arial", 12)).pack(pady=10)

# Message label
message_label = tk.Label(window, text="", font=("Arial", 12))
message_label.pack()
# Start the Tkinter event loop
window.mainloop()
