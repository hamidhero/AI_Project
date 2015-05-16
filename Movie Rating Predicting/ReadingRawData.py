
from operator import itemgetter

file = open("RawDataCorrect.txt", "r")
dic = str(file.read())
code = compile(dic, '<string>', 'exec')
exec code


directors = {}
director = 'Director'
title = 'Title'
imdbRating = 'imdbRating'
year = 'Year'


for movie in dic.keys():
	if director in dic[movie].keys():
		if dic[movie][director] in directors.keys():
			directors[dic[movie][director]].append([dic[movie][title], dic[movie][imdbRating], dic[movie][year]])
		else:
			directors[dic[movie][director]] = [[dic[movie][title], dic[movie][imdbRating], dic[movie][year]]]



# for i in directors.keys():
# 	print i
# 	print directors[i]

# print directors['Quentin Tarantino']
# print len(directors)


actors = {}
actor = 'Actors'

for movie in dic.keys():
	if actor in dic[movie].keys():
		temp_list = dic[movie][actor].split(', ')
		actor_1 = temp_list[0]
		if len(temp_list) > 1:
			actor_2 = temp_list[1]


		if actor_1 in actors.keys():
			actors[actor_1].append([dic[movie][title], dic[movie][imdbRating], dic[movie][year]])
		else:
			actors[actor_1] = [[dic[movie][title], dic[movie][imdbRating], dic[movie][year]]]

		if actor_2 in actors.keys():
			actors[actor_2].append([dic[movie][title], dic[movie][imdbRating], dic[movie][year]])
		else:
			actors[actor_2] = [[dic[movie][title], dic[movie][imdbRating], dic[movie][year]]]

# for i in actors.keys():
# 	print i
# 	print actors[i]

# temp = actors['Jason Statham']
# print len(temp)
# print sorted(temp, key=itemgetter(2))

# print len(actors)


