# Lian_Yu
## CTF write-up

- **Platform** : **TryHackMe**
- **Room** : **Lian_Yu**
- **Difficulty** : **Easy**
- **Category** : **Web, hash cracking, privilege escalation**

## Methodology Or Flow

Reconnaissance => hash => privilege escalate

## Actions

### step 1

I first nmap it.

'''bash: nmap -sV -T4 -F -Pn <TARGET_IP>'''

**Findings and Analysis**

I find open ports in ssh, ftp and http.

I go and check the http website, it is a website about the 'ARROWVERSE'.

### step 2

I use gobuster to the site for information.

'''bash: gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirb/big.txt'''

**Findings and Analysis**

I find a directory named '/island', so I check there.

The site give me a code, 'vigilante'.


### step 3

If you look at the first question, it is about the hidden directory but in number.

SO,For more information I gobuster it again but this time I use number wordlist.

'''bash: gobuster dir -u http://<TARGET_IP>/island -w /usr/share/seclists/Fuzzing/4-digits-0000-9999.txt'''

**Findings and Analysis**

I found a directory, '/2100', so I add it to the answer box of the related question.

I then go and check the new directory.

The web page is a text,'How Oliver Queen finds his way to Lian_Yu?', and a youtube video link.

And a text saying 'You can avail your .ticket here but how?'

### step 4

To find the ticket,I use gobuster again. And I find a file named '/green_arrow.ticket'.

I go to the site , http://<TARGET_IP>/island/2100/green_arrow.ticket .

And Download the file, It has a code.

But it is encrpyted, so I go to the cyberchef.com and decrypt it.

**Findings and Analysis**

The code is decrypted by 'From Base58' and it is '!#th3h00d'.

I answer the question, 'What is the file name you found?', with 'green_arrow.ticket'.

### step 5

Now I gonna login to ftp server as vigilante and !#th3h00d as password.

'''bash: ftp <TARGET_IP>'''

and enter username and password. I am in ftp server and check files by 'ls -la'.

**Findings and Analysis**
I see Leave_me_alone.png, Queen's_Gambit.png, aa.jpg, .other_user and .profile.

I download all of them.

### step 6

Then I use xxd to Leave_me_alone.png but I need just the top one line to edit the png signature so

'''bash: xxd Leave_me_alone.png | head -n 1'''

Then I search png signature on google.

The signature is '89 50 4E 47 0D 0A 1A 0A'.

I use hexeditor on Leave_me_alone.png and

'''bash: hexedit Leave_me_alone.png'''

and type the signature and Ctrl+S to save and hit enter and Ctrl+X to exit.

**Findings and Analysis**

Then I see the picture change and the text say, 'Just leave me alone Here take what you want password'.

SO 'password' is for something.


### step 7

Then for aa.jpg, I use steghide

'''bash: steghide --extract -sf aa.jpg'''

and I add 'password' since that is the only information I now have.

**Findings and Analysis**

OK I now have 'ss.zip', I unzip it and it has 'password.txt' and 'shado'.

I cat 'password.txt', it doesn't give me enough information.

But for 'shado', I get a code 'M3tahuman'.

I assume that password for the ssh since that is the only vulnerability we have left.

### step 8

Then I cat '.other_user', the file is about the person named 'Slade Wailson' who became metahuman.

I gonna login to ssh as 'slade' now,

'''bash: ssh slade@<TARGET_IP>'''

and then add 'M3tahuman'.

OK I am in slade account.

**Findings and Analysis**

I then check files by ls and find user.txt.

I cat it and get user flag.

Now for root flag, I have to escalate my privilege to root.

### step 9

I type

'''bash: sudo -l'''

and add 'M3tahuman' since we don't know the root password.

At the bottom of the result,

=> (root) PASSWD : /usr/bin/pkexec

I copy it and search it on google, On GTFOBin.com,the vulnerability is called CVE-2021-4034.

Its root privilege can be escalate by this command,

'''bash: sudo pkexec /bin/sh'''

or

'''bash: sudo -u root /usr/bin/pkexec /bin/bash '''

**Findings and Analysis**

And I get the root access.

Then ls and see root.txt and I cat it.

## Challenge COmpleted

