import face_recognition

image_of_bill = face_recognition.load_image_file('../img/bill.jpg')
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

unknown_image = face_recognition.load_image_file('../img/bill2.jpg')
# unknown_image = face_recognition.load_image_file('../img/steve_jobs.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

#  Compare Faces

results = face_recognition.compare_faces(
    [bill_face_encoding], unknown_face_encoding)

if results[0]:
    print('This is Bill Gates')
else:
    print("This isn't Bill Gates")
