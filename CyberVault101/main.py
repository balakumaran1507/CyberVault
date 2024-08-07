import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

class ScriptLauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Script Launcher")
        
        # Create GUI elements
        self.label = tk.Label(root, text="Select a Python script to run:")
        self.label.pack(pady=10)
        
        self.select_button = tk.Button(root, text="Select Script", command=self.select_script)
        self.select_button.pack(pady=5)
        
        self.run_button = tk.Button(root, text="Run Script", command=self.run_script, state=tk.DISABLED)
        self.run_button.pack(pady=5)
        
        self.script_path = None

    def select_script(self):
        # Open a file dialog to select a Python script
        self.script_path = filedialog.askopenfilename(
            filetypes=[("Python Files", "*.py")],
            title="Select a Python Script"
        )
        if self.script_path:
            self.run_button.config(state=tk.NORMAL)
            messagebox.showinfo("Script Selected", f"Selected Script: {os.path.basename(self.script_path)}")
        else:
            self.run_button.config(state=tk.DISABLED)

    def run_script(self):
        if not self.script_path:
            messagebox.showwarning("No Script", "Please select a script to run.")
            return
        
        # Run the selected script
        try:
            result = subprocess.run(
                ['python', self.script_path],
                capture_output=True,
                text=True,
                check=True
            )
            messagebox.showinfo("Script Output", result.stdout)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Script Error", f"Error: {e.stderr}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScriptLauncherApp(root)
    root.mainloop()
