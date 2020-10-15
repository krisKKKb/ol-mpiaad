names = [line.split(',') for line in open("osalejad.txt")]
names = [line.strip() for line in open("osalejad.txt")]
print(names)
