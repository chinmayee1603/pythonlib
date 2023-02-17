# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
import cv2

# Open the default camera
cap = cv2.VideoCapture(0)

# Capture an image
ret, frame = cap.read()

# Release the camera
cap.release()

# Save the image as a file
cv2.imwrite("image.jpg", frame)
# Load the image
img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (48, 48))
img = np.array(img).reshape(-1, 48, 48, 1).astype("float32") / 255.0

# Load the model
model = keras.models.load_model("model.h5")

# Predict the emotion label
emotion_labels = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]
predictions = model.predict(img)
emotion_label = emotion_labels[np.argmax(predictions[0])]

print("The detected emotion is:", emotion_label)
