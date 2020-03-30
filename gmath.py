import math
from display import *


def make_vector(a,b):
    return [
        b[0] - a[0],
        b[1] - a[1],
        b[2] - a[2]
    ]


#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt(vector[0] * vector[0] + 
                          vector[1] * vector[1] + 
                          vector[2] * vector[2])
    for i in range(len(vector)):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    p = 0
    for i in range(3):
        p = a[i] * b[i] + p
    return p

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons):
    A = make_vector(polygons[0],polygons[1])
    B = make_vector(polygons[0],polygons[2])

    print([
        A[1] * B[2] - A[2] * B[1],
        A[2] * B[0] - A[0] * B[2],
        A[0] * B[1] - A[1] * B[0]
    ])
    return [
        A[1] * B[2] - A[2] * B[1],
        A[2] * B[0] - A[0] * B[2],
        A[0] * B[1] - A[1] * B[0]
    ]
    # s = 0
    # for i in range(len(polygons)):
    #     polygons
