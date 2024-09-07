import cv2
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# connect to db
def connectdb():
    return mysql.connector.connect(host="localhost",user="root",password="12345",database="attendance_db")

#get next id
def nextid():
    conn = connectdb()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(id) FROM attendance")
    result = cursor.fetchone()
    conn.close()
    if result[0] is not None:
        return (result[0] + 1) 
    else:
        return 1

# save attendance
def saveattend(personid):
    conn = connectdb()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (name) VALUES (%s)", (f"Person {personid}",))
    conn.commit()
    conn.close()

#load facedetection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# find faces
def detectface(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#show video feed
def updateframe():
    ret, frame = cap.read()
    if ret:
        global lastframe
        lastframe = frame  
        detectedfaces = detectface(frame)  
        
        #draw rectangle
        for (x, y, w, h) in detectedfaces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        #show in tkinter
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=image)
        video_label.config(image=photo)
        video_label.image = photo

    root.after(10, updateframe)  #keep updating frames

#code for button
def markattend():
    faces = detectface(lastframe)
    if len(faces) > 0: 
        personid = nextid()
        saveattend(personid)
        status_label.config(text=f"Status: Attendance recorded for Person {personid}")
        messagebox.showinfo("Success", f"Attendance recorded for Person {personid}")
    else:
        messagebox.showwarning("Warning", "No faces detected. Attendance not recorded.")
        status_label.config(text=f"No faces detected. Attendance not recorded.")

# tkinter window
root = tk.Tk()
root.title("Attendance System")
root.geometry("900x700")
root.configure(bg="#f0f0f0")
video_label = tk.Label(root)
video_label.pack(pady=20)
status_label = tk.Label(root, text="Status: Waiting for action", font=("Arial", 14), bg="#f0f0f0")
status_label.pack(pady=10)
start_button = tk.Button(root, text="Start Recognition", command=markattend, font=("Arial", 14), bg="#4CAF50", fg="white")
start_button.pack(pady=20)

#srtart capturing 
cap = cv2.VideoCapture(0)

last_frame = None  
updateframe()
root.mainloop()
cap.release()
