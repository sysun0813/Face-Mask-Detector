import face_recognition
from PIL import Image,ImageDraw

image_path='data/without_mask/0.jpg'
mask_image_path='data/mask.png'

face_image_np=face_recognition.load_image_file(image_path)
face_locations=face_recognition.face_locations(face_image_np)
face_image=Image.fromarray(face_image_np)
draw=ImageDraw.Draw(face_image)

mask_image=Image.open(mask_image_path)
mask_image=mask_image.resize((60,50))


for face_location in face_locations:
    top=face_location[0]
    right=face_location[1]
    bottom=face_location[2]
    left=face_location[3]
    face_image.paste(mask_image,(top,left),mask_image)
    face_image.show()

#face_image.paste(mask_image,(55,60),mask_image)
#face_image.show()