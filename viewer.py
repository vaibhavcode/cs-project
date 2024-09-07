import tkinter as tk
from tkinter import ttk
import mysql.connector


def connectdb():
    return mysql.connector.connect(host="localhost",user="root",password="12345",database="attendance_db")


def getdata():
    conn = connectdb()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance")
    rows = cursor.fetchall()
    conn.close()
    return rows


root = tk.Tk()
root.title("Attendance Viewer")
root.geometry("600x400")
root.configure(bg="#f0f0f0")


tree = ttk.Treeview(root, columns=("ID", "Name", "Timestamp"), show='headings')
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Timestamp", text="Timestamp")
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


def load_data():
    for row in getdata():
        tree.insert("", tk.END, values=row)

load_data()

root.mainloop()
