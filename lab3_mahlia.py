# Mahlia | Lab 3 | Intro to Python

# Ticket 1
#username = "mayday_101"

#PREDICT: 10. I think that my handle is about 10 characters long.

#print(len(username))    

#EXPLAIN: len() counted every character, including the underscore symbol.

# Ticket 2
#print(username[0])

#print(username[len(username) - 1])

#PREDICT: I think that the two letters that will print are m and 1.

#EXPLAIN: the last index len(username) is minus 1 because we need to get the entire length of the code and we need to minus 1 to get it.

#Ticket 3
#first = " Welcome to Loop, "

#last = " @mayday_101! "

#ull = f"first + " " + last"

#PREDICT: I think that both lines will look idenitical on screen.

#print(f"{first} {last}" )

#print(full)

#EXPLAIN: the method that felt easiest to me is the concatenation method because it is faster to print out and I didn't have to add anything other than full to the print.

#Ticket 4
#username[0] = "X" 

#PREDICT: I think that the line will crash because it is not written properly and there is nothing for the terminal to run.

# NameError: name 'username' is not defined

#username = " MAYDAY_101 "
#print(username)
#EXPLAIN: Immutable in regards to a string means that object's value can't be changed once it is created.

#Ticket 5
#feed = [" chill for the win " , " 2cool4skool " , " sleep rules! "]

#PREDICT: I think that the number 3 will print for the count, and I think that "chill for the win" will be the first caption to print

#print(len(feed))

#print(feed[0])

#EXPLAIN: The index I used to get the first post was 0 because 0 represents the first item in the code.

#Ticket 6
#feed = [" chill for the win " , " 2cool4skool " , " sleep rules! "]

#feed.append(" boba is life ")

#PREDICT: I think that the index this new post will have is 3.

#print(feed)

#EXPLAIN: The fourth post sits at index 3 becuase we start from 0 and the first post is 0 so the last one is 3.

#Ticket 7
#feed = [" chill for the win " , " 2cool4skool " , " sleep rules! " , " boba is life "]

#feed.remove(" chill for the win ")

#PREDICT: I think that the first post will get removed. The order the rest will end up in is 0 1 2 
#print(feed)

feed = [' 2cool4skool ', ' sleep rules! ', ' boba is life ']

#feed.sort()
#print(feed)
#EXPLAIN: The methods I used were .remove and .sort. .remove gets rid of an item that you don't want to be in the ocde anymore, and .sort arranges the code by alphabetical order.

#Ticket 8
profile = {" username " : " @mayday_101 "  , " followers ": 250  , " verified" : "True if there is * "}

#PREDICT: I think that the follower number will print 250. I think that profile[0] does nothing because it isn't properly defined.

#print(profile[ " followers "])

#profile[0]
#NameError: name 'profile' is not defined. Did you forget to import 'profile'?
#EXPLAIN: Dictionaries look things up by key name because it is faster to do than looking it up by their index.

#Ticket 9
#profile[" followers "] = profile[" followers "] + 50

#profile[" bio "] = " just here for fun :) "

#print(profile)

#PREDICT: I don't think that .get("age") will print anything when the key is missing.

#profile.get(" age ")

#EXPLAIN: Using .get is safer than profile["age"] because when you use . the operation will pop up for you to see if it is there.

#Ticket 10

print(f"@{profile[' username ']} has {profile[' followers ']} followers and {len(feed)} posts. Top post: {feed[0]}")

#PREDICT: @mayday_101 has 300 followers and 3 posts. Top post: 2cool4skool

#EXPLAIN: I used profile, profile['username'], and profile['followers'] for the dictionary. I then used feed, len(feed), and fed[0] for the list.
