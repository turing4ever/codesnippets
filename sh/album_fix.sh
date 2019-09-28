#!/bin/bash

# Unzip zip file download from google photo 
# Convert .heic -> .jpg, .mov -> .mp4 
# Remove .heic, .mov files 

function fix_one_album () {
    if [ ! -f "$1" ]; then
        echo "'$1' does not exist"
        exit 1
    fi
    filename=$(basename "$1")
    fname="${filename%.*}"
    ext="${filename##*.}"
    (set -x; unzip -q -o -d $fname $1)
    cd $fname
    mogrify -monitor -format jpg *.HEIC
    mogrify -monitor -format jpg *.heic
    for i in *.{MOV,mov}; do
        [ -f "$i" ] || break
        mov_filename=$(basename "$i")
        mov_fname="${i%.*}"
        (set -x; ffmpeg -loglevel panic -y -i $i "$mov_fname.mp4")
    done
    rm *.HEIC *.heic *.MOV *.mov
}

export -f fix_one_album

parallel --progress fix_one_album ::: "$@"
