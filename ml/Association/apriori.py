def generate_one_item_set(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            item = frozenset([item])
            if not item in C1:
                C1.append(item)
    return C1

def generate_k_item_set(k_minus_one_item, k):
    ret = []
    n = len(k_minus_one_item)
    for i in range(n):
        for j in range(i + 1, n):
            a = list(k_minus_one_item[i])
            b = list(k_minus_one_item[j])
            a.sort(); b.sort()
            if a[:k - 2] == b[:k - 2]:
                ret.append(k_minus_one_item[i] | k_minus_one_item[j])
    return ret

def get_frequent_item_set(dataSet, candidate_item_set, min_support_count):
    counts = {}

    for transaction in dataSet:
        for candidate in candidate_item_set:
            if candidate.issubset(transaction):
                if candidate in counts:
                    counts[candidate] += 1
                else:
                    counts[candidate] = 1

    ret_item_set = []
    support_count = []
    for candidate, count in counts.iteritems():
        if count >= min_support_count:
            ret_item_set.append(candidate)
            support_count.append(count)

    return ret_item_set

def apriori(dataSet, min_support=0.5):
    """
    create frequent item set
    """
    # initialize
    frequent_item_sets = []    
    min_support_count = len(dataSet) * min_support
    dataSet = map(set, dataSet)
    
    # create one item set
    one_item = generate_one_item_set(dataSet)
    freq_one_item = \
        get_frequent_item_set(dataSet, one_item, min_support_count)
    
    # compute frequent k item set
    k_minus_one_item = one_item
    for k in range(2, len(one_item)):
        k_item = generate_k_item_set(k_minus_one_item, k)
        if(len(k_item) < 1):
            break
            
        freq_k_item = get_frequent_item_set(dataSet, k_item, min_support_count)

        k += 1
        frequent_item_sets.append(freq_k_item)
        k_minus_one_item = freq_k_item

    return frequent_item_sets