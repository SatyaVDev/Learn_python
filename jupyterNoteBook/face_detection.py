import face_recognition
import cv2

image_path = r"Data/images/20190123_083309-COLLAGE.jpg"
image = cv2.imread(image_path)

# Check if the image was loaded correctly
if image is None:
    print(f"Error: Image file '{image_path}' not found or unable to read.")
else:
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(rgb_image)

    for (top, right, bottom, left) in faces:
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

    # Save the image with the detected faces
    cv2.imwrite('processed_image.jpg', image)  # Save image
    print("Image saved as 'processed_image.jpg'.")
