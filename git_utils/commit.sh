#!/bin/bash
# Created by Artem Botnev on 03/19/2020

# creates commit with all changes.
# Adds branch name before message

# example of usage:
# current branch name is super_branch
# ./commit.sh 'it is new cool commit'
# will be created commit with message: super_branch it is new cool commit

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
