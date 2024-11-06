from PIL import Image, ImageFilter

def apply_grayscale(image):
    return image.convert("L")

def apply_blur(image, radius=2):
    return image.filter(ImageFilter.GaussianBlur(radius))
