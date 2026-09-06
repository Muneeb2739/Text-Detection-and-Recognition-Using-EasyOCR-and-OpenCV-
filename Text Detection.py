import cv2
import easyocr
import matplotlib.pyplot as plt

image = cv2.imread("before.jpg")

reader = easyocr.Reader(['en'])

results = reader.readtext(image)

for (box, text, confidence) in results:

    top_left = tuple(map(int, box[0]))
    bottom_right = tuple(map(int, box[2]))


    cv2.rectangle( image, top_left, bottom_right, (0, 255, 0), 3)

    cv2.putText(image, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)
plt.axis("off")
plt.show()