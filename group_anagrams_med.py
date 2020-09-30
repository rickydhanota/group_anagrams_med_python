# Write a function that takes in an array of strings and groups anagrams together. Anagrams are strings made up of exactly the same letters, where order doesnt matter. For example, "cinema" and "iceman" are anagrams, similarily, "foo" and "ofo" are anagrams
# Your function should return a list of anagram groups in no parituclar order.

# sample input; 
#words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

# Sample output:
# output = [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]

def groupAnagrams(words):
    anagram = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagram:
            anagram[sortedWord].append(word)
        else:
            anagram[sortedWord] = [word]
    return list(anagram.values())
        
print(groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))