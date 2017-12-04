class Node(object):
    def __init__(self, item, count, parent):
        self.item = item
        self.count = count
        self.parent = parent
        self.next = None
        self.children = {}

    def inc(self, count_delta):
        self.count += count_delta 


def createHeaderTable(dataSet, min_support_count=1):
    headerTable = {}
    for transaction in dataSet:
        for item in transaction:
            headerTable[item] = headerTable.get(item, 0) + 1

    for item in headerTable.keys():
        if(headerTable[item] < min_support_count):
            del headerTable[item] 
    
    return headerTable

def getSortedDataSet(dataSet, headerTable):
    dataSetSorted = map(lambda x: \
        [[y, headerTable[y]] for y in x], dataSet)
    for i, transaction in enumerate(dataSetSorted):
        dataSetSorted[i] = \
            [y[0] for y in \
            sorted(transaction, key=lambda x: x[1], reverse=True)]
    return dataSetSorted


def createTree(dataSet, min_support_count=1):
    headerTable = createHeaderTable(dataSet, min_support_count)

    # TODO check number of header table
    dataSetSorted = getSortedDataSet(dataSet, headerTable)

    root = Node('null', 0, None)
    for transaction in dataSetSorted:
        for item in transaction:

def updateTree(currNode, item):
    
    
    
    return currNode 
