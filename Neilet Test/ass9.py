def word_count(sentence):
    words = sentence.lower().split()
    freq = {}

    for word in words:
        freq[word] = freq.get (word, 0) + 1

    return freq

s1 = "apple banana apple cherry banana apple"
s2 = "python is easy python is powerful"

print(word_count(s1))
print(word_count(s2))
 
