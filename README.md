# Form Automation

A Python + Selenium script that reads people's info from a CSV file and fills out and submits the practice form on [QA Practice](https://www.qapractice.com/practice-forms) for each one, automatically

## What it does

- Reads form data from a CSV file
- Fills in the personal info fields of students who passed
- Picks the preferred communication method
- Submits the form, goes back to it, and moves on to the next person in the file

## What you need to run it

- Python
- Google Chrome
- Selenium (the CSV library is built into Python)
- A code editor like [PyCharm](https://www.jetbrains.com/pycharm/download/) or [Visual Studio Code](https://code.visualstudio.com/Download) (VS Code needs the Python extension)

## Setup

1. Install Python, Chrome, and a code editor if you don't have them.
2. Install Selenium by typing this in the terminal:

```bash
   pip install selenium
```

   If that doesn't work, try:

```bash
   py -m pip install selenium
```

3. Clone or download this repo.
4. Make sure `Site.csv` is in the same folder as the Python file.

## The CSV file

The first row is a header and gets skipped. Every other row is one person, with the columns in this order:

```csv
Country,Title,first_name,Last_name,Date of birth,Date of joining,Email,Phone number,Prefered method of communication
```

The communication method should be `phone` or `email`.

## Running it

```bash
py form_automation.py
```

A Chrome window opens and fills out the form once per row. When a form is submitted, the script prints the name in the terminal:

```
Submitted: <first name> <last name>
```

## Why I made this

I built this Selenium automation project to automate a repetitive task: filling in the same form again and again.

## Need something similar?

If you need something like this for a different site or form, message me
