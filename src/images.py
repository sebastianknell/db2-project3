import face_recognition
image = face_recognition.load_image_file("img\example.png")
facesLocations = face_recognition.face_locations(image)

print(facesLocations)