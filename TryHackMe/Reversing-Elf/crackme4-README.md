# Reversing Elf - crackme4

## CTF writeup

## Actions

### step 1
I download the file and make it executable and run it.

=> ./crackme4

I get the Usage

=> Usage: ./crackme4 password

And it says the string is hidden and it use strcmp(string compare).

### step 2

SO I use strings on that

=> strings ./crackme4 password123456

And the result contains password.

## Challenge Completed
