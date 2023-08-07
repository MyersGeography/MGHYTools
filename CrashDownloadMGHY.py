# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:09:43 2022
save to a C drive location to make it faster and avoid the "already exists repladce yes/no question on each download"
The weekly download list contains mostly reports we already have that need to be overwritten for some reason

This is python 3 code written and run in Eclipse/pyDev for Eclipse 

edit 3/1323
in chrome:
    go to chrome://settings/content/pdfDocuments
    set browser to auto download pdfs instead of auto open
    this downloads the pdf automatically, the code was edited to rename the auto downloaded pdf each time
    chrome://settings/content/pdfDocuments
    the clicking and pasting is no longer necessary
    also the script will stop if a download or script process errors

in chrome:
    settings, advanced, set download directory
    make it so PDFS dont auto open in bluebeam
    highlight red text with file name - EDITED 9/20/22 script will auto populate file name into clipboard
    control+c - EDITED 9/20/22 script will auto populate file name into clipboard
    click pdf download button - EDITED 9/20/22 script will auto click this button in a full screen chrome window
    control+v
    save

Sleep times are used to give the web page time to load before clicking the download button and to pause for manual interaction;
    at home on google fiber a sleep time of 2 seconds is sufficient
    at work an intial sleep time of 3.5 or more seconds is needed, sometimes pages take 10 seconds or more and the process will need to be stopped and rerun with an edited list

you can also add a breakpoint in the for loop and step through each one individually in debug mode, setting sleep time to 1 or 0

some files reference 2011 or older crashes that cant be queried in the TRS

copy downloaded files to \\citydata\public\MSO_Engr\KDOT\CrashReports

log into TRS at https://portal.kstrs.org/private/SimpleSearch.aspx

added pause after each 20 crashes for browser maintenance - decided to remove 4/26/2023

@author: kgonterwitz ... updated by cmyers
"""

import webbrowser
from time import sleep
import pyperclip
import os
from numpy import loadtxt


# ws = r'//citydata/public/MSO_Engr/KDOT/CrashReports/'
# move the list local while hte VPN is down
ws = r'C:/Users/cmyers/Downloads/crashdownload20230807/'
dl = r'C:/Users/cmyers/Downloads/crashdownload20230807/downloads/'

index = 0


######## INSTRUCTIONS TO RUN:
# the following text file must be formatted with no column headers ...
# ACCIDENT_KEY in the first column ...
# and REPORT_IMAGE_LINK in the second column
# be sure to set the Chrome download folder to somewhere local

text_file = ws + "Sorted_bits_export.csv"

lines = loadtxt(text_file, dtype=str, comments="#", delimiter=",", unpack=False)

for line in lines:
    index += 1
    file_name = str((line[0:1]))[2:13] + ".pdf"
    print(str(index) + " " + str(file_name))
    pyperclip.copy(file_name)
    print("Asking KDOT for " + str((line[1:2]))[2:10])
    # print("https://portal.kstrs.org/private/PDF.aspx?itemID=" + str((line[1:2]))[2:9] + "&VerNbr=1&rType=PDF&rSource=AccidentLib")
    url = "https://portal.kstrs.org/private/PDF.aspx?itemID=" + str((line[1:2]))[2:10] + "&VerNbr=1&rType=PDF&rSource=AccidentLib"
    webbrowser.open(url, new=0, autoraise=True)
    sleep(5)
    # click()
    os.rename(dl + 'PDF.pdf', dl + file_name)

