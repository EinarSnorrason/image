import numpy as np
from PIL import Image


def grayscale(pixels):
    red = 0.21
    green = 0.72
    blue = 0.07
    
    for row in pixels:
        for pixel in row:
            brightness = pixel[0]*red+pixel[1]*green+pixel[2]*blue
            for i in range(3):
                pixel[i]=brightness
    grayscale_image = pixels.astype('uint8')
    grayscale_image = Image.fromarray(grayscale_image)
    grayscale_image.save("sol_grayscale.jpg")

def sepia(pixels):
    sepia_matrix = np.array([
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ])
    for row in pixels:
        for i,pixel in enumerate(row):
            row[i] = np.matmul(sepia_matrix,pixel)
            for j in range(3):
                row[i][j]=min(255,row[i][j])
    sepia_image = pixels.astype('uint8')
    sepia_image = Image.fromarray(sepia_image)
    sepia_image.save("sol_sepia.jpg")

filename = "soloppgang.jpg"
pixels = np.asarray(Image.open(filename))
grayscale(pixels)
pixels  = np.asarray(Image.open(filename))
sepia(pixels.astype('uint32'))
