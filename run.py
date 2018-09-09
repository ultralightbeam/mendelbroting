
import numpy as np
import matplotlib.pyplot as plt

def maps(z, c):
    
    return z * z + c


def main():

    num_iter = 10

    lim_axis = 5
    n_axis = 1000

    radius_bound = 10
    
    c_real = np.linspace(-lim_axis, lim_axis, n_axis)
    c_imag = np.linspace(-lim_axis, lim_axis, n_axis)
    M = np.zeros((n_axis, n_axis))
    for k_real in range(n_axis):
        for k_imag in range(n_axis):
            c = c_real[k_real] + 1j * c_imag[k_imag]
            z = 0. + 1j * 0.
            for k in range(num_iter):
                z = maps(z, c)
            if np.absolute(z) > radius_bound:
                M[k_imag, k_real] = 0
            else:
                M[k_imag, k_real] = 1
    plt.figure
    plt.imshow(M, clim=[0, 1])
    plt.colorbar()
    plt.show()
    
    

if __name__ == '__main__':
    main()
