import argparse
from source import brightnessChange

def main():
    parser = argparse.ArgumentParser(description='Change lightness of a provided image.')
    parser.add_argument("--filepath", type=str, default='sky.jpg', help='Provide the input path of the image.')
    parser.add_argument("--lightness", type=int, default=10, help='Input the range of lightness (0 to 255).')
    args = parser.parse_args()
    bc = brightnessChange(file_path=args.filepath, lightness_value=args.lightness)
    bc.ImageBrightness()

if __name__ == "__main__":
    main()



