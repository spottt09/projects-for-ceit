# 'W1se Guy' CTF writeup

- **Platform** : TryHackMe.com
- **Category** : Hashing
- **Difficulty** : Easy
- **Other platform** : cyberchef.com


## Instruction

The instruction says the target server has listening port on 1337.

## Goals

- to capture the Flag1 and Flag2

## Actions

### step 1

I join the server hosted by the target via netcat.

=> nc <TARGET_IP>  PORT

It give me the XOR encoded text for flag1 but I need the login key for netcat.

### step 2

For now, I got the XOR encoded text flag 1, but since it is encoded we have to decode it.

### step 3

I copy the hash and go to the cyberchef.com .

### step 4

I choose magic as a recipe to know better about the hash.

It says matching ops are : from base64, from Base 85, from hex , from hexdump Valid UTF8.

### step 5

I copy the first 8 letters of the hash and paste it in key,
while the recipe is set to XOR.

### step 6

I type "THM{" in the input box since most of the flag come in this form.

### step 7

I copy the output from step6 and paste it in XOR key box.

### step 8

Now I put 'from Hex' recipe on top of the XOR .
Then change the XOR scheme from Hex to UTF8.

### step 9

I paste the whole hash into the input box and now come bruteforcing.

### step 10

Add a character or number to key box from step7,

For EXAMPLE==> **if the key from step7 is Lnou, you should change it like Lnou1 or Lnou2 or Lnoua or Lnoub**

Keep chaning the key until the output look something like

==> THM{..................}

### step 11

If you found the right key and the flag has legit form,
paste the flag in flag1 box.

Now You complete the flag1 part.


### step 12

Then copy the key that work and paste it in the netcat login key.

BOOM !! I got the flag2 and the challenge is completed.

## Challenge completed
