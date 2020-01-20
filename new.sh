#!/bin/bash

# TODO:
# * When copying template.md to solution directory, replace any name values with solution name
# * Likewise, set initial values for some of the other files, like 'Done'.
# * Or better yet, take the leetcode URL and generate the markdown template from the HTML
# * Handle if extenstion has leading period

function usage() {
cat <<END_USAGE
A script to create a new practice problem.

usage: new.sh PROB_NAME EXT

    PROB_NAME           The name of the problem to create. Will be used
                        For the name of the directory, and the solution file.
    EXT                 The extension of the solution file to creation. For example,
                        '.py', or '.rs'. Pass without period.
END_USAGE
}


# Check problem name argument isn't null
if [ -z "$1" ]
then
    echo "error: PROB_NAME is required."
    usage
    exit 1
fi


# Check solution file extension argument isn't null
if [ -z "$2" ]
then
    echo "error: EXT is required."
    usage
    exit 1
fi


# main
solution_dir="$PWD/$1"
solution_file="$solution_dir/${1}.${2}"
mkdir $solution_dir
touch $solution_file
cp "./template.md" "$solution_dir/README.md" 
