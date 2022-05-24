import numpy as np
import matplotlib.pyplot as plt
import sys
import csv

from mandel import compute_mandel as compute_mandel_py
try:
    from mandel_cyt import compute_mandel as compute_mandel_cyt
except ImportError:
    pass

def plot_mandel(mandel):
    plt.imshow(mandel)
    plt.axis('off')
    plt.show()

def main(version='Python', NN=100):
    kwargs = dict(cr=0.285, ci=0.01,
                  N=NN,
                  bound=1.5)

    # choose pure Python or Cython version
    if version == 'Python':
        #print("Using pure Python")
        mandel_func = compute_mandel_py
    elif version == 'Cython': 
        #print("Using Cython")
        try:
            mandel_func = compute_mandel_cyt
        except NameError as ex:
            raise RuntimeError("Cython extension missing") from ex
    else:
        raise RuntimeError("Unknown version")

    mandel_set, runtime = mandel_func(**kwargs)
    return mandel_set, runtime
    
if __name__ == '__main__':
    #if len(sys.argv) == 2:
    #    mandel_set, runtime = main('cyt')
    #else:
    #    mandel_set, runtime = main()
    Ns = [100, 200, 300, 500, 700, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000]
    versions = ['Python','Cython']

	# field names 
    headResults = ['version', 'N', 'time (s)'] 
    newList = []
    
    for version in versions:
        for N in Ns:
            mandel_set, runtime = main(version, N)
            newList.append([version, N,'{0:5.2f}'.format(runtime)])
            #print('Mandelbrot set generated in {0:5.2f} seconds'.format(runtime))
            #plot_mandel(mandel_set)

    with open('results-A.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

		# write the header
        writer.writerow(headResults)

		# write multiple rows
        writer.writerows(newList)
    

