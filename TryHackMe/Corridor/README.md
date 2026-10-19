# CTF writeup : [Corridor]

## 1. Challenge Information

- **Plaform** : [TryHackMe]
- **Challenge** : [Corridor]
- **Category** : [Web hacking , hash-cracking]
- **Difficulty** : [Easy]
- **Date Completed** : [18.10.2026]
- **Tools Used** : [nmap , gobuster]

## 2. Objective

The challenge is about finding the hidden flag in hash website directory one by one.

## 3. Initail Reconnaissance

- Target : <TARGET_IP>
- Open ports or services : 80/tcp http
- version : Werkzeug httpd 2.0.3 (Python 3.10.2)

## 4. Methodology

### step 1.

**Command**

'''bash : nmap -sV -F -T4 <TARGET_IP> '''

**Observation**

I found http service opening on port 80.
I went to the website, It is just an image ,and there is nothing in source code.


**Analysis**

I found out that version of http web service is old and vulnerable on goole.

### step 2.

I use gobuster to further investigation.

**Command**

'''bash: gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/common.txt '''

**Observation**

Even with  the gobuster I found nothing.

**Analysis**

So I have to check the website manually.
HEy I found a directory in website, the directory looks like a hash.

### step 3.

I copied that directory and checked that with hash-identifier.

**Command**

'''bash: hash-identifier'''

and pasted the directory.

**Obervation**

Yeah it is a hash and it says MD5.

**Analysis**

I went to the crackstation.com for hashcracking.

I pasted the hash and cracked it.

It also said MD5 but the result is 9.

So I had to try adding every MD5 hash of 0 to 9 next to the website url to find flag.

### step 4.

Now let's go to cyberchef.com , we gonna try every hash starting from zero.

I add 0 to input box with MD5 hash on.

I got a long cracked hash, and pasted it next to the url.

HEYY HEYYY!!! FLAGG!!


## 5. Vulnerability Analysis

- **Vulnerability** : [IDOR vulnerability]
- **Root cause** : [websites missing object level authorization]
- **Impact** : [Attacker can get access to sensitive information]


## 6. Solution

nmap => expore website => crackstation.com => cyberchef.com => FLAG

## 7. Lessons Learned

- IDOR vulnerability
- I made mistake of just scanning websites instead of exploring the websites.

## 8. References

- Official challenge page : TryHackMe
- My Official Documentation
- Additional learning resources : exploit-db.com , crackstation.com , cyberchef.com
