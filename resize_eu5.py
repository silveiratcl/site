#!/usr/bin/env python3
"""
Resize eu5.png to a square format (320x320) by cropping from center
This creates a perfect circle when border-radius: 50% is applied
"""
from PIL import Image

input_file = "assets/images/eu5.png"
output_file = "assets/images/eu5.png"
target_size = 320

# Open the image
img = Image.open(input_file)
print(f"Original size: {img.size} (width x height)")

# Get the smaller dimension to crop to a square
crop_size = min(img.size[0], img.size[1])

# Calculate crop coordinates to center the crop
left = (img.size[0] - crop_size) // 2
top = (img.size[1] - crop_size) // 2
right = left + crop_size
bottom = top + crop_size

# Crop to square
square_img = img.crop((left, top, right, bottom))

# Resize to target size
square_img = square_img.resize((target_size, target_size), Image.Resampling.LANCZOS)

# Save the result
square_img.save(output_file, quality=95)

print(f"Cropped to square and resized to {target_size}x{target_size}")
print(f"File: {output_file}")
