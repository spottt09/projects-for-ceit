# CTF Write up : [Dig Dug]

## 1. Challenge Information

- **Platform** : [TryHackMe]
- **Chllenge** : [Dig Dug]
- **Category** : [Web Domain Exploitation]
- **Date Completed** : [19.10.2026]
- **Difficulty** : [Easy]
- **Tools Used** : [dig , nslookup]

## 2. Objective

The challenge is to capture the flag hidden in the domain.

I used passive reconnaissance tools to find the required flag.

## 3. Initail Reconnaissance

I read the instruction on the room , it says

**Target is a DNS server**
**It only responds to a special type of request for a 'givemetheflag.com' domain**

## 4. Operaton

### step 1

I first use 'dig' since it says it is a DNS server.

**Command**

'''bash: dig <TARGET_IP>'''

**Observation**

It provides some information but that is not enough for now.

**Analysis**

We gonna have to use other tools and techniques.


### step 2

I will use 'nslookup' now.

I searched syntax for the nslookup.So it gonna be like this

**Command**

'''bash: nslookup -type=A givemetheflag.com <TARGET_IP> '''

## 5. Finding Flag

Yayyy!!! I found the flag.

## References

- Official challenge page : TryHackMe/Dig Dug

