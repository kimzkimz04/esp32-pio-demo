import cv2
import numpy as np
import os

os.makedirs("output", exist_ok=True)

img = np.full((400, 400, 3), 255, dtype=np.uint8)

cv2.circle(img,    (100, 100), 60, (255, 0, 0), -1)
cv2.rectangle(img, (220, 40), (360, 160), (0, 255, 0), -1)
pts = np.array([[200, 380], [120, 240], [280, 240]], np.int32)
cv2.fillPoly(img, [pts], (0, 0, 255))

cv2.imwrite("output/1_original.jpg", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("output/2_gray.jpg", gray)

_, thresh = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY_INV)
cv2.imwrite("output/3_thresh.jpg", thresh)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

result = img.copy()
count = 0
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 500:
        continue
    count += 1
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)
    v = len(approx)
    shape = "Triangle" if v == 3 else "Rectangle" if v == 4 else "Circle"

    x, y, w, h = cv2.boundingRect(approx)
    cv2.rectangle(result, (x, y), (x + w, y + h), (0, 0, 0), 2)
    cv2.putText(result, shape, (x, y - 8),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    print(f"พบ {shape} พื้นที่ {int(area)} px จุดยอด {v} จุด")

cv2.imwrite("output/4_result.jpg", result)

print(f"--- OpenCV version {cv2.__version__} ---")
print(f"ตรวจพบวัตถุทั้งหมด {count} ชิ้น")