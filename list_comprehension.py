evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# even squares from 1 to 10
even_squares = [x**2 for x in range(1,12) if x%2==0]

cubes_by_four=[x**3 for x in range(1,11) if x**3%4==0]
print cubes_by_four

