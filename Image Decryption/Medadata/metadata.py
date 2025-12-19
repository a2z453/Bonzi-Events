#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from PIL import Image, PngImagePlugin

def hide_message_in_image(filename, message, output_filename):
    """Hide a message in PNG metadata"""
    img = Image.open(filename)
    meta = PngImagePlugin.PngInfo()
    meta.add_text("HiddenMessage", message)
    img.save(output_filename, pnginfo=meta)
    print(f"Message hidden in {output_filename}")

def show_message_from_image(filename):
    """Retrieve hidden message from PNG metadata"""
    img = Image.open(filename)
    hidden_message = img.info.get("HiddenMessage")
    if hidden_message:
        print("Hidden message:", hidden_message)
    else:
        print("No hidden message found in this image.")

if __name__ == "__main__":
    print("Mode options:\n  h: hide message\n  s: show message")
    mode = input("Choose mode (h/s) > ").strip().lower()

    if mode == 'h':
        filename = input("Enter source image filename > ").strip()
        message = input("Enter message to hide > ").strip()
        output_filename = input("Enter output image filename > ").strip()
        hide_message_in_image(filename, message, output_filename)

    elif mode == 's':
        filename = input("Enter image filename to read > ").strip()
        show_message_from_image(filename)

    else:
        raise Exception("[Error] invalid mode input!")
