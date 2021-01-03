def isAnagram(word1, word2):
    s1 = list(word1)
    s1.sort()
    s2 = list(word2)
    s2.sort()

    return (s1 == s2)


if __name__ == "__main__":
    word1 = "fabiola"
    word2 = "aloibaf"
    valAnagram = isAnagram(word1, word2)

    print("%s | %s | Are anagrams? [ %s ]" % (word1, word2, valAnagram))
