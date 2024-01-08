#!/bin/bash

echo "Total:"
cat README.md \
    | grep ':white_check_mark:' \
    | wc -l
echo ""

echo "Difficulties:"
cat README.md \
    | grep -i ':white_check_mark:' \
    | grep -Eo '(Easy|Medium|Hard)' \
    | sort \
    | uniq -c
echo ""

echo "Languages:"
cat README.md \
    | tail -n +3 \
    | awk -F "|" '{print $4 }' \
    | awk NF \
    | sort \
    | uniq -c \
    | sort -r
echo ""

echo "Categories:"
cat README.md \
    | tail -n +3 \
    | awk -F "|" '{print $7 }' \
    | awk NF \
    | sort \
    | uniq -c \
    | sort -r
echo ""

