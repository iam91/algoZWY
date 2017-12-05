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


def createHeaderTable(dataSet, counts, minSupportCount=1):
    headerTable = {}
    for i, transaction in enumerate(dataSet):
        for item in transaction:
            headerTable[item] = headerTable.get(item, 0) + counts[i]

    for item in headerTable.keys():
        if(headerTable[item] < minSupportCount):
            # remove infrequent items
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


def createTree(dataSet, counts, minSupportCount=1):
    headerTable = createHeaderTable(dataSet, counts, minSupportCount)
    if(len(headerTable) < 1):
        return None, None
        
    dataSetSorted = getSortedDataSet(dataSet, headerTable)

    root = Node('null', 0, None)
    for i, transaction in enumerate(dataSetSorted):
        updateTree(root, transaction, headerTable, counts[i])

    return root, headerTable


def updateTree(currNode, items, headerTable, count):
    firstItem = items[0]
    if(firstItem in currNode.children):
        currNode.children[firstItem].count += count
    else:
        newNode = Node(firstItem, count, currNode)
        currNode.children[firstItem] = newNode
        updateHeaderTable(firstItem, newNode, headerTable)
    if(len(items) > 1):
        updateTree(currNode.children[firstItem], items[1:], headerTable, count)
    
    return currNode 

def updateHeaderTable(item, newNode, headerTable):
    
    if(headerTable[item][1] == None):
        headerTable[item][1] = newNode
    else:
        currLink = headerTable[item][1]
        while(currLink.next != None):
            currLink = currLink.next 
        currLink.next = newNode

def findCondPattBase(condItem, headerTable):
    condPatt = []
    condPattCount = []
    linkNode = headerTable[condItem][1]
    while(linkNode != None):
        # traverse link list
        prefix = []
        treeNode = linkNode
        while(treeNode.parent != None):
            # traverse tree
            prefix.insert(0, treeNode.item)
            treeNode = treeNode.parent

        if(len(prefix) > 1):
            condPatt.append(prefix[:-1])
            condPattCount.append(linkNode.count)

        linkNode = linkNode.next
    return condPatt, condPattCount

def mineTree(headerTable, suffix, freqItemSet, minSupportCount):
    currSuffix = [x[0] for x in sorted(headerTable.items(), \
        key=lambda y: y[1][0])]

    for suff in currSuffix:
        newSuffix = suffix.copy()
        newSuffix.add(suff)
        freqItemSet.append(newSuffix)

        condPatt, condPattCount = \
            findCondPattBase(suff, headerTable)
        condTree, condHeaderTable = createTree(condPatt, \
            condPattCount, minSupportCount)
        if condTree != None:
            mineTree(condHeaderTable, newSuffix, freqItemSet, minSupportCount)

def findFreqItemSets(dataSet, minSupportCount=1):
    counts = []
    for i in range(len(dataSet)):
        counts.append(1)

    root, headerTable = createTree(dataSet, counts, minSupportCount)

    freqItemSet = []
    mineTree(headerTable, set([]), freqItemSet, minSupportCount)

    return freqItemSet
