# TryHackMe Agent-T  - CTF Writeup

## Challenge Information

- Platform : TryHackMe
- Room : Agent T
- Category : Beginner-friendly Penetration testing
- Focus : Exploiting via vulnerable web version
- Status : Completed

## Objective

To investigate Target machine , exploite, gain access and complete challenge.


## Methodology

1. Performed reconnaissance against the target machine.
2. Identified open ports and running services.
3. Investigated the running services.
4. Searched vulnerabilities from online sources.
5. Applied necessary exploitation to complete the challenge.
6. Documented the Findings and lessons learned.


## 1. Reconnaissance

### Objective

Scan the target machine IP for open ports and running services.
I am using nmap here.

### Command

'''bash : nmap -sV -T4 -F <TARGET_IP> '''

### Findings

I found port 80/tcp open , running http website with version of PHP cli server 5.5 or later (PHP 8.1.0-dev)

### Analysis

The only port open here is http , we have to use that for further exploitation.


## 2. Vulnerability Identification

### Observation

I don't see anything suspious from the website.

### Investigation

Now let's check the website source code.
Nothing useful is found for me.

### Conclusion

We can't find anything useful , so now let's move on to the next step.

## 3. Exploitation

### Objective

Since I cannot find the vulnerability , I gonna go check the exploit-db.com for more information.

### Steps

I search for the exact version of the website , PHP 8.1.0-dev, on exploit-db.com .
HEY look, I found the script for that version.

=> PHP 8.1.0-dev-'User agentt' Remote code execution

I copied that script and run it.

Then I add host url , http://<TARGET_IP>

### Result

BOOM!!! I got the shell!!
I check the access , it said root, SWEET.
checked what I can see.

''' bash : ls '''

I checked jason files, html files and javascript files , Nothing useful found.
Let's check everywhere to find flag.

''' bash : ls / '''

See I use 'ls /' instead of 'ls' , this is because we are root and going to the ~ directory.

HEYYY , I found flag.txt. Gonna cat it.
Important thing here is we can't 'cat flag.txt' , we gonna use

''' bash : cat /flag.txt '''

YEAHHHHH , we got the flag.


### Security Impact

In realworld system, we can't use old and outdated websites.
Attackers can easily exploit those websites and gain access to useful and sensitive information.


## Lessons Learned

- Improved my knowledge to exploit old , outdated systems.
- Learned to use online resources for exploitation.


## Conclusion

This challenge helped me practice the penetration-testing workflow, from initial reconnaissance to verifying results.


