words = ["jabloň", "kámen", "velbloud", "auto", "sklenice", "počítač", "vrabec", "víno", "elektrárna", "okouně", "racecar", "radar", "level"]
reverseWords = []

for word, reverseWord in zip(words, reverseWords):
    if word[::-1] == word:
        print(word)

# [start:stop:step] -> když provedu jen step tak se vyberou všechny znaky v daných krocích
                    # v případě [::-1] -> se bude postupovat od konce po 1