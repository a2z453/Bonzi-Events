from PIL import Image

def colors_to_text(colors):
    hex_str = ''.join([c[1:] for c in colors])  # remove '#' and join
    # Convert each pair of hex digits back to char
    text = ''
    for i in range(0, len(hex_str), 2):
        char_hex = hex_str[i:i+2]
        if char_hex == '00':  # padding
            break
        text += chr(int(char_hex, 16))
    return text

def image_to_colors(filename, block_size=50):
    img = Image.open(filename)
    width, height = img.size
    colors = []
    for i in range(0, width, block_size):
        pixel = img.getpixel((i + block_size//2, height//2))  # sample center of block
        colors.append('#{:02x}{:02x}{:02x}'.format(*pixel))
    return colors

if __name__ == "__main__":
    filename = input("Enter image filename: ")
    colors = image_to_colors(filename)
    text = colors_to_text(colors)
    print("Decoded text:", text)
