# Reversing Elf - crackme5

## CTF writeup

## Actions

### step 1

I download the file and make it executable and run it.

The goal here is to get the ouput 'Good game'.

I get the input box, so jut 'pass1234'.

The output is 'Always dig deeper'.
#
### step 2

I use ltarce

=> ltrace ./crackme5

and add 'pass12345'.
#
### step 3

At the end of the output, I see

strncmp funciton and a code. Usually strncmp and strcmp are used for comparing strings in password requring programs like this one.

So I copy that code and start the program.

=> ./crackme5

and enter the code. The output is 'Good game'.

## Challenge Completed

