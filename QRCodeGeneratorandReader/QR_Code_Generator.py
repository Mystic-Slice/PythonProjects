import qrcode

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size = 20,border = 2)

qr.add_data("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
qr.make(fit = True)

img = qr.make_image(fill_color = 'black',back_color = 'white')
img.save("Not_a_meme.png")

'''import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("Hello World!",image_factory = factory)
svg_img.save("dont_know_what_svg_is.svg")'''
 
