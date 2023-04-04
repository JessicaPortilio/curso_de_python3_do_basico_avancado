# Introdução ás Generator functions
# generator = (n for n range(100000000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return
        

gen = generator(n=5, maximum=100)
for n in gen:
    print(n)