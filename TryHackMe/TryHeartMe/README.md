# TryHeartMe
## CTF writeup

- **Platform** : **TryHackMe**
- **Room : TryHeartMe**
- **Difficulty : Easy**
- **Category : Web, cookie**
- **Date Completed : 22.11.2026**

## Methodology
I use **cookies manipulation** and bypass **JWT Authentication** for hidden item and flag.

## Actions
### step 1
I go to the wesite from the instruction.

=> http://<TARGET_IP>:5000

It's a valentine gift shop site and I explore abit.

**Findings and Analysis**
I gobuster the site, I found hidden directories but nothing is that useful.

<img width="1280" height="800" alt="Screenshot_2026-11-22_19_19_40" src="https://github.com/user-attachments/assets/b0cdf907-7c7c-45cb-a8ef-7f6de95a9a00" />


I now gonna use burpsuite for investigation.
#
### step 2
I set the intercept on and sign up a new account.

<img width="1280" height="800" alt="Screenshot_2026-11-22_19_25_05" src="https://github.com/user-attachments/assets/d4085ed4-6561-4b49-aeaf-0b182e9847af" />


I get the cookie, => tryheartme_jwt=...

**Findings and Analysis**
I go to https://jwt.io and change from decoder to encoder.

<img width="1280" height="800" alt="Screenshot_2026-11-22_19_26_49" src="https://github.com/user-attachments/assets/fe458794-4143-4455-8ea4-f15b00fed792" />


I set the credit to 1000 for the test. I copy the jwt and paste it in website cookie area.

<img width="1280" height="800" alt="Screenshot_2026-11-22_19_27_33" src="https://github.com/user-attachments/assets/346793d9-a508-41d8-85c3-4fa984ad95f1" />

<img width="1280" height="800" alt="Screenshot_2026-11-22_19_31_03" src="https://github.com/user-attachments/assets/ab6f9aef-9652-4b7b-81c1-fb733a179ffa" />


I buy all the items but the instruction is about purphasing hidden item,'Valenflag', for the flag.
#
### step 3
Since I saw admin in gobuster, I gonna change user to admin, and I change the cookie.

<img width="1280" height="800" alt="Screenshot_2026-11-22_19_33_22" src="https://github.com/user-attachments/assets/05e8b780-9626-4fc4-9b0f-19c037e221d4" />


**Findings and Analysis**
I see the 'Valenflag' and purphase it to get the flag.

<img width="1280" height="800" alt="Screenshot_2026-11-22_19_33_51" src="https://github.com/user-attachments/assets/24405c64-4dfe-48ff-8c1c-c6367df5735d" />

<img width="1280" height="800" alt="Screenshot_2026-11-22_19_34_04" src="https://github.com/user-attachments/assets/0fb8ce4d-cff0-4295-911b-0def46761806" />


#
## Lessons Learned
**Cookie Manipulation, JWT Tampering, Privilege Escalation**
#
## Real-World Security Impact
- **Unauthorized Access** : Attackers can access admin only pages and information
- **Data Exposure** : Customer records, private documents, or business information become accessible
- **Data Manipulation** : Unauthorized modification of user accounts or business records
- **Account Takeover** : Other users' account may become vulnerable
#
## How developers should prevent it
- **Cryptographically verify JWT signatures**
- **Validate JWT expiration and relevant claims**
- **Never trust user-controlled role information**
- **Enforce authorization on the server for every sensitive endpoint**
- **Apply least-privilege access**
- **Rotate credentials and invalidate compromised sessions**
