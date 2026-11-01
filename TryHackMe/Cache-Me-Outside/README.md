# Cache Me Outside
## CTF writeup

- **Platform** : **TryHackMe**
- **Room** : **Cache Me Outside**
- **Difficulty** : **Medium**
- **Category** : **Information gathering**
- **Date Completed** : **1.11.2026**

## Methodology
This challenge teaches metadata to search the required information.

## Actions
### step 1
I first download the image from the instruction, and check it in my device.
**Findings and Analysis**
The image contains a link and when I go there, it is a account of a person named 'Jim Lee' and his github account.

### step 2
I then go to the github account, it has a README.md.
I then go to commit section by adding '/commit' to original github repository URL.
**Findings and Analysis**
From the commit section, I see 'commit 7b2c8e0', so I copy that and add next to URL.
I then search its patch by adding '.patch' at the end.
So the whole url becomes something like

=> https://github.com/.../.../commit/7b2c8e0.patch
And I found his email account.

### step 3
I then send 'what is the phone number for CTF?' to that email account and
The reply is his phone number.

### step 4
I use sherlock on jiml33t(his github account) to find his social media accounts.

=> sherlock jiml33t

**Findings and Analysis**
I find his account on threads.com and he post a picture on that account.
I use google image search on that picture and the city's name is
'Timișoara' located in Romania.

### step 5
To find the tram station where he got off on 7th may, 2026, I just search the nearest tram station near the image.
**Findings and Analysis**
The tram station name is 'Piața Gheorghe Domășnean'.

## Challenge Completed


## Questions and Answers
- **What is the retired hacker's full name?**
- **Jim Lee**
##
- **What email address did he accidently exposed?**
- **jimleepro1@gmail.com**
##
- **What is his phone number?**
- **+40 743 321 239**
##
- **In which city is he located?**
- **Timișoara**
##
- **Submit the name of the tram station where he got off on the 7th of May,2026**
- **Piața Gheorghe Domășnean**
##

## This challenge is the first medium difficulty challenge and I really had a hard time solving it
