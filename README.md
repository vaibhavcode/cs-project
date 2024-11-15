# Computer Vision-Based Real-Time Attendance Logger

This project implements a real-time attendance logging system using computer vision techniques. It leverages facial recognition to track attendance and log it automatically based on video feeds.

---

## Features

- Real-time facial detection for attendance tracking.
- Logs attendance to a database.
- Uses pre-trained models for facial recognition.
- Supports both live webcam and video file input.

---

## Project Structure

- **`detector.py`**: The script for detecting faces in the video feed.
- **`recognizer.py`**: Handles facial recognition to match faces to known individuals.
- **`trainer.py`**: Used for training the model with facial data.
- **`viewer.py`**: Displays real-time video feed with detection boxes.
- **`sqlprp`**: Handles database operations for logging attendance.
- **`trained_model.yml`**: Stores the trained model for facial recognition.
- **`test.py`**: Contains test cases for validating the model and system.
- **`requirements.txt`**: Lists necessary Python dependencies.

---

## Prerequisites

- Python 3.7 or higher.
- Required Python libraries listed in `requirements.txt`.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vaibhavcode/cs-project.git
   cd cs-project
   ```

2. **Install dependencies**:
   Install all required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model**:
   If you haven't already, train the facial recognition model by running:
   ```bash
   python trainer.py
   ```

4. **Run the application**:
   Execute the attendance logging system:
   ```bash
   python viewer.py
   ```

---

## How It Works

1. The system captures video frames either from a webcam or a video file.
2. Detected faces are matched against known individuals using a pre-trained model.
3. If a match is found, the individual's attendance is logged in a database.
4. The live video feed is displayed with detection boxes highlighting recognized faces.

---

## Contributors

- **Vaibhav Khurana**

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code under the terms of the license.

---

## Acknowledgements

This project utilizes OpenCV for real-time computer vision and facial recognition. Special thanks to the OpenCV community for their invaluable resources.
