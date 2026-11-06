# Mustacchio
## CTF writeup
- **Platform** : **TryHackMe**
- **Room** : **Mustacchio**
- **Category** : **Hash cracking, Privilege Escalation, XXE injection**
- **Difficulty** : **Easy**
- **Completed Date** : **6.11.2007**
#
## Methodology and WorkFlow
I fist explore the web and get the credentials. Then use injection attack and ssh login.
And privilege escalation is used.
#
## Actions
### step 1
I first use nmap to the lab machine.
**Findings and Analysis**
I found open ports in ssh, 80/tcp http, 8765/tcp http.
#
### step 2
I go and check the 80/tcp http site, it's a site about men's facial hair.
To find hidden directories, I use gobuster to it.

=> gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirb/big.txt

**Findings and Analysis**
I found new directories, /custom, /fonts, /images, /robots.txt.
I explored all these and found something useful in /custom/js/users.bak.
I use strings on it and it has admin and hash. I have to crack it.
I go to crackstation.net and paste the hash, the result is 'bulldog19'.
#
### step 3
I then go to 8765/tcp http site, it's a login page.
I use 'admin' and 'bulldog19' as username and password.
I get to the page with user input box.
**Findings and Analysis**
I checked the source code and found a name 'barry' and a new file directory '/auth/dontforget.bak'.
I went to that directory and downloaded the file.
It is a XML file about Joe Hamd.
#
### step 4
I copy and paste the whole script form the dontforget.bak, and
the result is like the output of that script.
I gonna use XXE injection attack, so I search it on google.
You can use any payload you like and since github don't allow any payload, I just explain the process.
I copy the payload and paste in the script, change script as instruction.
And paste it in user input box of the site.
**Findings and Analysis**
I get a ssh key , I copy it and paste it in a file name id_rsa.
I have to make that ssh key usable now.
#
### step 5
I first locate ssh2john.py,

=> locate ssh2john.py

and I gonna demonstrate here by my device pathway.

=> /usr/share/john/ssh2john.py id_rsa > hash

and

=> john --wordlist=/usr/share/wordlists/rockyou.txt hash

**Findings and Analysis**
And the output is 'urieljames'.
I chmod it.

=> chmod 700 hash

Then ssh login by using it

=> ssh -i hash barry@<TARGET_IP>

And now we are in barry account.
And ls and I can get user flag.
#
### step 6
Now it's time for privilege escalation.
I explore to /home directory and see /barry and /joe.
In /joe, there is a program named 'live_log'.
It is like log tracker or something like that I don't know.
**Findings and Analysis**
If I run strings onto the live_log file, I can see tail files in it.
#
### step 7
I have to rely on youtube walkthrough for this challenge, here are the exact commands.

=> echo $PATH

=> cd ../../

=> cd /tmp/

=> touch tail

=> echo "/bin/bash" > tail

=> export PATH=/tmp:$PATH

=> chmod -x tail

Then go to the /home/joe directory and type

=> ./live_log

**Findings and Analysis**
Now I get the root access, go to the /root and I can see root.txt.
#
## Challenge Completed
**This challenge is really challenging for me**

