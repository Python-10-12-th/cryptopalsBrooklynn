#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 12:32:34 2025

@author: brooklynndominguez
"""

import unittest
import Cryptopals
input_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
final_str = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
 
class Test(unittest.TestCase):
    def test_hex2byte_valid(self):
       input_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
       expected_output = bytes.fromhex(input_str)
       self.assertEqual(Cryptopals.hex2byte(input_str), expected_output)
    def test_hex2byte_empty_string(self):
            self.assertEqual(Cryptopals.hex2byte(""), b"")
    
    def test_hex2byte_invalid_hex(self):
        with self.assertRaises(ValueError): 
            Cryptopals.hex2byte("ZZZ")
 
if __name__ == "__main__":
     unittest.main()
     