#from tkinter import *
import numpy as np
import sys
import matplotlib.pyplot as plt
import numpy.linalg

#window = Tk()

numpy.set_printoptions(threshold=sys.maxsize)

CHUTES_LADDERS = {1:38, 4:14, 9:31, 16:6, 21:42, 28:84, 36:44,
                  47:26, 49:11, 51:67, 56:53, 62:19, 64:60,
                  71:91, 80:100, 87:24, 93:73, 95:75, 98:78}

def cl_markov_matrix(max_roll=6):

    # create the basic transition matrix
    mat = np.zeros((101, 101))
    for i in range(101):
        mat[i + 1:i + 1 + max_roll, i] = 1. / max_roll

    mat[range(101), range(101)] += 1 - mat.sum(0)

    # add chutes and ladders
    cl_mat = np.zeros((101, 101))
    ind = [CHUTES_LADDERS.get(i, i) for i in range(101)]
    cl_mat[ind, range(101)] = 1
    return cl_mat @ mat

    #print(np.linalg.matrix_power(fin_mat, 6))


mat = cl_markov_matrix()
plt.matshow(mat)
plt.grid(False)
plt.show()

#matrix = Label(window, text=str(cl_markov_matrix()))
#matrix.pack()
#print(cl_markov_matrix())
#window.mainloop()