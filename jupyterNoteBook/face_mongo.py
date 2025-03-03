import face_recognition
import cv2
import numpy as np
from pymongo import MongoClient
from helper import get_all_face

# Connect to MongoDB (change the URI to your MongoDB instance if needed)
# Connect to MongoDB server
client = MongoClient(
    'mongodb+srv://satya9125:26ZfPds8iKKf5Dv0@firedb.6oyha.mongodb.net/')
db = client['face_recognition_db']  # Database name
collection = db['faces']  # Collection name

# Function to store face encoding and name in the database


def store_face_encoding(name, image_path):
    # Load the image

    faces = get_all_face(image_path)

    # for each face detected
    for x, y, w, h in faces:
        # crop the image to select only the face
        cropped_image = img[y: y + h, x: x + w]
        # loading the target image path into target_file_name variable  - replace <INSERT YOUR TARGET IMAGE NAME HERE> with the path to your target image

        cv2.imshow(cropped_image)

    """   image = face_recognition.load_image_file(image_path)

    # Find face encodings in the e
    encodings = face_recognition.face_encodings(image)

    if encodings:  # If at least one face is found
        # Use the first face encoding (if more than one is found)
        encoding = encodings[0]

        # Convert the encoding (which is a numpy array) to a list for MongoDB
        encoding_list = encoding.tolist()

        # Create a dictionary with the name and encoding
        face_data = {
            'name': name,
            'encoding': encoding_list  # MongoDB stores encodings as lists
        }

        # Insert the face data into MongoDB collection
        collection.insert_one(face_data)
        print(f"Face data for {name} stored successfully!")
    else:
        print(f"No face detected in the image {image_path}") """


# Example usage: Add a new face to the database
store_face_encoding("John Doe", "Data/images/20190123_083309-COLLAGE.jpg")
