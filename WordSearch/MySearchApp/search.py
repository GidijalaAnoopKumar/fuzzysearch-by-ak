import operator
#from operator import itemgetter

word_count = {}                           #dictionary
words = []
with open('word_search.tsv') as WSfile: 					#opening the given tsv file
	for eachline in WSfile:
		word, frequency = eachline.split('\t') 			#getting words and their occurance respectively.
		word_count[word] = int(frequency.strip())	#inserting into the wordcount dictionary {key,value} as {word,frequency} respectively..
		words.append(word)							#inserting word in words using append command.

#Search method to check the input word is present in any word of words list (even partial search).
def search_for_word(letters):
	all_words = []
	for word in words:
		if letters in word:
			all_words.append(word)
	return all_words

#SORTING method which meets the below requirements.
# 1. Exact matching word always tops result
# 2. Matching with the start of a word tops the list.
# 3. High usage words comes first than rarely used words(according to data given tsv file).
# 4. Short words first and then long ones.

def sort_words(all_words, partial_word):                                     #sorts the words based on a match with the search keyword.
	result_occured = [(result, result.find(partial_word), word_count[result], len(result)) for result in all_words]
	result_occured.sort(key=operator.itemgetter(1))                     #operator.itemgetter gets elements from a tuple.
	result_occured.sort(key=operator.itemgetter(3))
	searched_result = [result_occured[0] for result_occured in result_occured][:25]   # maximum of 25 elements to be displayed as per availablity.
	return searched_result
