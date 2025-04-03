import sys
from PIL import Image

def decode_image(encoded_image_path):
    image = Image.open(encoded_image_path)
    width, height = image.size
    binary_message = ""
    for row in range(height):
        for col in range(width):
            pixel = image.getpixel((col, row))
            # Extract the LSB of each color channel
            for color_channel in range(3):
                binary_message += format(pixel[color_channel], '08b')[-1]

    # Adjust to handle the 16-bit end-of-message delimiter
    delimiter = "1111111111111110"
    message = ""
    for i in range(0, len(binary_message), 8):
        if binary_message[i:i+16] == delimiter:  # Check for the delimiter
            break
        char = chr(int(binary_message[i:i+8], 2))
        message += char

    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decode_image.py <encoded_image_path>")
        sys.exit(1)

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)


if __name__ == "__main__":
    main()