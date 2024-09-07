import cv2
import os
import numpy as np

data_path = 'training_data'
people = [person for person in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, person))]

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

labels = []
faces = []

label_id = 0
label_map = {}

for person in people:
    person_path = os.path.join(data_path, person)
    label_map[label_id] = person
    for image_name in os.listdir(person_path):
        img_path = os.path.join(person_path, image_name)
        image = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        if image is None:
            continue
        if image.shape[-1] == 4:
            image = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
        else:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces.append(image)
        labels.append(label_id)
    label_id += 1


face_recognizer.train(faces, np.array(labels))
face_recognizer.write('trained_model.yml') 
