from PIL import Image
from style_transfer.learn import StyleTransfer
import sys

style_transfer = StyleTransfer()
artwork = style_transfer(Image.open(sys.argv[1]), Image.open(sys.argv[2]))
artwork.save(sys.argv[1],)