import numpy as np
import cv2
import pyocr
import os
from PIL import Image

path = r"C:/Users/Owner/AppData/Roaming/.minecraft/screenshots/"

img = cv2.imread(f"{path}/2023-12-19_17.43.54.png")

img = img[0:800, 600:1155]

bgr = [255,85,85]
img_bgr = np.array(bgr)
mask = cv2.inRange(img,img_bgr,img_bgr)

bgr = [85,255,85]
img_bgr = np.array(bgr)
mask += cv2.inRange(img,img_bgr,img_bgr)

bgr = [85,85,255]
img_bgr = np.array(bgr)
mask += cv2.inRange(img,img_bgr,img_bgr)

bgr = [85,255,255]
img_bgr = np.array(bgr)
mask += cv2.inRange(img,img_bgr,img_bgr)
result = cv2.bitwise_and(img, img, mask = mask)

cv2.imwrite("read.png", result)

img = Image.open('read.png')
path='C:\\Program Files\\Tesseract-OCR\\'
os.environ['PATH'] = os.environ['PATH'] + path

pyocr.tesseract.TESSERACT_CMD = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# pyocrが使えることを確認する
tools = pyocr.get_available_tools()
# tesseractのみダウンロードしたため0番目を指定
tool = tools[0]
print(tool.get_name())

txt1 = tool.image_to_string(img,lang='eng',builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)

print(txt1)