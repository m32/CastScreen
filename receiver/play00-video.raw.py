#!/usr/bin/env vpython3
import cv2

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    # return the resized image
    return resized

# grab a pointer to the video stream and initialize the FPS counter
#print("[INFO] sampling frames from webcam...")
#stream = cv2.VideoCapture(0)
stream = cv2.VideoCapture("video.raw")

# loop over some frames
frames = 0
while True:
    # grab the frame from the stream and resize it to have a maximum
    # width of 400 pixels
    (grabbed, frame) = stream.read()
    if not grabbed:
        break
    #frame = resize(frame, width=400)
    frames += 1

    cv2.imshow("Frame", frame)
    #cv2.waitKey(-1)
    key = cv2.waitKey(1) & 0xFF

print('total frames:', frames)
# do a bit of cleanup
stream.release()
cv2.destroyAllWindows()
