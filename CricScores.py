# Fetches Live Cricket Scores from Cricbuzz after every 20 mins.
# This script is written in Python 3
''' You need to install requests and BeautifulSoup before you can use this script on your machine. Read the official documentation for installation : 
Request - http://docs.python-requests.org/en/master/user/install/
BeautifulSoup - https://www.crummy.com/software/BeautifulSoup/bs4/doc/ '''
from requests import get
from bs4 import BeautifulSoup
from re import compile # re is regular expression module, we will need this to parse one of the HTML tag.
from time import sleep # sleep is needed to pause the program for ten minutes.
from os import system # system is needed to clear the screen. Old scores will be wiped from screen and new will be displayed.
def split_print(string): # this is a utility function to separate team name from its score and print them as in the HTML code they are written without space.
	for i in range(0,len(string)):
		if ord(string[i]) >= 48 and ord(string[i]) <= 57: # ord returns the ASCII value of a character.
			break # we will look for a position where numbers start. The ASCII value of numbers lie between 48 to 57.
	print(string[:i]+' : '+string[i:len(string)]) # once the position is found we print the string.
while True:	# run the loop forever
	print("Wait while the scores are generated.....\n")
	page = get('http://www.cricbuzz.com') 
	text = BeautifulSoup(page.text,"html.parser") # text variable 'll be bound to a BS object returned by the BeautifulSoup function
	List = text.findAll('div',{'ng-if':compile(r'run_active == .+')}) # this is the tag that stores match scores by catagory ex - International.
	system('cls') # Clear your terminal screen. Note - system('cls') works for Windows, you have to use 'clear' instead of 'cls' on Unix platforms.
	for element in List:
		string = element['ng-if']
		position = string.find('\'')
		Position = string[position+1:].find('\'')+position+1 # extract the catagory name
		print('===============================> '+string[position+1:Position]+' <===============================\n\n')	# print catagory name
		List1 = element.findAll('div',{'class':'cb-col cb-col-25 cb-mtch-blk'}) # All match statistics (including title) are stored in this tag
		for number,item in enumerate(List1):
			Match_Title = item.find('a')['title'] # extract the Match Title i.e. : Match - [Match Number] Team A v Team B
			print("Match - ",number+1,Match_Title,' : ') # print the Match title
			bat = item.find('div',{'class':'cb-hmscg-bat-txt cb-ovr-flo '}) # The HTML tag with batting statistics
			bowl = item.find('div',{'class':'cb-hmscg-bwl-txt '}) # The HTML tag with batting statistics
			try: # send both batting and bowling statistics(statistics contains team name and score) to split_print function.
				split_print(bat.get_text())
				split_print(bowl.get_text())
			except:
				print("Sorry! Batting and Bowling Statistics Are Not Availaible") # sometimes scores are not availaible.
			result = item.find('div',{'class': ' cb-ovr-flo cb-text-live'}) # extract match result
			if result == None: # match result comes under two tags based on live or exclusive. The above one was for live.
				result = item.find('div',{'class': ' cb-ovr-flo cb-text-complete'}) # This one is for exclusive. If match is not live print this one.
			try:
				print("Match Result So Far: "+result.get_text())
			except:
				print("Sorry! Currently No Result Is Availaible For this Match!") # if neither of the two is present tell the users about it.
			print("") # empty string just for sake of cleaner display.
	sleep(600) # sleep for 1200 secs = 20 mins.		 
