import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print()

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens: 
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go", "Hello, there is my car", "I\'ve lost my car in my car",
"I\'d like my boat back", "I will name my dog Diana"]
print()

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
print()

# web_sm has less similarites from the same statements in comparision to the use of web_md. This comes down to the lack of word vectors being used which lead to less accurate results from the same pieces of code.