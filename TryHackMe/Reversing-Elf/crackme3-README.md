# Reversing Elf - crackme3

## CTF writeup

## Actions

### step 1
I download the file from the instruction and make it executable first.

If you look at the hint, we can see the challenge contain decoding.
#
### step 2
I run the file

=> ./crackme3

It require password so I use ltrace.

=> ltrace ./crackme3 password123456
#
### step 3
I then find strings in the program by this command

=> strings ./crackme3

I then observe the output.
#
### step 4
I found some code above 'Correct password!', it look like it requires decoding and since the hint is about decoding I copy that.

And I go to cyberchef.com , I use base64 decoding.

And I get the required flag.

## Challenge Completed

