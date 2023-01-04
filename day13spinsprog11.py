spins=[('red','19'),('black','12'),('red','9')
       ,('red','4'),('red','12'),('black','34'),('red','45'),
       ('black','19'),('black','40'),('red','6')]

def countReds( aList ):
    count=0
    for color,number in aList:
        if color=='black':
            yield count
            count=0
        else:
            count +=1
    yield count
gaps=[ gap for gap in countReds(spins) ]
print(gaps)
