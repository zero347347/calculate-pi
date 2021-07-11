# you have a function called random that generates a number from 0 to 1 randomly \n
# and its uniformly distributed now calculate the number pi
# hint: area of circle / area of square
# answer thought flow below
# 1st we know that the circle has a radius of 1, square has a length of 2
# do your math number of points in your circle / number of points in your square
# distance equation, circle area equation, square area equation
# n is the number of points

import random

    def estimate_pi(n):
        num_point_circle = 0
        num_point_square = 0
        for points in range(n):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            distance = x**2 + y**2
            if distance <= 1:
                num_point_circle += 1
            else:
                num_point_square += 1
        return 4 * num_point_circle/num_point_square

# remember this generates a random number uniformly
# so basically the higher the number the closest it gets to the actual pi 3,14159
    estimate_pi(10)
    estimate_pi(100)
    estimate_pi(1000)


