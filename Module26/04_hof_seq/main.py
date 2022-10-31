def hoftshadter_sequence(start, limit):
    if start != [1, 1]:
        return
    seq = start[:]
    counter = 1
    while counter <= limit:
        q = seq[-seq[-1]] + seq[-seq[-2]]
        seq.append(q)
        counter += 1
        yield q


for num in hoftshadter_sequence([1, 1], 33):
    print(num, end=' ')
