from fp_growth import createHeaderTable
from fp_growth import createTree


def loadDataSet():
    return [['r', 'z', 'h', 'j', 'p'],
            ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
            ['z'],
            ['r', 'x', 'n', 'o', 's'],
            ['y', 'r', 'x', 'z', 'q', 't', 'p'],
            ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]


if __name__ == '__main__':

    dataSet = loadDataSet()

    print createHeaderTable(dataSet)
    print '-' * 10
    root = createTree(dataSet, minSupportCount=3)
    root.disp()