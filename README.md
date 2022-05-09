# Create a Pencil Sketch Portrait with OpenCV

## Procedures
1. Import the library
2. Setting up a webcam
3. Convert the color image to grayscale and convert to negative
4. Apply a Gaussian blur and blend the grayscle image with the blurred negative
5. Displaying the output

## Step 1: Import the library
```python
import cv2
```
## Step 2: Setting up a webcam (Windows)
```python
CAM_WIDTH = 1280
CAM_HEIGHT = 720

cap = cv2.VideoCapture()
cap.open(0, cv2.CAP_DSHOW)
cap.set(3, CAM_WIDTH)
cap.set(4, CAM_HEIGHT)
```
It is quicker to get web cam live in Windows environment by adding cv2.CAP_DSHOW attribute.
## Step 2: Setting up a webcam (Windows/Linux/Mac)
```python
CAM_WIDTH = 1280
CAM_HEIGHT = 720

cap = cv2.VideoCapture(0)
cap.set(3, CAM_WIDTH)
cap.set(4, CAM_HEIGHT)
```
## Step 3: Convert the color image to grayscale and convert to negative
```python
while cap.isOpened():
    success, image = cap.read()
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert_image = 255 - gray_image
```
## Step 4: Apply a Gaussian blur and blend the grayscle image with the blurred negative
```python
    blur_image = cv2.GaussianBlur(invert_image, (21, 21), 0)
    inverted_blur_image = 255 - blur_image
    sketch_image = cv2.divide(gray_image, inverted_blur_image, scale=256.0)
```
## Step 5: Displaying the output
```python
    cv2.imshow('Sketch Demo',sketch_image)
    if cv2.waitKey(1) == ord('q'):
        break
else:
    print('Fail to open')

cv2.destroyAllWindows()
cap.release()
```
## Reference
- [How to create a beautiful pencil sketch effect with OpenCV and Python](https://www.askaswiss.com/2016/01/how-to-create-pencil-sketch-opencv-python.html)
