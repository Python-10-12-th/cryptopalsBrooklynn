#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 14:52:25 2025

@author: brooklynndominguez
"""
hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

binary_string = ''.join(f'{int(hex_string[i:i+2], 16):08b}' for i in range(0, len(hex_string), 2))


base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


base64_string = ''
for i in range(0, len(binary_string), 6):
    chunk = binary_string[i:i+6]
    if len(chunk) < 6:
        chunk = chunk.ljust(6, '0') 
    base64_string += base64_chars[int(chunk, 2)]
while len(base64_string) % 4:
    base64_string += '='

print(base64_string)

