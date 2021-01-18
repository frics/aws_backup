from skimage.filters import threshold_local
import cv2
from PIL import Image

imgpath = "../resource/OriImgPath/pic_crop.jpg"
#image = Image.open(imgpath)
#image_crop = image.crop((700,0,2200,3000))
#image_crop.save('crop.jpg')

image = cv2.imread(imgpath)
orig = image.copy()

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray, ksize = (5,5),sigmaX=0)
warped = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 10)
clean_img = cv2.medianBlur(warped, 5)

savepath = "../resource/SaveImgPath/result.jpg"
cv2.imwrite(savepath,warped)
