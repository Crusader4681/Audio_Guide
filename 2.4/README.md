# Audio Tour Guide

## About
this is an audio tour app that uses eels, wxPython, GPSD and google maps API. the google maps api key is included so do not worry about generating your own nor do you need a GPS as there are 2 versions 1 with GPS one with out.
#
eel is a Python library for creating a front end for python using HTML, CSS and JavaScript.
wxPython is a Python library that is a cross platform GUI toolkit. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install wx and eels and GPSD if you're using a gps.

```bash
pip install eel wxPython
```
## GPSD Installation and Set-up (GPS with Linux only)
```bash
sudo apt-get install gpsd dpsd-clients 

sudo nano /etc/default/gpsd
```
then change replace the ttyXXX with the com port your computer is using

stty -F /dev/ttyXXX ispeed 4800 && cat </dev/ttyXXX
```bash
sudo apt install python-gi-cairo
```
then run xgps to see of your gps is working if it doesn't connect you may be out of line of site or you need to redo previous steps
```bash
pip3 install gpsd-py3
``` 
This is the python library for GPSD which allows us to pull data from the gps very easily 
THat should be done 
## Usage for non GPS

```
start via selecting tour guide,
then input user location ,
via imputing latitude and longitude into input boxes
then submit location and enjoy.
```
## With GPS
```
start via selecting tour guide,
then click get my location button and enjoy.
```