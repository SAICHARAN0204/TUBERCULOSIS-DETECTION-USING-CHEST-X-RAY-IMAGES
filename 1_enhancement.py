from PIL import Image
from PIL import ImageEnhance
  
# Opens the image file
image = Image.open("C:\\Users\\saich\\vs code\\dip_proj\\tuberculosis.jpg")
  
# shows image in image viewer
image.show()
  
# Enhance Sharpness
curr_sharp = ImageEnhance.Contrast(image)
new_sharp = 8.3
  
# Sharpness enhanced by a factor of 8.3
img_sharped = curr_sharp.enhance(new_sharp)
  
# shows updated image in image viewer
img_sharped.show()