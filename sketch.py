import cv2

CAM_WIDTH = 1280
CAM_HEIGHT = 720

cap = cv2.VideoCapture()
cap.open(0, cv2.CAP_DSHOW)
cap.set(3, CAM_WIDTH)
cap.set(4, CAM_HEIGHT)

while cap.isOpened():
    success, image = cap.read()
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert_image = 255 - gray_image
    blur_image = cv2.GaussianBlur(invert_image, (21, 21), 0)
    inverted_blur_image = 255 - blur_image
    sketch_image = cv2.divide(gray_image, inverted_blur_image, scale=256.0)
    cv2.imshow('Sketch Demo',sketch_image)
    if cv2.waitKey(1) == ord('q'):
        break
else:
    print('Fail to open')

cv2.destroyAllWindows()
cap.release()
