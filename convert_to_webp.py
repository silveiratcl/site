#!/usr/bin/env python3
"""
Convert PNG image to WebP format with optimization
"""
from PIL import Image
import os

# Input and output paths
input_file = "assets/images/header4_100dpi.png"
output_file = "assets/images/header4_100dpi.webp"

print(f"Converting {input_file} to WebP format...")
print(f"Original file size: {os.path.getsize(input_file) / 1024:.2f} KB")

# Open and convert the image
img = Image.open(input_file)

# Convert to WebP with quality optimization
# Quality 85 provides excellent quality with significant size reduction
img.save(output_file, "WebP", quality=85, method=6)

new_size = os.path.getsize(output_file) / 1024
original_size = os.path.getsize(input_file) / 1024
reduction = ((original_size - new_size) / original_size) * 100

print(f"✓ Conversion complete!")
print(f"New file size: {new_size:.2f} KB")
print(f"Size reduction: {reduction:.1f}%")
print(f"Saved to: {output_file}")
