# TryHackMe MD2PDF CTF-writeup

## Challenge Information

- Platform : TryHackMe
- Room : MD2PDF
- Category : Beginner Friendly Penetration Testing
- Focus : Exploiting via Cross Site Scripting (XSS)
- Status : Completed

## Objective

To get access to the flag hidden in the web page.


## Methodology

1. Performed reconnaissance against the target machine.
2. Identified open ports and running services.
3. Investigated the running services.
4. Applied necessary exploitation technique to complete the challenge.
6. Documented the Findings and lessons learned.



## 1. Reconnaissance

### Objective

Scan the target machine IP for open ports and running services.
I am using nmap here.


### Command

''' bash : nmap -sV -F -T4 <TARGET_IP> '''

WOAHHHH!! The version is really long, so I gonna do nmap scan again without identifying version.

''' bash : nmap -F -T4 <TARGET_IP> '''

### Findings

I found ports open in 22/tcp ssh , 80/tcp http and 5000/tcp upnp.


### Analysis

Since we need username and password for ssh login, we gonna use http web for this challenge.


## 2. Vulnerability identification

### Observation and Investigation

When I went to the website, the website has a program that convert text to pdf.
Then I use gobuster for more advanced web scanning.

### Command

''' bash : gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirb/common.txt '''

I found a directory name admin and went to check that directory by searching this

=> http://<TARGET_IP>/admin

It says "Forbidden , This page can only be seen internally (localhost:5000)" .

### Conclusion

Websites with user input box like this site are vulnerable to cross site scripting (XSS) and SQL injection.
We can use localhost:5000 for completing the challenge.



## 3. Exploitation

### Objective

I gonna use cross site scripting (XSS) to further exploitation.

### Steps

If you are familiar with web and proramming you might know about some basics of html, php and javascript.
Here we use that kind of principle.

 => <iframe src=http://127.0.0.1:5000/admin><'/frame'>

I have to write like this because github doesn't allow. Remove those 2 colons when executing. 

We have to use 'http://127.0.0.1:5000/admin' instead of 'http://<TARGET_IP>/admin' because we need to get the flag in localhost.
Most websites are host to localhost:5000 before hosting them in http or https site.


### Result

BOOM!! we got a flag!!!

## Security Impact

Website-developers should focus on handling strings to avoid XSS and SQL-injection.
Otherwise, sensitive information could be hacked.


## Lessons Learned

Cross-site-scripting (XSS)


## Conclusion

This challenge helped me practice the penetration-testing workflow, from initial reconnaissance to verifying results.

