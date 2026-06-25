rint("Примеры слов: авто, рыба, ель")

s = input("Введите слово для поиска: ")

with open("resource/text.txt", "r") as file:
    lines = file.readlines()

c = 0
n = []

for i in range(len(lines)):
    p = lines[i].count(s)
    if p > 0:
        c = c + p
        n.append(i + 1)
        print("Результат записан в файле")

with open("resource/search_results.txt", "w+") as result:
    result.write(f"Количество совпадений: {c}\n")
    result.write(f"В строках: {n}")
