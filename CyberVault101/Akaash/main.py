import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Simplified Banking App")
root.geometry("400x500")

# Configure the grid
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)

# Header Label
header_label = tk.Label(root, text="Welcome to EasyBank", font=("Arial", 24), pady=20)
header_label.grid(row=0, column=0)

# Define large buttons for banking options
balance_btn = tk.Button(root, text="Check Balance", font=("Arial", 18), height=3, width=20, bg="#4CAF50", fg="white")
balance_btn.grid(row=1, column=0, padx=20, pady=10)

withdraw_btn = tk.Button(root, text="Withdraw Money", font=("Arial", 18), height=3, width=20, bg="#2196F3", fg="white")
withdraw_btn.grid(row=2, column=0, padx=20, pady=10)

deposit_btn = tk.Button(root, text="Deposit Money", font=("Arial", 18), height=3, width=20, bg="#FFC107", fg="white")
deposit_btn.grid(row=3, column=0, padx=20, pady=10)

exit_btn = tk.Button(root, text="Exit", font=("Arial", 18), height=3, width=20, bg="#F44336", fg="white", command=root.quit)
exit_btn.grid(row=4, column=0, padx=20, pady=10)

# Run the main application loop
root.mainloop()
