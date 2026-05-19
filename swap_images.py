from PIL import Image

# Open the image
img = Image.open('media/Hero.png')

# Define bounding boxes for each third
left_box = (0, 0, 640, 1080)
middle_box = (640, 0, 1280, 1080)
right_box = (1280, 0, 1920, 1080)

# Crop the images
left_img = img.crop(left_box)
middle_img = img.crop(middle_box)
right_img = img.crop(right_box)

# Create a new image with the same dimensions, preserving mode if possible
new_img = Image.new(img.mode, (1920, 1080))

# Paste them in the new order: Middle, Left, Right (so the left image is now in the middle)
new_img.paste(middle_img, (0, 0))
new_img.paste(left_img, (640, 0))
new_img.paste(right_img, (1280, 0))

# Save the new image
new_img.save('media/Hero.png')
print("Image successfully rearranged.")
