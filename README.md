At Storemaven we track a lot of data, either from our UI, from 3rd parties services, scraping the web, and other methods. This data is being enriched and transformed in several pipelines before it is loaded into the final databases to serve the frontend and offline data procedures.

In this assignment, you will experience a very small portion of some of our flows. You will do so by implementing a data collector for a fictional organization, playing with Spotify’s API.

## General
Our fictional organization collects data about music from various categories and countries, and aims to figure out what’s the current musical trends worldwide.  
In this assignment, you will build a data collector that tracks data about Spotify’s top featuring songs.  
You will need to use Spotify’s API to find out what are the top featured playlists for a given category and country, and the songs that appear in these playlists.  
  
## Requirements
* Implement a method that collects data for the songs that appear in a Spotify’s given category.  
* The assignment deals only with the collection implementation, there is no need to store the data at this stage.  
* You will have to collect all the playlists for that category, and then for each playlist track info about the songs in that playlist.  
* The return value of that method will be a flat list of object, while each object represent a playlist track with the following data in it:  
  * General information about the track (id, name, artists). 
  * General information about the playlist this track was featured in (id, playlist name). 
  * The position of the track’s playlist in Spotify’s API results. 
  * The position of the track in the playlist it was featured on. 
* In order to assist you with the implementation we added to the assignment a basic template for you to use, with the desired object schemas and some basic tests to your output. 
  * The template uses Poetry for dependency management, but you can work with any other dependency management tool of your choice, the only dependency you’ll have to install is “pydantic”. 
* Feel free to use any other 3rd party library that will assist you with the solution, make sure to list that dependency somewhere in your solution (pyproject.py / requirements.txt files). 
* Do not use any Spotify’s client library, (such as spotipy), implement your solution using plain HTTP requests only.  
* Design and find your way for collecting the data in the fastest way possible.  

## General Guidelines
* You should implement your solution with Python 3. Any other implementation detail is up to you.  
* Write readable code. Apply Python's PEP 8 official coding standard as best as you can.  
* After you finish the implementation, send us your code and brief instructions for us to test it.  
* If you didn’t finish coding or have ideas on how to continue next please describe what was left and how you think it can be improved.  
* You can send the code back in an attachment or better share it using github.  
  
If you have any questions, feel free to contact us. Good luck! 
 							
						 					
				
			
		
