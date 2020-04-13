import warnings
with warnings.catch_warnings():
  warnings.filterwarnings("ignore",category=FutureWarning)
  import tensorflow as tf
from keras.models import load_model
from PIL import Image, ImageChops, ImageOps
import numpy as np
import cv2
import sys

def crop_surrounding_whitespace(cv_img):
    image = Image.fromarray(cv_img).convert('L')
    image = ImageOps.invert(image)
    bg = Image.new(image.mode, image.size, image.getpixel((0, 0)))
    diff = ImageChops.difference(image, bg)
    bbox = diff.getbbox()
    if not bbox:
        return cv_img
    image = image.crop(bbox)
    return np.asarray(image)

def keras_process_image(img):
    image_x = 28
    image_y = 28
    img = cv2.resize(img, (image_x, image_y))
    img = np.array(img, dtype=np.float32)
    img = np.reshape(img, (-1, image_x, image_y, 1))
    return img

def get_categories():
    with open('categories', 'r') as f:
        categories = [c.strip() for c in f.readlines()]
    return categories

def keras_predict(image):
    model = tf.keras.models.load_model('QuickDraw.h5')
    processed = keras_process_image(image)
    print("processed: " + str(processed.shape))
    pred_probab = model.predict(processed)[0]
    pred_class = list(pred_probab).index(max(pred_probab))
    return max(pred_probab), pred_class

def Predict(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Invalid Image Path: Could not open")
        exit(1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = crop_surrounding_whitespace(img)
    prob, prediction = keras_predict(img)
    categories = get_categories()
    return (categories[prediction], prob)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: python3 Predict.py <image path>")
        exit(1)

    image_path = sys.argv[1]
    print(Predict(image_path))
