def create_simplified_trie(words):
    trie = {}
    for word in words:
        curr = trie
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        # Mark the end of a word
        curr['#'] = True  
    return trie

str1 = "book1 book2 book3"
str2 = "book2 book3"
words1 = str1.split()
words2 = str2.split()
if len(words1) > len(words2):
    words1, words2 = words2, words1

words1_trie = create_simplified_trie(words1)

output = []
for word in words2:
    curr = words1_trie
    found_prefix = True
    for c in word:
        if c not in curr:
            found_prefix = False
            break
        curr = curr[c]
    if found_prefix and '#' in curr:
        output.append(word)

print(output)