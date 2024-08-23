import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class College:
    def __init__(self, name, location, ranking, tuition):  
        self.name = name
        self.location = location
        self.ranking = ranking
        self.tuition = tuition

    def update_info(self, name=None, location=None, ranking=None, tuition=None):
        if name:
            self.name = name
        if location:
            self.location = location
        if ranking:
            self.ranking = ranking
        if tuition:
            self.tuition = tuition

    def __str__(self):
        return f"{self.name} | Location: {self.location}, Ranking: {self.ranking}, Tuition: ${self.tuition}"

# Initialize the colleges list
colleges = []

def add_college(name, location, ranking, tuition):
    college = College(name, location, ranking, tuition)
    colleges.append(college)
    messagebox.showinfo("Success", f'College "{name}" added.')

def view_colleges():
    if colleges:
        view_window = tk.Toplevel(root)
        view_window.title("College List")
        view_window.configure(bg="#e0e0e0")
        for college in colleges:
            tk.Label(view_window, text=str(college), font=("Arial", 14), bg="#e0e0e0").pack(pady=5)
    else:
        messagebox.showinfo("Information", "No colleges in the list.")

def search_college(name):
    results = [college for college in colleges if college.name.lower() == name.lower()]
    if results:
        result_window = tk.Toplevel(root)
        result_window.title("Search Results")
        result_window.configure(bg="#e0e0e0")
        for college in results:
            tk.Label(result_window, text=str(college), font=("Arial", 14), bg="#e0e0e0").pack(pady=5)
    else:
        messagebox.showinfo("Information", "College not found.")

def sort_colleges_by(attribute):
    sorted_colleges = sorted(colleges, key=lambda x: getattr(x, attribute))
    sorted_window = tk.Toplevel(root)
    sorted_window.title(f"Colleges Sorted by {attribute.capitalize()}")
    sorted_window.configure(bg="#e0e0e0")
    for college in sorted_colleges:
        tk.Label(sorted_window, text=str(college), font=("Arial", 14), bg="#e0e0e0").pack(pady=5)

def average_tuition():
    if colleges:
        avg_tuition = sum(college.tuition for college in colleges) / len(colleges)
        messagebox.showinfo("Average Tuition", f"Average tuition: ${avg_tuition:.2f}")
    else:
        messagebox.showinfo("Information", "No colleges in the list.")

def visualize_tuition_vs_ranking():
    if colleges:
        rankings = [college.ranking for college in colleges]
        tuitions = [college.tuition for college in colleges]
        plt.scatter(rankings, tuitions)
        plt.xlabel('Ranking')
        plt.ylabel('Tuition ($)')
        plt.title('Tuition vs. Ranking')
        plt.show()
    else:
        messagebox.showinfo("Information", "No colleges in the list.")

def binary_search_by_ranking(target_ranking):
    colleges_sorted = sorted(colleges, key=lambda x: x.ranking)
    left, right = 0, len(colleges_sorted) - 1
    while left <= right:
        mid = (left + right) // 2
        if colleges_sorted[mid].ranking == target_ranking:
            messagebox.showinfo("Search Result", f"Found: {colleges_sorted[mid]}")
            return
        elif colleges_sorted[mid].ranking < target_ranking:
            left = mid + 1
        else:
            right = mid - 1
    messagebox.showinfo("Search Result", "College not found.")

# Main Application
root = tk.Tk()
root.title("College Management System")
root.configure(bg="#333")

# UI Layout
title_font = ("Arial", 20, "bold")
label_font = ("Arial", 14)
entry_font = ("Arial", 14)
button_font = ("Arial", 16, "bold")

tk.Label(root, text="College Management System", font=title_font, bg="#333", fg="#fff").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="College Name:", font=label_font, bg="#333", fg="#fff").grid(row=1, column=0, pady=5, sticky="e")
name_entry = tk.Entry(root, font=entry_font, width=30)
name_entry.grid(row=1, column=1, pady=5)

tk.Label(root, text="Location:", font=label_font, bg="#333", fg="#fff").grid(row=2, column=0, pady=5, sticky="e")
location_entry = tk.Entry(root, font=entry_font, width=30)
location_entry.grid(row=2, column=1, pady=5)

tk.Label(root, text="Ranking:", font=label_font, bg="#333", fg="#fff").grid(row=3, column=0, pady=5, sticky="e")
ranking_entry = tk.Entry(root, font=entry_font, width=30)
ranking_entry.grid(row=3, column=1, pady=5)

tk.Label(root, text="Tuition:", font=label_font, bg="#333", fg="#fff").grid(row=4, column=0, pady=5, sticky="e")
tuition_entry = tk.Entry(root, font=entry_font, width=30)
tuition_entry.grid(row=4, column=1, pady=5)

tk.Button(root, text="Add College", font=button_font, bg="#00bfff", fg="#fff",
          command=lambda: add_college(name_entry.get(), location_entry.get(), int(ranking_entry.get()), int(tuition_entry.get()))).grid(row=5, column=0, columnspan=2, pady=10)

tk.Button(root, text="View Colleges", font=button_font, bg="#ff8c00", fg="#fff", command=view_colleges).grid(row=6, column=0, columnspan=2, pady=10)
tk.Button(root, text="Search College", font=button_font, bg="#32cd32", fg="#fff", command=lambda: search_college(name_entry.get())).grid(row=7, column=0, columnspan=2, pady=10)
tk.Button(root, text="Sort by Ranking", font=button_font, bg="#ff4500", fg="#fff", command=lambda: sort_colleges_by('ranking')).grid(row=8, column=0, columnspan=2, pady=10)
tk.Button(root, text="Sort by Tuition", font=button_font, bg="#8a2be2", fg="#fff", command=lambda: sort_colleges_by('tuition')).grid(row=9, column=0, columnspan=2, pady=10)
tk.Button(root, text="Average Tuition", font=button_font, bg="#1e90ff", fg="#fff", command=average_tuition).grid(row=10, column=0, columnspan=2, pady=10)
tk.Button(root, text="Visualize Tuition vs Ranking", font=button_font, bg="#ff1493", fg="#fff", command=visualize_tuition_vs_ranking).grid(row=11, column=0, columnspan=2, pady=10)
tk.Button(root, text="Binary Search by Ranking", font=button_font, bg="#ff6347", fg="#fff", command=lambda: binary_search_by_ranking(int(ranking_entry.get()))).grid(row=12, column=0, columnspan=2, pady=10)

tk.Button(root, text="Exit", font=button_font, bg="#696969", fg="#fff", command=root.quit).grid(row=13, column=0, columnspan=2, pady=10)

root.mainloop()
