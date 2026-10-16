# Python-Automation
To be more descriptive it's a form automation using selenium with a csv file to get info from and put it in the form

Selenium Form Automation
This project demonstrates my python automation skills still using selenium.
The script reads data from a CSV file and automatically fills out and submits forms on [QA Practice] (https://www.qapractice.com/practice-forms).

What does it do?

Reads form data from a CSV file.
Automatically fills in personal information and dropdown menus.
Selects a preferred communication method.
Submits the form for each person in the CSV file.
Returns to the form and continues with the next entry.

Built with

Python
Selenium library (Installed with terminal)
built in CSV library

How to use it:
1.Install python and google chrome and install any code editor

Pycharm
https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows

Visual studio code - (though you are going to have to install extensions to be able to use python on it)
https://code.visualstudio.com/Download?_exp_download=d53503e735

2. Install Selenium:
pip install selenium

If that doesn't work, try:
py -m pip install selenium

Put the given CSV (Site.csv) in the same folder which includes python file "Selenium-Form-Automation"
4. Run the script
in the terminal run
python Selenium-Form-Automation

The script will process each valid row, submit the form, and print the name of each person submitted in the terminal.

Why I made this?

I built this project to practice Selenium browser automation, working with CSV files, to organize repetitive tasks.
