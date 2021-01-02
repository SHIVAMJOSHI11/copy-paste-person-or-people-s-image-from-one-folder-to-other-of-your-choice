import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from time import sleep
import face_recognition as fr
import os
import cv2
import face_recognition
import time
import datetime
import shutil


def get_encoded_faces():
    """
    looks through the faces folder and encodes all
    the faces

    :return: dict of (name, image encoded)
    """
    encoded = {}

    # for dirpath, dnames, fnames in os.walk("./faces"):
    for dirpath, dnames, fnames in os.walk("./KAKA"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("KAKA/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded


def unknown_image_encoded(img):
    """
    encode a face given the file name
    """
    face = fr.load_image_file("KAKA/" + img)
    encoding = fr.face_encodings(face)[0]

    return encoding


def classify_face(im,image):
    """
    will find all of the faces in a given image and label
    them if it knows what they are

    :param im: str of file path
    :return: list of face names
    """
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    img = im
    # img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    # img = img[:,:,::-1]

    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(faces_encoded, face_encoding, 0.559)
        name = "Unknown"
        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            shutil.copy(image, r'C:\Users\Shivam\Pictures\KAKAIMAGES')
        face_names.append(name)
        

    # Display the resulting image
    """  while True:
        j=90
        print("wwo")
        if j==90:
            cv2.imwrite(f"{a}.jpg",img)
            break#return face_names ko niche kara he vo break ki jagah he
    return face_names

jo=0
print(time.localtime())
#for dirpath, dnames, fnames in os.walk(r"D:\Mobile\Camera"):
for dirpath, dnames, fnames in os.walk(r"D:\DIDIKAHE\DCIM"):
    for f in fnames:
        if f.endswith(".jpg") or f.endswith(".png"):
            print(f)
            #x= cv2.imread("D:\Mobile\Camera/" + f,1)
            x= cv2.imread("D:\DIDIKAHE\DCIM/" + f,1)
      #      print("D:\Mobile\Camera/" + f,1)
            timm=datetime.datetime.now()
            #classify_face(x,"D:\Mobile\Camera/" + f)
            classify_face(x,"D:\DIDIKAHE\DCIM/" + f)
            print(f"{datetime.datetime.now()-timm} time it takes")
            jo=jo+1
            print(jo)
classify_face("sw1 (1).jpg","iss1")
try:
 classify_face("sw1 (2).jpg","iss2")
 classify_face("sw1 (3).jpg","iss3")
 classify_face("sw1 (4).jpg","iss4")
 classify_face("sw1 (5).jpg","iss5")
 classify_face("sw1 (6).jpg","iss6")
 classify_face("sw1 (7).jpg","iss7")
 pass
except:
    pass
time.localtime()"""
jo=0
r=0
lp=[]
for dirpath, dnames, fnames2 in os.walk(r"D:\DIDIKAHE\DCIM"):
    a=len(dnames)
    r=r+1
    print(dnames)
    lp=dnames.copy()
    print(lp)
    if r>0:
        break
r=0
for i in lp:
 r = r + 1
 for dirpath1, dnames2, fnames in os.walk(r"D:\DIDIKAHE\DCIM/"+ lp[r-1]):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                print(f"D:\DIDIKAHE\DCIM\{lp[r-1]}\{f}")
                # x= cv2.imread("D:\Mobile\Camera/" + f,1)
                x = cv2.imread(f"D:\DIDIKAHE\DCIM\{lp[r-1]}\{f}", 1)
                #      print("D:\Mobile\Camera/" + f,1)
                timm = datetime.datetime.now()
                # classify_face(x,"D:\Mobile\Camera/" + f)
                classify_face(x,f"D:\DIDIKAHE\DCIM\{lp[r-1]}\{f}")
                print(f"{datetime.datetime.now() - timm} time it takes")
                jo = jo + 1
                print(jo)
