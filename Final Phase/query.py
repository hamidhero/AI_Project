from Predicting import *
import math

file = open("RawData_2014only.txt", "r")
dic = str(file.read())
code = compile(dic, '<string>', 'exec')
exec code

count = []
relative_error = []
def predict(movie):
	result = []
	if movie in dic.keys():
		director = dic[movie]['Director']
		actors = dic[movie]['Actors'].split(', ')
		if len(actors) > 2:
			actor_1 = actors[0]
			actor_2 = actors[1]
			actor_3 = actors[2]
		elif len(actors) > 1:
			actor_1 = actors[0]
			actor_2 = actors[1]
		else:
			#print 'Not Enough Info ! less than 2 actors'
			return 
		writers = dic[movie]['Writer'].split(', ')
		writer_0 = writers[0].split(' (')
		writer = writer_0[0]
		
		if director in predicted_directors.keys():	
			a = float(predicted_directors[director][0])
		else:
			#print 'Not Enough Info ! director first experience'
			return
		
		if actor_1 in predicted_actors.keys():
			b = float(predicted_actors[actor_1][0])
		else:
			#print 'Not Enough Info ! actor_1 first experience'
			return

		if actor_2 in predicted_actors.keys():	
			c = float(predicted_actors[actor_2][0])
		else:
			#print 'Not Enough Info ! actor_2 first experience'
			return
		if actor_3 in predicted_actors.keys():
			d = float(predicted_actors[actor_3][0])
		else:
			return

		if writer in predicted_writers.keys():
			e = float(predicted_writers[writer_1][0])
		else:
			return

		result.append(a)
		result.append(b)
		result.append(c)
		result.append(d)
		result.append(e)
		# print a
		# print b
		# print c

		predicted_rating = math.ceil((.3*a + .4*b + .2*c + .05*d + .05*e)*10)/10
		result.append(predicted_rating)
		#print result
		if len(result) == 6:
			count.append(dic[movie]['Title'])
			print str(len(count))+'. '+dic[movie]['Title']
			print 'Predicted Rating = '+str(result[-1])+'			'+'IMDB Rating = '+dic[movie]['imdbRating']
			print ''
			relative_error.append(abs(result[-1] - float(dic[movie]['imdbRating'])) / float(dic[movie]['imdbRating']))
	# else:
	# 	print 'No Such Movie !'




for movie in dic.keys():
	predict(movie)

the_mean_relative_error = 0
for item in relative_error:
	the_mean_relative_error = the_mean_relative_error + item	

print 'The Mean Relative Error = '+str(float(the_mean_relative_error / len(relative_error)) * 100)+' %' 