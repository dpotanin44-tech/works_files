with open("resource/input.txt", "r") as file:

    s = len(file.readlines())
    print(f"Количество строк в файле: {s}")


    with open("resource/input.txt", "r") as file:


        c = 0
        for line in file:
            w = len(line)

            line = file.read()

            words = len(line.replace(" ", ""))

            c += 1

            print(f"Количество символов в строке {c}: {words}")
