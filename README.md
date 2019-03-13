# Interview Problem: Devin Noth's Solution
The solution I've written to the interview problem is written in Python. 
Both the two required subproblems as well as the two optional subproblems
are completed.

In terms of time organization, the first two required subproblems and 
the second optional subproblem were completed in the first hour, 
while the first optional subproblem of printing the information 
as an XML took about an hour on its own, due to personal inexperience 
with XML files and formatting. 

## Building and Running Instructions

The program has practically no building needed.
The easiest way to run the program through the command line is
and have it print the data as a JSON array is,

```
python main.py
```

Then to get the program to print the data in an XML format 
instead, simply add "XML" onto the command used above,
which would be,

```
python main.py XML
```

The following command is what I used to test my program through the 
jsonlint validator. Simply piping the original command that tells the
program to output a json array to the jsonlint validator.

```
python main.py | jsonlint
```

These were the main three commands I used to test and run my code 
and are the ones I would recommend using. You could use others if you
want such as running the program through the command

./main.py

This however could possibly be stopped through a permission denied error or 
some error that relates to running a python program without using the python 
command. To fix the permission denied error if you run into it, use the command

chmod +x main.py
