import time

if __name__ == '__main__':
    f = lambda n : sorted(str(n))
    index = 1
    then = time.time()
    while not f(2 * index) == f(3 * index) == f(4 * index) == f(5 * index) == f(6 * index):
        index += 1
    print(index)
    print('time taken ', time.time() - then, ' seconds')
