#!/bin/bash

# Create and initialize a Python Environment Variable
echo "Creating virtual env - .venv"
python3 -m venv .venv

echo "Sourcing  virtual env - .venv"
source .venv/bin/activate

# Creating a directory to put things in =
echo "Creating 'setup' directory"
mkdir setup

# Moving the relevant files into the setup directory
echo "Moving function file(s) to setup dir"
cp *.py setup/
cd ./setup

# Installation Requirement
echo "pip installing requirements from requirement file into the target directory"
pip3 install -r ../requirements.txt -t .

# Prepares the deployment package
echo "Zipping package"
zip -r ../package.zip ./* 

# Remove the setup directory used
echo "Removing setup directory and virtual environment"
cd ..
rm -rf ./setup
deactivate
rm -rf ./.venv
# changing dirs back to dir from before
echo "Opening folder containg function package - 'package.zip'"
open .