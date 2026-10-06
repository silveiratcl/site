#!/usr/bin/env python3
"""Check and compare image dimensions"""
from PIL import Image

# Check dimensions
eu4 = Image.open('assets/images/eu4.png')
eu5 = Image.open('assets/images/eu5.png')

print(f'eu4.png: {eu4.size} (width x height)')
print(f'eu5.png: {eu5.size} (width x height)')
print(f'\nAspect ratio eu4: {eu4.size[0]/eu4.size[1]:.2f}')
print(f'Aspect ratio eu5: {eu5.size[0]/eu5.size[1]:.2f}')
