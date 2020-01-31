#!/bin/bash
# Ask the user for the comment in the commit
echo Please enter your command for the Git commit below
read commit
make git m=$commit
