# Fools mate - CTF writeup

- **Name** : **Fools mate**
- **Category** : **Web**
- **Difficulty** : **Easy**
- **Date completed** : **20.10.2026**
- **Tools used** : **BurpSuite**

## Instruction

The instruction says to win against the chess engine from the target website.

## Methodology

I use burpsuite to intercept the POSTs and get the flag.

## Actions

### step 1

I go to the target website , it is an easy chess puzzle.

### step 2

But whenever I make the checkmate move, I got the window telling me not to move that.

So I know I have to make the traffic to make the checkmate move.

### step 3

I open the BurpSuite and set the scope to 'http://<TARGET_IP>' in Target.

### step 4

I open the Proxy setting and set the Intercept ON.

Then I make a move.

### step 5

Since I set the intercept on, I capture the traffic .

I click a POST traffic and send it to Repeater.

### step 6

In repeater, I change to 'a1' and 'a8'.

for example ==> **from 'h2' to 'h3'** becomes **from 'a1' to 'a8'**

Then I click send. AND I got the flag.

## Conclusion

This challenge teachs me basics of burpsuite and intercepting traffic.
