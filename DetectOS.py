import cv2
import numpy as np
import sys, glob, os

if len(sys.argv) < 3 :
	sys.exit('Usage: %s images-dir marker-img' % sys.argv[0])

path = sys.argv[1]
marker_path = sys.argv[2]
for file in glob.glob(path + '*.png') :
	img_rgb = cv2.imread(file)
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	template = cv2.imread(marker_path,0)
	w, h = template.shape[::-1]

	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.8
	loc = np.where( res >= threshold)
	if len(zip(*loc[::-1])) > 0 :
		filename = os.path.basename(file)
		print os.path.splitext(filename)[0]
