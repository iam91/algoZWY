from apriori import generate_one_item_set
from apriori import apriori

def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

if __name__ == '__main__':

    dataSet = loadDataSet()
    one = generate_one_item_set(dataSet)

    freq = apriori(dataSet)

    print freq