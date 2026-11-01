# Reversing Elf - crackme2

## CTF writeup

## Actions
### step 1
I first download the file from the instruction and make it executable

=> chmod +x crackme2
#
### step 2
I then run that file

=> ./crackme2

And I get the usage guide

=> Usage: ./crackme2 password
#
### step 3
I use ltrace to find more information about password of the program.

=> ltrace ./cracme2 123456pass

'123456pass' is just a dummy password for test.
#
### step 4
OHH the output contains the password I'm looking for, 'super_secret_password'.

And I use that password

=> ./crackme2 super_secret_password

And I get the flag.

## Challenge Completed
