from PIL import Image, ImageDraw, ImageFont

text = "Vrinda & Tanya"


#font1 = ImageFont.truetype(font='Herculanum', size = 40)
#font2 = ImageFont.truetype(font='Avenir', size = 40)
font3 = ImageFont.truetype(font='Arial', size = 40)
#or use this:
#font = ImageFont.load_default();

col1 = "blue"
col2 = "red"
col3 = "green"

#following lists are just for multiple colors and fonts 
#l = [font1, font2, font3]
m = [col1, col2, col3]

image = Image.new('RGB',(450, 120), (255, 255, 255))
#From the docs:
#Image.new(mode, size) ⇒ image //by default black
#Image.new(mode, size, color) ⇒ image



offset = 0
x = 0
y = 50
for i in range(len(text)):
	c = text[i]
	font = font3
	c_size = font.getsize(c)
	c_image = Image.new('RGBA', c_size, (0,0,0,0))
	c_draw = ImageDraw.Draw(c_image)
	c_draw.text((0, 0), c, font=font, fill=(0,0,0,255))
	
	
	
	image.paste(c_image, (x+offset, y), c_image)
	offset += c_size[0]





image.save("file.png", "PNG")



#Some Help:
'''check this out too:
	            http://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html#example-draw-partial-opacity-text
'''
'''
**im.paste(image, box)

Pastes another image into this image. The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, right, and lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple is given, the size of the pasted image must match the size of the region.

If the modes don’t match, the pasted image is converted to the mode of this image (see the convert method for details).

**im.paste(colour, box)

Same as above, but fills the region with a single colour. The colour is given as a single numerical value for single-band images, and a tuple for multi-band images.

**im.paste(image, box, mask)

Same as above, but updates only the regions indicated by the mask. You can use either “1”, “L” or “RGBA” images (in the latter case, the alpha band is used as mask). Where the mask is 255, the given image is copied as is. Where the mask is 0, the current value is preserved. Intermediate values can be used for transparency effects.

Note that if you paste an “RGBA” image, the alpha band is ignored. You can work around this by using the same image as both source image and mask.

**im.paste(colour, box, mask)

Same as above, but fills the region indicated by the mask with a single colour.
'''


'''
draw.text(position, string, options)

Draws the string at the given position. The position gives the upper left corner of the text.

The font option is used to specify which font to use. It should be an instance of the ImageFont class, typically loaded from file using the load method in the ImageFont module.

The fill option gives the colour to use for the text.
'''
