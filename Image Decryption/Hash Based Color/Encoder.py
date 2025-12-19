from PIL import Image

def text_to_colors(text):
    # Convert each character to 2-digit hex
    hex_str = ''.join([format(ord(c), '02x') for c in text])
    # Pad to multiple of 6
    while len(hex_str) % 6 != 0:
        hex_str += '00'
    # Split into 6-character chunks -> hex color
    colors = [f"#{hex_str[i:i+6]}" for i in range(0, len(hex_str), 6)]
    return colors

def create_color_image(colors, block_size=50, filename="color_blocks.png"):
    img = Image.new('RGB', (block_size * len(colors), block_size))
    for i, color in enumerate(colors):
        block = Image.new('RGB', (block_size, block_size), color)
        img.paste(block, (i*block_size, 0))
    img.save(filename)
    print(f"Saved color image as {filename}")

if __name__ == "__main__":
    text = input("Enter text to encode: ")
    colors = text_to_colors(text)
    create_color_image(colors)
    print("Encoding complete!")
