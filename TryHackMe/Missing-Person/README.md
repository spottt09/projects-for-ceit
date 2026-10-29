# Missing Person
## CTF write-up

- **Platform** : **TryHackMe**
- **Room** : **Missing Person**
- **Category** : **OSINT, information detecting**
- **Difficulty** : **Easy**
- **Date Completed** : **28.10.2026**


## Objective
This challenge is about finding information of a person who went to vacation in 2025 by using OSINT tools on two photos.

## Actions

### step 1

I download the file as the instruction and unzip it.

It is two photos, 'food.jpg' and 'MotoGP.jpg'.

The fist question is about name of this circuit?

SO, I look toward the MotoGP.jpg, I can see the name, 'PERTAMINA'.

I search that name on google and found out this is form 'Pertamina Mandalika International Circuit',
which is held in Indonesia in 2025.

### step 2

For the date of that race, I search 'Pertamina indonesia 2025 date'.

And the date was '3 to 5 october'.


### step 3

For the name of the restaurant, I use google search to food.jpg

and the result is 'Cantina Mexicana'.

### step 4

To find out the time of the food.jpg taken, I use exiftool

'''bash: exiftool food.jpg'''

and the date and time was 2025:10:05 and 19:55:30.

### step 5

For location of the bar that held after party, I use google map.

I ask the google map AI, 'Which bar or restaurant held after-party at Pertamina MotoGP 2025?' .

And the result is 'Surfer's Bar', so I just search for its location.

### step 6

For the name of the DJ at that after-party, I search 'Surfer's Bar indonesia 2025 october DJ'.

The name of the DJ is 'Bong Leleh'.

### step 7

For the name of cave the friend went with the DJ the next day, I search

'Bong Leleh 2025 cave travel'.

And the cave was 'Gua Sumur'.

### step 8

FOr the business number of Bong Leleh, I just search

'Bong Leleh Tour Business number'

and the result is '085333137345'.

## Challenge Completed

**This Challenge teaches me how to use google more effictively and efficiently.**

