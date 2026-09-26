import numpy as np
def calculate_brightness(img):
	# Write your code here
    try:
        img = np.array(img, dtype=float)
    except (ValueError, TypeError):
        return -1
    if img.size == 0:
        return -1
    # 检查像素值是否都在 [0, 255] 范围内
    if np.any(img < 0) or np.any(img > 255):
        return -1
    return float(np.mean(img))
