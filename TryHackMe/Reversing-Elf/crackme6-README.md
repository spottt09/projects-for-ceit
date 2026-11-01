# Reversing Elf - crackme6

## CTF writeup

## Actions
###  step 1
I download the file, chmod it and run it.

I get the usage,

=> Usage: ./crackme6 password
#
### step 2
I open the ghidra and import the program to analysis.

I observe it and find some useful in main funciton.

The program wrote its password in separate line, if they combine, the full password becomes '1337_pwd'.

I add that to the answer box and it is correct.

## Challenge Completed
