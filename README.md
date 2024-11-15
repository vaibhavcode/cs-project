Real-Time Attendance Logger
This project implements a computer vision-based real-time attendance system using facial recognition. It captures live images, identifies individuals, and logs attendance securely.

Features
Live Facial Recognition: Detects and recognizes faces in real time.
Database Integration: Stores attendance records efficiently.
User-Friendly: Easy to set up and use.
Prerequisites
Python Version: Python 3.7+
Database: MySQL
Libraries:
OpenCV
NumPy
Pandas
MySQL Connector
Install dependencies using:

bash
Copy code
pip install -r requirements.txt
Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/vaibhavcode/cs-project.git
cd cs-project
2. Configure the Database
Create a MySQL database named attendance.
Import the schema:
bash
Copy code
mysql -u <username> -p attendance < attendance_schema.sql
3. Train the Model
Collect training images using detector.py.
Train the recognition model:
bash
Copy code
python trainer.py
4. Run the Attendance Logger
Start the program to log attendance:
bash
Copy code
python recognizer.py
Usage
Prepare Training Data: Use detector.py to capture face samples.
Train the Model: Run trainer.py to create a trained facial recognition model.
Start Attendance Logger: Use recognizer.py to detect and log attendance.
Troubleshooting
Ensure the MySQL service is running.
Verify camera permissions.
Confirm all dependencies are installed.
Contributing
Feel free to fork this repository and suggest improvements via pull requests.

License
This project is licensed under the MIT License. See LICENSE for details.

