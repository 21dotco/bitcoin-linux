# Bitcoin Linux

This repository provides two servers and two command-line programs, all
which can be used independently of each other.  Instructions for using
both sets of programs are described below:

## General setup

    ## Clone this repository using HTTPS or SSH
    ## If you use HTTPS GitHub access
    git clone https://github.com/stanford-bitcoin/bitcoin-linux.git
    ## If you use SSH keys
    git clone git@github.com:stanford-bitcoin/bitcoin-linux.git

    ## Enter the bitcoin-linux directory
    cd bitcoin-linux

## CLI: `img2txt21`

The `img2txt21` program takes a JPEG image and converts it to text.
To install:

    ## Enter the img2txt21 directory from the bitcoin-linux directory
    cd img2txt21

    ## Install img2txt21 as a command
    sudo pip3 install --editable .

Now you can run img2txt21 as you would any other system command:

    ## With a file
    img2txt21 image.jpg

    ## In a pipeline
    cat image.jpg | img2txt21

Note that img2txt21 defaults to buying optical character recognition
services from an endpoint running on the local computer.  To change what
endpoint it uses, edit it and re-run.


## CLI: `translate21`

The `translate21` command takes text input and converts it to Chinese.
To install:

    ## Enter the translate21 directory from the bitcoin-linux directory
    cd translate21

    ## Install translate21 as a command
    sudo pip3 install --editable .

Now you can run translate21 as you would any other system command:

    ## With a file
    translate21 file.txt

    ## In a pipeline
    cat file.txt | translate21

Note that translate21 defaults to buying translation services from an
endpoint running on the local computer.  To change what endpoint it
uses, edit it and re-run.

Translate API on the text provided it. The Google API requires
registering an API key and creating a paid account with a credit card
(debit cards not accepted).

## CLI `pep8_21`

The `pep8_21` command takes a python file and performs [PEP8](https://www.python.org/dev/peps/pep-0008/) linting.
To install:

    ## Enter the translate21 directory from the bitcoin-linux directory
    cd pep8_21

    ## Install pep8_21 as a command
    sudo pip3 install --editable .

Now you can run pep8-21 as you would any other system command:

    ## With a file
    pep8_21 file.py

Note that translate21 defaults to buying translation services from an
endpoint running on the local computer.  To change what endpoint it
uses, edit it and re-run.

## Translation Server

To create an API key, go to the [Google Developers
Console](https://console.developers.google.com) and login with your
Google account.  Then create a project (you can give it any name), go to
*Credentials*, and create credentials for a server API key.  Save the
API, you'll need it later.

After creating credentials, click *Enable and manage APIs*, and choose
the Translate API.  After enabling translate, go to the Billing screen
and click *Create billing account*.  Enter your payment details.

Now you can perform the technical setup:

    ## Enter the translate21 directory from the bitcoin-linux directory
    cd translate21

    ## Install the dependencies
    sudo pip install -r requirements.txt

    ## Set your API key in an environmental variable
    export GOOGLE_TRANSLATE_API_KEY=YOUR_KEY

    ## Run the server
    python3 translate-server.py

## Server: OCR server

The Optical Character Recognition (OCR) server uses the Tesseract OCR
engine on the local device to turn an image into text.  To install:

    ## Enter the img2txt21 directory from the bitcoin-linux directory
    cd img2txt21

    ## Install a JPEG library and tesseract-ocr
    sudo apt-get install libjpeg9-dev tesseract-ocr

    ## Intall the Python dependencies
    sudo pip install -r requirements.txt

    ## Run the server
    python3 server.py

## Server: PEP8 server

    ## Enter the translate21 directory from the bitcoin-linux directory
    cd pep8-21

    ## Install the dependencies
    sudo pip install -r requirements.txt

    ## Run the server
    python3 pep8-server.py
