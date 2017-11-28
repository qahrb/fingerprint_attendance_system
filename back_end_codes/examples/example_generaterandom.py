#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2017 Philipp Meisberger <team@pm-codeworks.de>
All rights reserved.

"""

from pyfingerprint.pyfingerprint import PyFingerprint


## Generates a 32-bit random number
##

## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

## Tries to generate a 32-bit random number
try:
    print(f.generateRandomNumber())

except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)
