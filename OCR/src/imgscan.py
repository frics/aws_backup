from imutils.perspective import four_point_transform
from skimage.filters import threshold_local
import cv2
import imutils

imgpath = "../resource/ImgPath/pic.jpg"
image = cv2.imread(imgpath)
ratio = image.shape[0]/500.0
orig = image.copy()
image = imutils.resize(image,height=500)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray,(5,5),0)
edged = cv2.Canny(gray,75,200)

contours = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours,key = cv2.contourArea, reverse=True)[:5]

for c in contours:
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.02*peri,True)
    if len(approx) == 4:
        screenCount = approx
        break

warped = four_point_transform(orig,screenCount.reshape(4,2)*ratio)
warped = cv2.cvtColor(warped,cv2.COLOR_BGR2GRAY)
T = threshold_local(warped,11,offset=10,method="gaussian")
warped = (warped > T).astype("uint8")*255

savepath = "../resource/SaveImgPath/result.jpg"
cv2.imwrite(savepath,warped)
