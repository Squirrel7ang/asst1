#!/usr/bin/python3
# coding=utf-8

import sys
from PIL import Image

def ppm_to_png(input_filename: str):
  if input_filename[-3:] != "ppm":
    exit(1)

  output_filename = input_filename[:-3] + 'png'
  try:
    img = Image.open(input_filename)
    img.save(output_filename, 'PNG')
    print(f"saving in {output_filename}")
  except Exception as e:
    print(e)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("usage: ppm2png.py <file-name>")
    exit(1)
  else:
    input_file = sys.argv[1]
    ppm_to_png(input_file)