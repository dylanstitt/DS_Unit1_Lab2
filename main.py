# Dylan Stitt
# Rat Gen
# Unit 1 Lab 2

import matplotlib.pyplot as plt

def readFile(filename):
    with open(filename) as file:
        content = [int(line) for line in file.read().splitlines()]
    return content


def graph(dataset):
    plt.plot(dataset)
    plt.xlabel('Generations')
    plt.ylabel('Weight (g)')


def main():
    mins = readFile('min.txt')
    avgs = readFile('avg.txt')
    maxes = readFile('max.txt')

    for dataset in [mins, avgs, maxes]:
        graph(dataset)

    plt.legend(['Min', 'Average', 'Max'])
    plt.show()


if __name__ == '__main__':
    main()