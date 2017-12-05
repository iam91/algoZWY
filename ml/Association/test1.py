from fp_growth import createHeaderTable
from fp_growth import createTree
from fp_growth import findCondPattBase
from fp_growth import findFreqItemSets

def loadDataSet():
    return [['r', 'z', 'h', 'j', 'p'],
            ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
            ['z'],
            ['r', 'x', 'n', 'o', 's'],
            ['y', 'r', 'x', 'z', 'q', 't', 'p'],
            ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]


if __name__ == '__main__':

    dataSet = loadDataSet()
    print dataSet
    print '-' * 10
    
    counts = []
    for i in range(len(dataSet)):
        counts.append(1)

    root, headerTable = createTree(dataSet, counts, minSupportCount=3)
    root.disp()

    print '-' * 10
    freq = findFreqItemSets(dataSet, minSupportCount=3)

    bench = [set(['y']), set(['y', 'z']), set(['y', 'x', 'z']), set(['y', 'x']),
        set(['s']), set(['x', 's']), set(['t']), set(['y', 't']), set(['x', 't']), set(['y', 'x', 't']), set(['z', 't']), set(['y', 'z', 't']),
        set(['x', 'z', 't']), set(['y', 'x', 'z', 't']), set(['r']), set(['x']),
        set(['x', 'z']), set(['z'])]

    # test
    assert len(bench) == len(freq), "number of freq set doesn't match"
    for b in bench:
        assert b in freq, 'wrong freq set'