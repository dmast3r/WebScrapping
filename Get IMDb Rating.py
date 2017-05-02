import omdb # to install omdb type in terminal pip install omdb and enter
import sys
from os.path import splitext
from os import listdir 

def movieInfo(movie_name):
	movie = omdb.title(movie_name)
	printInfo(movie, movie_name)

def printInfo(movie, movie_name):
	try:
		info_string = 'Tilte : '+movie.title+'\nYear : '+movie.year+'\nDirector : '+movie.director+'\nActors : '+movie.actors+'\n\nIMDb Rating : '+str(movie.imdb_rating)+ '  /  '+str(movie.imdb_votes)+' votes\n\nThis movie has also won following awards:\n' + movie.awards
		file = open(movie.title+'.txt', 'w')
		file.write(info_string)
	except Exception as e:
		print("Please recheck the name of this movie("+movie_name+"). Correct spelling mistake, if any.")

def removeUseless(full_name):
	useless_keywords = ['(', '{', '[', '-', '.', ' (', ' {', ' [', ' -', ' .'] # remove useless keywords present in the movie name.
	for kywrd in useless_keywords:
		if kywrd in full_name:
			return full_name[:full_name.find(kywrd)]
	return full_name

def main():
	for movie in listdir():
		root, extension = splitext(movie)
		if extension in [".avi", ".mp4", ".mkv", ".mpg", ".mpeg", ".mov", ".rm", ".vob", ".wmv", ".flv", ".3gp",".3g2"]: # check for all of these formats.
			movie_name = removeUseless(root)
			movieInfo(movie_name)

if __name__ == '__main__':
	main()
		
