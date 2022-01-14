
import sys 
sys.path.append(r"c:\users\abina\appdata\local\programs\python\python39\lib\site-packages")
from PIL import Image ,ImageFilter
im = Image.open("./pokedex/astro.jpg")
im.thumbnail((400,400))
im.save("resized.jpg") 
