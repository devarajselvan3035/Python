#!/bin/bash

filename=$(basename "$1")
extension="${filename##*.}"
# echo "$filename"
# echo "$extension"

# FileNames
python="py"
bash="sh"

case "$extension" in
"$python") python3 "$1" ;;
"$bash") bash "$1" ;;
*) exit 1 ;;
esac
