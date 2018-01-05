def purify(numbers):
    lst=[]
    for n in numbers:
        if n%2==0:
            lst.append(n)
    return lst


print purify([1,2,3])
