
RoBrutev6
=========

# Pythonista 3 Brute Force

[copyright (c) SavSec 2017](http://instagram.com/russian_otter)

# Brute Force
Inspect a login page for a website.
Locate the id for both the user and password box.
Enter the IDs into the arguments as listed in the program.
Then let it run.
***Syntax:***

-B -u `example.com/login.php` -l `welcome` --uid `user_id` --pid `pass_id` --usr `admin` -p `passes.txt`

# Force Speed
The speed depends on your internet connection and how
big the website login page is.

# FUZZER
RoBrutev5's new url fuzzer has the following.
***Syntax:***

-F -t `example.com/*` -f `fuzz.data` -m -r `0.5` -i `Welcome`

There are multiple uses for this, wether you want to test for urls or if you want to get a list of random values to throw at the site!

# SSH Brute Force
SSH Brute Force is an extremely fast brute force option for RoBrute! This option creates threads for every password so each password gets carred out by a thread, allowing for faster speed!
***Syntax:***

-S -i `ip address` -p `22` -u `admin` -P `basic.txt`

