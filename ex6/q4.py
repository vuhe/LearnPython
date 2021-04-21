from PIL import Image, ImageFilter

im = Image.open('./resources/上海.png')
print(im.format, im.size, im.mode)

om = im.filter(ImageFilter.CONTOUR)
om.save('./resources/test.png')
