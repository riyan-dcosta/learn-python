import cv2

class brightnessChange:
    def __init__(self,file_path, lightness_value, contrast=1):
        self.img_path    = file_path
        self.light_value = lightness_value
        self.contrast  = contrast
    def ImageBrightness(self):
        img = cv2.imread(self.img_path, 1)
        out = cv2.convertScaleAbs(img, alpha=self.contrast, beta=self.light_value)
        cv2.imwrite("out.jpg",out)
