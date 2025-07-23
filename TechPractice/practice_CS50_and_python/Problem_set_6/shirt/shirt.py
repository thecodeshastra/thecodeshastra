import sys
from PIL import Image
from PIL import ImageOps
import PIL
import os

def main():
    try:
        sysargv_check()
        imgBG = Image.open(sys.argv[1])
        imgpng = Image.open("shirt.png")
        whsize = imgpng.size
        imgpngresize = ImageOps.fit(imgBG, whsize)
        imgpngresize.paste(imgpng, imgpng)
        new_image = imgpngresize.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


def sysargv_check():
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) >= 4:
            sys.exit("Too many command-line arguments")
        elif os.path.splitext(sys.argv[2])[1] not in [".jpg",".jpeg",".png"]:
            sys.exit("Invalid output")
        elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
            sys.exit("Input and output have different extensions")
        else:
            return sys.argv[1], sys.argv[2]

if __name__ == "__main__":
    main()