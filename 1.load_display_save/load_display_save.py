import argparse
import cv2

# Commande line arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
print(f'width : {image.shape[1]} pixels')
print(f'height : {image.shape[0]} pixels')
print(f'channels : {image.shape[1]} ')

# showing the image
cv2.imshow('Image', image)

'''a call to cv2.waitKey pauses the execution of the script until
we press a key on our keyboard. Using a parameter of 0
indicates that any keypress will un-pause the execution'''
cv2.waitKey(0)

# Writing the image in a png format
cv2.imwrite('newimage.png', image)

# Run the following script in the terminal
# python load_display_save.py --image Messi.jpg

