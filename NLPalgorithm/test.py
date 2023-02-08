paragraph1 = "hello how are do you do"
paragraph2 = "you, me, he"


import nltk

print('NTLK version: %s' % (nltk.__version__))

from nltk import word_tokenize, pos_tag, ne_chunk

nltk.download('words')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('maxent_ne_chunker')


results = ne_chunk(pos_tag(word_tokenize(paragraph1)))
print('The sentence is : %s' % (paragraph1)) 
print()
for x in str(results).split('\n'):
    if '/NNP' in x:
        print(x)        

results = ne_chunk(pos_tag(word_tokenize(paragraph2)))
print(paragraph2)
print()
for x in str(results).split('\n'):
    if '/NNP' in x:
        print(x)