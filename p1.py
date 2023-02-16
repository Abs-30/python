import cv2 as cv
im = cv.imread('images/grad.jpg', cv.IMREAD_COLOR)
assert im is not None

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

resized_im = rescaleFrame(im)
cv.namedWindow('image', cv.WINDOW_KEEPRATIO)

cv.imshow('image', resized_im)
cv.waitKey(0)

cv.destroyAllWindows()