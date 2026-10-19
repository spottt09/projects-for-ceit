# CTF write-up : [CyberHeroes]

## 1. Challenge Information

- **Platform** : [TryHackMe]
- **Challenge** : [CyberHeroes]
- **Category** : [Web]
- **Difficulty** : [Easy]

## 2. Objective

- To login to the account and capture the flag on website.

I check the website source code for username and password required to login.

## 3. Initial Reconnaissnace

I read the instruction on the official TryHackMe room.

It says the target machine is running the website on port 80.

## 4. Methodology

### step 1.

When I go to the website, the website has login page.

So as instict, I try SQL injection.

=> username' OR '1=TRUE

=> password' OR '1=TRUE

Ofcourse, It doesn't work.

### step 2.

Then I check the website source code.

I go to the login section of the source code.

Wait , I find it.

### step 3.

Look at the line 128, it says

=> if (a.value=='h3ck3rBoi' & b.value==ReverseString("54321@terceSrepuS))

**Analysis**

OK so we got the username and password to login.

But look carefully, username is Okay but password is in reverseString.

So the username is "h3ck3rBoi"and password become "SuperSecret@12345" .

## 5. Final Flag

So , I add the username and password to login page.

YAYYYY!!!!! I got the FLAGG!!!

## 6. Lessons Learned

- I learn to observe the source code of the website for investigation
