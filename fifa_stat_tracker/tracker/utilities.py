from random import randrange

BODY_PART_OPTIONS = [
    ('Foot', 'Foot'),
    ('Head', 'Head'),
    ('Left Foot', 'Left Foot'),
    ('Right Foot', 'Right Foot')]

POSITION_OPTIONS = [
    ('LF', 'Left Forward'),
    ('CF', 'Centre Forward'),
    ('RF', 'Right Forward'),
    ('LM', 'Left Midfield'),
    ('CM', 'Centre Midfield'),
    ('RM', 'Right Midfield'),
    ('LB', 'Left Back'),
    ('CB', 'Centre Back'),
    ('RB', 'Right Back'),
    ('GK', 'Goalkeeper')]

def mean(items):
    sum = float(0)
    for item in items:
        sum += item
    return sum / len(items)

def chooseRandomIndex(left, right):
    return randrange(left, right + 1)

def partition(items, left, right):
    randomPivotIndex = chooseRandomIndex(left, right)
    items[randomPivotIndex], items[right] = items[right], items[randomPivotIndex]
    pivot = items[right]
    pivotIndex = left
    # move items larger than the pivot to the right of the pivot
    for i in range(left, right):
        if items[i] > pivot:
            items[i], items[pivotIndex] = items[pivotIndex], items[i] # swap these 2
            pivotIndex += 1
    # swap pivot to the correct location
    items[right], items[pivotIndex] = items[pivotIndex], items[right]
    return pivotIndex
            

def findKthLargestRec(items, k, left, right):
    pivotIndex = partition(items, left, right)
    if (pivotIndex == k - 1):
        return items[pivotIndex]
    else:
        if pivotIndex < k - 1:
            return findKthLargestRec(items, k, pivotIndex + 1, right)
        else:
            return findKthLargestRec(items, k, left, pivotIndex - 1)

def findKthLargest(items, k):
    return findKthLargestRec(items, k, 0, len(items) - 1)

def median(items):
    return findKthLargest(items, (len(items) + 1)//2)