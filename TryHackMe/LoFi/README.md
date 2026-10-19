# CTF writeup : LoFi

## 1. Challenge Information

- **Platfrom** [TryHackMe]
- **Challenge** [LoFi]
- **Category** [Web Hacking]
- **Difficulty** [EASY]
- **Date Completed** [18.10.2026]
- **Tools Used** [nmap, gobuster, firefox]


## 2. Objective

The goal of the challenge is to discover and capture the flag hidden in the website.

## 3. Initial Reconnaissance

I first nmap the Target IP address.

'''bash: nmap -sV -F -T4 <TARGET_IP>'''

***Explanation***

"-sV" is for version checking of the running services.

"-F" is for faster scan.

"-T4" is for more aggressive scan.

I found open ports in 22/tcp ssh and 80/tcp http .Their versions are

22/tcp => OpenSSH 8.2p1 Ubuntu 4ubuntu 0.4 (Ubuntu Linux;protocol 2.0)

80/tcp => Apache httpd 2.2.22 ((Ubuntu))

SSH login requires username and password, so we gonna look at the http now.

I went to the http site.

=> http://<TARGET_IP>

It is a website with youtube lofi music video.

## 4. Methodology

I first checked the source code of the website but nothing is found.
SO I checked the site with gobuster for further investigation.

'''bash: gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirb/common.txt '''

***Explanation***

=> 'dir' mean directory since we are finding hidden directories.

=> '-u' is for url link like http://<TARGET_IP>

=> '-w' is for wordlist to find the hidden directories from exiting words


I found nothing with gobuster.

***Analysis***

Since we found nothing on the website, we gonna have to use other techniques to capture flag.

## 5. Vulnerability Analysis

I research the website version on the exploit-db.com .
It is an old and vulnerable software especially to DoS/DDoS and SQL injections.


## 6. Solution

So I gonna use one of SQL injection techniques , Directory Transversal.
I searched in the root directory of the website for flag.

=> http://<TARGET_IP>/?pages=../../../../flag.txt

***Flag Found***

Yeah I found the Flag!!!


## 7. Lessons Learned

- I learned about the Directory Transversal, one of SQL injection techniques.
- I used nmap , gobuster, exploit-db.com .

## 8. Mitigation

In real world , websites should be the latest and secure versions of https instead of old http.


## 9. References

- Offical challenge Page : TryHackMe/room/LoFi
- Documentation
- Additional Resources : exploit-db.com
