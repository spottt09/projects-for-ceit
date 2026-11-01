# Reversing Elf - crackme7
## CTF writeup
## Actions
### step 1
I download the file, chmod it and run it.

It is a program with three options 'Say hello' , 'Add numbers' and 'Quit'.

I explore all of them and quit it.
#
### step 2
I go to the ghidra, import the program and observe it.

In main function, I see a string, 'Wow such h4x3r!'.

That's usually output of the correct process so I observe that area.
#
### step 3
In assembly and seudocode, I see that typing 0x7a69 outputs above text .

So I use google to find its decimal and its decimal is '31337'.

So I restart the program and just 31337 instead of the available options.

And I get the flag.

## Challenge Completed
