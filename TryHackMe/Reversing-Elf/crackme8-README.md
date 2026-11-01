# Reversing Elf - crackme8
## CTF writeup
## Actions
### step 1
I download the file, make it executable and run it.

I get the usage output, so I try random password

=> ./crackme8 password12345

Ofcourse the output is 'Access denied'.
#
### step 2
I open ghidra on that program and explore and analysis its main fuction.

In seudocode, I find that input '-0x35010ff3' outputs 'Access granted'.

SO I immediately use that as password, the output is still 'Access denied'.
#
### step 3
I use python to convert that into decimal

=> python

and type that

=>> -0x35010ff3

and the output is '-889262067'.
#
### step 4
I use that as the password and run the program.

And I get the flag.

## Challenge Completed
