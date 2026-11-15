# Hidden Deep Into my Heart
## CTF write up

- **Room** : **Hidden Deep Into my Heart**
- **Platform** : **TryHackMe**
- **Difficulty** : **Easy**
- **Category** : **Web**
- **Completed Date** : **14.11.2026**

## Methodology
I used gobuster here to login as a admin and got the flag.
#
## Actions
### step 1
I go to the site from the instruction. It's a web page with some text.
**Findings and Analysis**
I use gobuster to find more hidden directories.I found /robots.txt.
It has a new directory,/cupids_secret_vault, and a string.
#
### step 2
I go to /cupids_secret_vault and the site says to discover more.
**Findings and Analysis**
I use gobuster again. I found a new directory, /administrator.
#
### step 3
I go to the /administrator directory and it's a login page.
**Findings and Analysis**
I use 'admin' and string from robots.txt to login and I got the flag.
#
## Challenge Completed

## Real WOrld security
The startups and small businesses should not leave sensitive information to publicly accessable site.

**This challenge is really good for beginner who start doing CTFs**
