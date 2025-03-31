# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
a='уеёэоаыяиУЕЁЭОАЫЯИЮ'
b=0
for letter in word:
    if letter in a:
         b+=1
print(b)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words=sentence.split()
print(len(words))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words=sentence.split()
for wordd in words:
    print(wordd[0])



# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sum_len=0
words=sentence.split()
for wordd in words:
    sum_len+=len(wordd)
print(round(sum_len/len(word),2))