import sys
from memeocr import MemeOCR

def main(argv):
    if len(argv) != 2:
        print 'usage:'
        print '    python main.py meme-file-name'
        return

    meme_fname = argv[1]
    ocr = MemeOCR()
    txt = ocr.recognize(meme_fname)
    print txt

if __name__ == '__main__':
    main(sys.argv)

