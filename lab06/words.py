import os
import string
def read_words(filename):
    # se till att vi öppnar filen i rätt katalog (slå samman 
    # katalogen som scriptet ligger i med filnamnet på textfilen)
    filepath = os.path.join(os.path.dirname(__file__), filename)

    # öppna filen (utf-8 behövs för att hantera åäö rätt)
    file = open(filepath, encoding='utf-8')
    words_list = []

    for line in file:
        line = line.replace(",", "").replace(".", "").replace("!", "").replace('"', "").replace("'", "").replace(":", "").replace("?", "").lower()
        words = line.split()
        words_list.extend(words)

    return words_list





    # skriv ut filens innehåll

def count_only(words, provinces):
    dictionary = {}
    for i in provinces:
        dictionary[i] = 0

    for ord in words:
        if ord.lower() in provinces:
            dictionary[ord.lower()] += 1
    return dictionary

def count_all_except(words, stopwords):
    dictionary = {}
    for ord in words:
        if ord in dictionary:
            dictionary[ord] += 1
        elif ord not in stopwords:
            dictionary[ord] = 1
    return dictionary

def filter_hist(dict, min_count):
    top_words = {}
    for x, y in dict.items():
        if y >= min_count:
            top_words[x] = y
    return top_words

def sorted_hist(dict):
    list = [(y, x) for x, y in dict.items()]
    return sorted(list, reverse=True)
# -----------------------------------------------------------

# namnet på filen som ska läsas
filename = 'nilsholg.txt'

words = read_words(filename)

provinces = read_words('landskap.txt')

Landskap = count_only(words, provinces)




stopwords = read_words('undantagsord.txt')
Antal_ord_exklusive = count_all_except(words, stopwords)

for x in sorted_hist(Antal_ord_exklusive)[:10]:
    print(x)

print(filter_hist(Antal_ord_exklusive, 100))
print(len(filter_hist(Antal_ord_exklusive, 100)))