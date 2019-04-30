import face_recognition
import numpy as np
import matplotlib.pyplot as plt
import urllib.request
import os

def get_image(ip):
    if os.path.isfile("new.jpg"):
        os.rename("new.jpg", "old.jpg")
    urllib.request.urlretrieve(ip + "/photo.jpg", "new.jpg") 
    
def snap(ip):
    urllib.request.urlretrieve(ip + "/photo.jpg", "snap.jpg") 

def get_faces(filename, ax=None):
    image = face_recognition.load_image_file(filename)
    faces = face_recognition.face_locations(image)
    encodings = []
    for f in faces:
        sub_image = image[f[0]:f[2], f[3]:f[1]]
        encoding = face_recognition.face_encodings(sub_image)
        if len(encoding) == 1:
            encodings += encoding
        else:
            encodings.append(np.zeros(128))
    if ax is not None:
        ax.imshow(image)
        for f in faces:
            ax.plot([f[1], f[1], f[3], f[3], f[1]], [f[0], f[2], f[2], f[0], f[0]])
    print(faces, encodings)
    return faces, encodings

def show_nth_faces(filename, faces_position, n):
    image = face_recognition.load_image_file(filename)
    f = faces_position[n]
    sub_image = image[f[0]:f[2], f[3]:f[1]]
    plt.imshow(sub_image)
    plt.show()
    
def get_stat(photo_before, photo_after, tolerance=0.5, debug=False):
    fig, (ax_l, ax_r) = plt.subplots(1, 2)
    faces_before, encodings_before = get_faces(photo_before, ax=ax_l)
    faces_after, encodings_after = get_faces(photo_after, ax=ax_r)
    fig.show()
    before_count = len(faces_before)
    after_count = len(faces_after)
    results = []
    for i, face in enumerate(encodings_after):
        result = face_recognition.compare_faces(encodings_before, face, tolerance=tolerance)
        if debug:
            print(i, result)
        results.append(result)
    get_on_count = 0
    for face in np.array(results):
        if True not in face:
            get_on_count += 1
    got_off_count = before_count + get_on_count - after_count
    if get_on_count < 0:
        got_off_count -= get_on_count
        get_on_count = 0
    if got_off_count < 0:
        get_on_count -= got_off_count
        got_off_count = 0
    if debug:
        print("ก่อนหน้า: {} ขึ้นเพิ่ม: {} ลงรถ: {} ปัจจุบัน: {}".format(before_count, get_on_count, got_off_count, after_count))
    return [before_count, get_on_count, got_off_count, after_count]