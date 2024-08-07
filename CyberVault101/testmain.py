import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import string
import pyperclip
from cryptography.fernet import Fernet

window = tk.Tk()
window.title("Password Manager V0.0.1")
window.geometry('440x540')
window.configure(bg='#333333')

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt and decrypt functions
def encrypt_data(data):
    return cipher_suite.encrypt(data.encode())

def decrypt_data(encrypted_data):
    return cipher_suite.decrypt(encrypted_data).decode()

# Encrypted login credentials
encrypted_username = encrypt_data("User123")
encrypted_password = encrypt_data("password")

# Encrypted passwords storage
encrypted_passwords = {}

def login():
    username = "User123"
    password = "password"
    if username_entry.get() == decrypt_data(encrypted_username) and password_entry.get() == decrypt_data(encrypted_password):
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        show_password_manager()
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

def show_password_manager():
    frame.pack_forget()
    password_manager_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def add_password():
    website = website_entry.get()
    password = password_new_entry.get()
    email = email_entry.get()
    
    encrypted_password = encrypt_data(password)
    
    if website in encrypted_passwords:
        encrypted_passwords[website].append({'password': encrypted_password, 'email': email})
    else:
        encrypted_passwords[website] = [{'password': encrypted_password, 'email': email}]
        
    messagebox.showinfo("Success", "Password added successfully")

def view_passwords():
    password_window = tk.Toplevel(window)
    password_window.title("Passwords")
    password_window.geometry('600x400')
    password_window.configure(bg='#333333')

    tree = ttk.Treeview(password_window, columns=("Website", "Email", "Password"), show='headings')
    tree.heading("Website", text="Website")
    tree.heading("Email", text="Email")
    tree.heading("Password", text="Password")

    for website, data in encrypted_passwords.items():
        for entry in data:
            email = entry["email"]
            password = decrypt_data(entry["password"])
            tree.insert("", "end", values=(website, email, password))

    tree.pack(expand=True, fill=tk.BOTH)

def generate_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    pyperclip.copy(password)
    messagebox.showinfo("Generated Password", f"Your generated password is: {password}\n\nThe password has been copied to the clipboard.")

def manage_subscriptions():
    messagebox.showinfo("Manage Subscriptions", "Feature under development. Coming soon!")

frame = tk.Frame(bg='#333333')

login_label = tk.Label(frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tk.Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tk.Entry(frame, font=("Arial", 16))
password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
password_label = tk.Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tk.Button(frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

password_manager_frame = tk.Frame(window, bg='#333333')

website_label = tk.Label(password_manager_frame, text="Website", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
website_entry = tk.Entry(password_manager_frame, font=("Arial", 16))
email_label = tk.Label(password_manager_frame, text="Email", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
email_entry = tk.Entry(password_manager_frame, font=("Arial", 16))
password_new_label = tk.Label(password_manager_frame, text="New Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
password_new_entry = tk.Entry(password_manager_frame, show="*", font=("Arial", 16))
add_password_button = tk.Button(password_manager_frame, text="Add Password", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=add_password)
view_passwords_button = tk.Button(password_manager_frame, text="View Passwords", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=view_passwords)
generate_password_button = tk.Button(password_manager_frame, text="Generate Password", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=generate_password)
manage_subscriptions_button = tk.Button(password_manager_frame, text="Manage Subscriptions", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=manage_subscriptions)

website_label.grid(row=0, column=0)
website_entry.grid(row=0, column=1, pady=10)
email_label.grid(row=1, column=0)
email_entry.grid(row=1, column=1, pady=10)
password_new_label.grid(row=2, column=0)
password_new_entry.grid(row=2, column=1, pady=10)
add_password_button.grid(row=3, column=0, columnspan=2, pady=10)
view_passwords_button.grid(row=4, column=0, columnspan=2, pady=10)
generate_password_button.grid(row=5, column=0, columnspan=2, pady=10)
manage_subscriptions_button.grid(row=6, column=0, columnspan=2, pady=10)

window.mainloop()