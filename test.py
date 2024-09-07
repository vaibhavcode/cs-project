import tkinter as tk
from tkinter import ttk
import cv2
import mysql.connector
from PIL import Image, ImageTk
import time


def connectdb():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="attendance_db"
    )


def getdata():
    conn = connectdb()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance")
    rows = cursor.fetchall()
    conn.close()
    return rows


def saveattend(name):
    conn = connectdb()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (name) VALUES (%s)", (name,))
    conn.commit()
    conn.close()


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
last_seen = {}
delay = 10

def detect_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    return faces


root = tk.Tk()
root.title("Face Detection and Attendance Viewer")
root.geometry("1200x700")
root.configure(bg="#f0f0f0")

face_frame = tk.Frame(root, width=600, height=700)
face_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


viewer_frame = tk.Frame(root, width=600, height=700)
viewer_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


tree = ttk.Treeview(viewer_frame, columns=("ID", "Name", "Timestamp"), show='headings')
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Timestamp", text="Timestamp")
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


def load_data():
    for row in getdata():
        tree.insert("", tk.END, values=row)


cap = cv2.VideoCapture(0)


def update_frame():
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detect_face(frame)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
   
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=image)
        video_label.config(image=photo)
        video_label.image = photo
    
    root.after(10, update_frame)


video_label = tk.Label(face_frame)
video_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
status_label = tk.Label(face_frame, text="Status: Not Recognizing", font=("Arial", 14), bg="#f0f0f0")
status_label.pack(pady=10)
start_button = tk.Button(face_frame, text="Start Recognition", command=lambda: status_label.config(text="Status: Recognizing Faces"))
start_button.pack(pady=20)


view_button = tk.Button(viewer_frame, text="Refresh Data", command=load_data)
view_button.pack(pady=10)
load_data()  

update_frame()

root.mainloop()
cap.release()
