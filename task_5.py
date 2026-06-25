with open('resource/words.txt', 'r') as f:
    words = [line.strip() for line in f if line.strip()]


alphabetical = sorted(words)


by_length = sorted(words, key=len)


reverse = sorted(words, reverse=True)


with open('resource/sorted_alphabetically.txt', 'w') as f:
    for word in alphabetical:
        f.write(word + '\n')

with open('resource/sorted_by_length.txt', 'w') as f:
    for word in by_length:
        f.write(word + '\n')

with open('resource/sorted_reverse.txt', 'w') as f:
    for word in reverse:
        f.write(word + '\n')

print("Создано 3 файла")
