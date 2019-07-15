#!/bin/bash

exiftool 2018.png | grep -oE "picoCTF{.*}"
