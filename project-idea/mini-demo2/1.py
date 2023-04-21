'''
隨機著色    

'''

import numpy, random, sys, cv2

original = cv2.imread(sys.argv[1])
output = original.copy()

bgr2gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(bgr2gray, 170, 225, cv2.THRESH_BINARY)
bitwise_not = cv2.bitwise_not(threshold)
img, contour, hier = cv2.findContours(bitwise_not, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for cnt in contour:
    color = cv2.cvtColor(numpy.uint8([[[random.randint(0,170), random.randint(150,150), random.randint(150,255)]]]),
                         cv2.COLOR_HSV2BGR)[0,0]
    cv2.drawContours(output, [cnt], 0, [int(i) for i in color], -1)
cv2.imwrite(sys.argv[1] + "_new.jpg", output)



