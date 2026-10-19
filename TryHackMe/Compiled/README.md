# Compiled CTF - writeup

## Challenge Information

- **Challenge Name** : [Compiled]
- **Category** : [Reverse Engineering]
- **Tool Used** : [Ghidra]
- **Objective** : [To find the flag hidden in the given program]

## 1. Initial Analysis

First, I download the program from the room.
Then I put it in ghidra and analysed it.

I started the inspection in 'main' Function to understand how program works and find information about the flag.

## 2. Reverse Engineering

The program is about taking user input and outputing the user input with a string attached to it.

While examining the functions in Ghidra, I discovered a string containing the required flag.

So I investigated that part of decompiled code for the flag.


## 3. Finding the Flag

After investigating the required input and its output in Ghidra,
I found out that the flag is output of the specific string input.

Then I ran the program, typed the required input and

BOOM!! our flag.

## 4. Lessons Learned

- Learned how to inspect a compiled program using Ghidra
- Practiced examining the functions and decompiled code
- Discovered how strings can provide useful clues during reverse engineering
- Improved my ability to solve CTF challenges independently

## 5. Conclusion

This challenge gave me practical experience with basic reverse engineering.
I used Ghidra to examine the program, discovered the required input, and successfully retrieve the flag without any help.

## Tools Used : Ghidra | Reverse Engineering | CTF
