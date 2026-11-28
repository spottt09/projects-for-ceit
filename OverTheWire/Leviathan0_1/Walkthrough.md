## Leviathan
### Leviathan 0 to 1
- **Platform** : OverTheWire
- **Level** : Leviathan 0 to 1
- **Difficulty** : 6/10
- **Category** : Reverse Engineering
- **Completed Date** : 27.11.2026
#
### Method
I use wsl(Kali) to solve the challenge.

**Tools I used**:
- ltrace
- Strings
- ssh
- grep

### Actions
- **SSH into the lab machine via port 2223**
-- name : leviathan0
-- password : leviathan0
- **Find password for leviathan1 in .backup directory**
- **SSH login to leviathan1 with the password from leviathan0**
- **Run the challenge program**
- **Use strings for the first lookup**
- **Use ltrace for string comparing process**
- **Complete the challenge**

### Lesson Learned
- Reverse engineering basics and strings

### Addition
I also find password for leviathan2 in /etc/leviathan_pass/leviathan2

