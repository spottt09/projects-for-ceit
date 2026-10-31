# Digital Footprint - CTF writeup

- **Platform** : **TryHackMe**
- **Room** : **Digital Footprint**
- **Difficulty** : **Easy**
- **Category** : **OSINT**
- **Completed Date** : **31.10.2026**

## Instruction

This challenge is about using OSINT tools and metadata to search information.

## Methodology

I used metadata to search and complete the challenge.

## Actions

### step 1

I first download the file from the instruction , it is a image file called 'edited-house.jpg'.

Since the flag is city name, I use exiftool to search information about it.

bash:
        exiftool edited-house.jpg

**Findings and Analysis**

I got the latitude and longitude number, so I search them on google and found out the location is a city named
'Johannesburg'.

### step 2

For the second question about published date and time of ACME Jet Solution website ,

I just search 'ACME Jet Solution website release date and time' and the result is

Feburary 10, 2016 at 22:46:02 UTC.

### step 3

For the third question, asking about the english name of a landmark, I first downloaded the 'landmark.jpg'.

If you look at the question carefully, the question isn't about the name of middle building, it is about the building on the right side.

I use google image search to find the information.

**Findings and Analysis**

The name of the middle building is 'Spire of Dublin' officially titled as 'Monument of Light'.

But that's not what the question is about.

I open google map and go to the 'Spire of Dublin' and find the angle of the image I downloaded.

And once I got the angle, I look the right and the building is 'GPO', a museum liked building.

I search the google about the long form of GPO and the result is

'General Post Office'.

### step 4

For the final question, I download the file and open it.

It also has files, so I search the flag in them manually up to down.

I find a file I can use in Thumbnails directory, 'internal-doc.odt'.

I use exiftool to it.

**Findings and Analysis**

I useful at the buttom of the results.

        User-defined : markwilliams7243

Since the file says he will post the video , I fist go check the youtube and search that name.

I find a account and in that account description, I can see the Flag.

## Challenge Completed

## This challenge is a good beginner-friendly challenge that teaches OSINT and metadata information searching.
