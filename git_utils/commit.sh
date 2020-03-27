#!/bin/bash
# Creates commit with all changes.
# Adds branch name before message

# check your remote
remote=origin
message="$*"

branch_name=$(git rev-parse --abbrev-ref HEAD)
git add -A

if [[ $# -eq 0 ]]
then
    echo commit must has message
else
    git commit -m "$branch_name $message"

    if [[ $? -eq 0 ]]
    then
        echo commit successfully created
    else
        echo something went wrong, commit creation failed
    fi
fi
