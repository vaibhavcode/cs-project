import cv2
import numpy as np
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trained_model.yml')


labels = {0: "Elon Musk", 1: "Bill Gates"}


def connectdb():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="attendance_db"
    )


def saveattend(name):
    conn = connectdb()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (name) VALUES (%s)", (name,))
    conn.commit()
    conn.close()


last_seen = {}
delay = 10


root = tk.Tk()
root.title("Attendance System")
root.geometry("800x600")


video_label = tk.Label(root)
video_label.pack()

status_label = tk.Label(root, text="Status: Not Recognizing")
status_label.pack(pady=20)


def startrecognize():
    status_label.config(text="Status: Recognizing Faces")

start_button = tk.Button(root, text="Start Recognition", command=startrecognize)
start_button.pack(pady=20)


cap = cv2.VideoCapture(0)


def updateframe():
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml').detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5)
        
        for (x, y, w, h) in faces:
            face_roi = gray[y:y + h, x:x + w]
            label, confidence = recognizer.predict(face_roi)
            current_time = time.time()
            
            if confidence > 90:
                name = labels.get(label, "Unknown")
                if name not in last_seen or (current_time - last_seen[name]) > delay:
                    last_seen[name] = current_time
                    saveattend(name)
                    status_label.config(text=f"Status: Attendance recorded for {name}")
            else:
                name = "Unknown"
            
            cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=image)
        video_label.config(image=photo)
        video_label.image = photo

    root.after(10, updateframe)

updateframe()
root.mainloop()
cap.release()
