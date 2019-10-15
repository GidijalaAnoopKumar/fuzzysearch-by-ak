from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from .search import search_for_word, sort_words
import json

#renders the search page.
def search_view(request):
    return render(request, 'search.html', {})

#Returns the autocomplete results while the user types in a letter.
def search_partialword(request):
    if request.is_ajax():
        query = request.GET.get('term','')
        results = sort_words(search_for_word(query.lower()), query.lower())
        value = json.dumps(results)
    else:
        value = 'fail'
    type = 'application/json'
    return HttpResponse(value, type)

# Returns a jsonresponse having the search results upto 25 words containing the partially searched word.
def getSearchResults(request):
    if request.method == 'GET':
        query = request.GET.get('term')
        if query:
            Result = sort_words(search_for_word(query.lower()), query.lower())   #search from sorted words and also case sensitive.
            if len(Result) == 0:
                return JsonResponse({'Searched_Result': " No Result Found."})
            else:
                return JsonResponse({'Searched_Result': Result})
        else:
            return redirect('/')

