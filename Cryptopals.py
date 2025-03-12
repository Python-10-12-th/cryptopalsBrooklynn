#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 14:52:25 2025

@author: brooklynndominguez
"""

import base64

def hex_to_base64(h):
    byte_str = bytes.fromhex(h)
    return base64.b64encode(byte_str).decode()

def hex2bin(h):
    bin_out = ""
    for i in bytes.fromhex(h):
        bin_out += str(i)
        print(bin_out)
    print(bin_out)
    return bin_out

 
hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
bytes_data = bytes.fromhex(hex_string) 
base64_string = base64.b64encode(bytes_data).decode()  
 
print(base64_string)
 
 
 
def fixed_xor(hex1, hex2):
     bytes1 = bytes.fromhex(hex1)
     bytes2 = bytes.fromhex(hex2)
     
     xored_bytes = bytes(a ^ b for a, b in zip(bytes1, bytes2))
     
     return xored_bytes.hex()
 
hex_string1 = "1c0111001f010100061a024b53535009181c"
hex_string2 = "686974207468652062756c6c277320657965"
 
result = fixed_xor(hex_string1, hex_string2)
print(result)
 
b64vals = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789+/"
b64vals[7]
z=int.frombytes(bytes.from_hex("4d616e"))
