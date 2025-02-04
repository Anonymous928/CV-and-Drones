import cv2
import numpy as np
import matplotlib.pyplot as plt


def hough_line(s):
    image = cv2.imread(s)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,100,160,apertureSize=3)

    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
    

    final_img = image.copy()
    for r_theta in lines:
        arr = np.array(r_theta[0], dtype=np.float64)
        r, theta = arr
        a = np.cos(theta)
        b = np.sin(theta)
    
        x0 = a*r
        y0 = b*r
    
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
    
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(final_img, (x1, y1), (x2, y2), (0, 255, 0), 4)

    _,ax = plt.subplots(1,2,figsize=[10,5])
    ax[0].imshow(image);ax[0].set_title('Input Image');ax[0].axis('off')
    ax[1].imshow(final_img);ax[1].set_title('Detected Lines');ax[1].axis('off')
    plt.show()