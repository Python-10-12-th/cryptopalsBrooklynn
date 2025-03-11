#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 14:52:25 2025

@author: brooklynndominguez
"""

 def hex2bin(h):
    bin_out = ""
    for i in bytes.fromhex(h):
        bin_out += str(i)
        print(bin_out)
    print(bin_out)
    return bin_out