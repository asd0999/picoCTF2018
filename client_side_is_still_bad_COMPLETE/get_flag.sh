#!/bin/bash

curl -s "http://2018shell.picoctf.com:8249/" | head -n 20 | cut -d "'" -f2 | tail -n 8 | rev | tr -d "\n" | rev
