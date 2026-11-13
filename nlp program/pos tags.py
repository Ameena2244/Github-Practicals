import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The cat is playing"

words = nltk.word_tokenize(sentence)

result = nltk.pos_tag(words)

print(result)
