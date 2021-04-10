# Rolladice.py -- Work in Progress
A wrapper to simulate a dice rolling game similar to the rules of Yahtzee.

5 Dice will be rolled, the client will be playing against the house. 

Free to use, with no attribution under the MIT no attribution license.

The goal for this project is to use only built in libraries, and use best coding practices,
maintainability is key.

So far the project only uses Python's built in random library for use of randint. Other options will be explored to produce a more random outcome event.

The end project will include a sample Tkinker client. Networking may be implemented, depending on developer's interest in expanding the project.

Installation:
1. Create directory
2. git clone https://github.com/PipInstallCalifornia/Rolladice.git
3. cd into directory
4. py example.py




So far 'hands()' produces a dictionary following this schema:
{ "player": [1,2,3,4,5],
"dealer: [1,2,3,4,5] }
where the list 1,2,3,4,5 is produced from a call to random_hand() which invokes the random_int() function 5 times.

After hands() is invoked, a count of occurences must be called. The decision for this ranking logic is to count the occurences of a specific int in each respective hand. Example: [2,2,3,1,5] will produce a count_hands() of [1,2,1,0,1,0] where the correlated numbers are [1,2,3,4,5,6] respectively.

count_hands() requires the hands() dictionary object. It will return both the player's and dealer's occurences with matching schema to hands().

Once count_hands() object is returned, it will be scored. The scoring is as follows:

* No Hand (no matching numbers in the hand of 5) -- Base Score 0
* Example: hand: [1,2,3,4,6] occurences: [1,1,1,1,0,1]


* Pair (two numbers are matched in the hand of 5) -- Base Score 1
* Example: hand: [1,4,3,5,1] occurences: [2,0,1,1,1,0]


=== Todo ===

* Seperate game logic class, and gameloop files
* Seperate file into classes, rather than divided functions
* Code cleanup for maintainability

