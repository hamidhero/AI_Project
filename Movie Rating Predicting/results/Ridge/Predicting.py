from ReadingRawData import *
from sklearn import linear_model

predicted_directors = {}

for item in directors.keys():
	number_of_movies = len(directors[item])

	parameter_1 = []

	for i in range(number_of_movies):
		parameter_1.append([i+1])

	parameter_2 = []
	sorted_by_year_list = sorted(directors[item], key=itemgetter(2))
	for movie in sorted_by_year_list:
		if movie[1] != 'N/A':							
			parameter_2.append(float(movie[1]))

	# print item
	# print movie[0]		
	# print parameter_1
	# print parameter_2
	clf = linear_model.Ridge (alpha = .5)
	clf.fit(parameter_1, parameter_2)
	predicted_next_movie_rate = clf.predict([number_of_movies + 1])
	predicted_directors[item] = predicted_next_movie_rate


predicted_actors = {}

for item in actors.keys():
	number_of_movies = len(actors[item])
	parameter_1 = []
	for i in range(number_of_movies):
		parameter_1.append([i+1])

	parameter_2 = []
	sorted_by_year_list = sorted(actors[item], key=itemgetter(2))
	for movie in sorted_by_year_list:
		parameter_2.append(float(sorted_by_year_list[i][1]))

	clf = linear_model.Ridge (alpha = .5)
	clf.fit(parameter_1, parameter_2)
	predicted_next_movie_rate = clf.predict([number_of_movies + 1])
	predicted_actors[item] = predicted_next_movie_rate



# print predicted_directors
# print predicted_actors['Ellar Coltrane']