Roblox has approximately 3 billion users, and 200 million users monthly. Also, your reason to disagree seemed to be you thinking that the thumbnail link has no connection to the user itself, rather than due to a time/storage concern or due to an issue with your method.\
I corrected you, that there is in fact a connection with the user, as a result, and in response you decided to be passive aggressive about it.\
\
Assuming there is a large database of icon links, OP would be correct that you could find a player within a game.\
Ignoring that, storing the links wouldn't take a ridiculous amount of storage either or be that long of a process. \
\
The main part of the thumbnail url is 32 bytes long, 32*3 billion is approximately 90 GB in storage. This is assuming that you are storing EVERY single users data and none of the users are banned or bots or inactive and this is uncompressed. Let's say there are 800 million active users who have played Roblox within the last 3 months, that is less than 30GB of storage. \
\
A dedi server could do 2m-3m requests per minute, rent a few out from an hourly cloud service provider and you have around 10m requests per minute. \
\
With that, it would take less than a day to scan those 3 billion users Roblox has. \
\
You could then filter it so that you routinely scan the user ids who have been active in the last few months.\
\
Lets say that is 800 million, it would take about 5 hours for your database to update to their latest thumbnail for all users which should be sufficient.\
This should give you a very good accuracy, and wouldn't be too expensive to sustain either. \
\
It would also be faster and more accurate to comparing each thumbnail against a reverse image search.\
\
Problems:\
\
Trying to iterate through 3 billion users\
When user changes their avatar\
Roblox ratelimits\
One icon link can link to multiple accounts (e.g, a bacon hair icon link is connected to multiple accounts, rendering searching for bacon hair avatars useless)\
\
The one icon link can link to multiple accounts is the main issue of this project and is why it has stopped\
Other attempts was to find out whatever this is\
![image](https://user-images.githubusercontent.com/89518595/162002832-602eacd6-62cc-4624-9f55-3f1a6db7aba6.png)\
either its pure gibberish or its not useful at all and they just trolled us
