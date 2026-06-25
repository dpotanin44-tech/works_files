s = ['file1.txt', 'file2.txt', 'file3.txt']

with open('resource/combined.txt', 'w') as files:
    for f in s:
        with open(f, 'r') as i:
            files.write(f"=== Содержимое {f} ===\n")
            files.write(i.read())
            files.write("\n\n")
