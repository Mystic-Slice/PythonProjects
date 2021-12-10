from pyzbar.pyzbar import decode
from PIL import Image
d = decode(Image.open("Not_a_meme.png"))
print(d[0].data.decode())