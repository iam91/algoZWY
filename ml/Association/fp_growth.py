class Node(object):
    def __init__(self, item, count, parent):
        self.item = item
        self.count = count
        self.parent = parent
        self.next = None
        self.children = {}
        
    def disp(self, ind=1):
        print(' ' * ind + '{:s} {:d}'.format(self.item, self.count))
        for child in self.children.values():
            child.disp(ind + 1)


def createHeaderTable(dataSet, minSupportCount=1):
    headerTable = {}
    for transaction in dataSet:
        for item in transaction:
            headerTable[item] = headerTable.get(item, 0) + 1

    for item in headerTable.keys():
        if(headerTable[item] < minSupportCount):
            del headerTable[item] 
        else:
            headerTable[item] = [headerTable[item], None]

    return headerTable

def getSortedDataSet(dataSet, headerTable):
    for i, transaction in enumerate(dataSet):
        items = []
        for item in transaction:
            if item in headerTable:
                items.append(item)
        items.sort()
        dataSet[i] = items

    dataSetSorted = map(lambda x: \
        [[y, headerTable[y][0]] for y in x], dataSet)
    for i, transaction in enumerate(dataSetSorted):
        dataSetSorted[i] = \
            [y[0] for y in \
            sorted(transaction, key=lambda x: x[1], reverse=True)]
    return dataSetSorted


def createTree(dataSet, minSupportCount=1):
    headerTable = createHeaderTable(dataSet, minSupportCount)

    # TODO check number of header table
    dataSetSorted = getSortedDataSet(dataSet, headerTable)

    root = Node('null', 0, None)
    for transaction in dataSetSorted:
        updateTree(root, transaction, headerTable)

    return root


def updateTree(currNode, items, headerTable):
    firstItem = items[0]
    if(firstItem in currNode.children):
        currNode.children[firstItem].count += 1
    else:
        newNode = Node(firstItem, 1, currNode)
        currNode.children[firstItem] = newNode
        updateHeaderTable(firstItem, newNode, headerTable)
    if(len(items) > 1):
        updateTree(currNode.children[firstItem], items[1::], headerTable)
    
    return currNode 

def updateHeaderTable(item, newNode, headerTable):
    
    if(headerTable[item][1] == None):
        headerTable[item][1] = newNode
    else:
        currLink = headerTable[item][1]
        while(currLink.next != None):
            currLink = currLink.next 
        currLink.next = newNode
