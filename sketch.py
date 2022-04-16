import cv2

CAM_WIDTH = 1280
CAM_HEIGHT = 720
capture = cv2.VideoCapture(0)
capture.set(3, CAM_WIDTH)
capture.set(4, CAM_HEIGHT)
while capture.isOpened():
    success, image = capture.read()
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert_image = 255 - gray_image
    blur_image = cv2.GaussianBlur(invert_image, (21, 21), 0)
    inverted_blur_image = 255 - blur_image
    sketch_image = cv2.divide(gray_image, inverted_blur_image, scale=256.0)
    #cv2.resizeWindow('Frame1',CAM_WIDTH, CAM_HEIGHT)
    cv2.imshow('Frame1',sketch_image)
    if cv2.waitKey(1) == ord('q') or cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        capture.release()
        break
else:
    print('Fail to open')
