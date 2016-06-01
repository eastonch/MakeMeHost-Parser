# MakeMeHost-Parser
Parser for MMH Website in Python with Tkinter GUI*...

# Why?
The in-game Warcraft 3 games list is poor, there's no filtering and it was never designed to support the multitude of custom games we have today, with this 10+ year old Real Time Strategy (RTS) game. 

Currently, avid Warcraft 3 players are using the MakeMeHost.com website to view a list of games `games.php` and copy and paste the game name into the warcraft 3 game to connect to the open game. The site currently does not offer any form of sorting or filtering ability and makes it difficult to copy and paste data as a horizontal tab is inserted into the cliboard which causes a server disconnect within Warcraft3.

This python script is intended for players to be able to quickly see games that are filling up on hosting bots so that they can join quickly, or to filter for a certain game type that they can join. Future developments may see parsing of Tournament and "Professional" realms. 


# Usage

`python mmh.py`\n
This will parse "http://makemehost.com/refresh/parse.php" once every 10 seconds, currently displaying all games that are NOT empty. 
Currently this will only show games that are hosted by ENT Gaming, MakeMeHost and their respective partner hosting bots. 


# Future Developments
* *Tkinter GUI 
* Ability to Copy / Paste / Modify clipboard
* Ability to set a trigger / alert for certain game types using Regex input perhaps? 
* Ability to sort, filter, groups for DOTA, LEGION, etc. 
* Optional multi-realm search (Garena, Legion TD)
* 
