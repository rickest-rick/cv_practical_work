"""Independent Tool to manually select ROIs of Images in the desired file format (numpy array)

Files generated by this tool can be used for training and as input for the classifiers and are also acepted as input for
the DataProvider class

:author: Thomas Poschadel"""
import glob
import cv2
import numpy as np
# The absolut image folder path
FOLDER_PATH = "enter path here"

filenames = glob.glob(f"{FOLDER_PATH}/*")
data = dict()

for img_path in filenames:
    img = cv2.imread(img_path)
    window_name = f"Select ROI for {img_path}"
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    x, y, w, h = cv2.selectROI(window_name, img)
    cv2.destroyAllWindows()
    data[img_path] = x, y, w, h

print(f"Writing to npy file ...")
# please change the outputpath of the file according to your file system
np.save("~/outputpath", data)




