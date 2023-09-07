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

ROUND_OPTIONS = [
    ('GR', 'Group Stage'),
    ('R16', 'Round of 16'),
    ('QF', 'Quarter Finals'),
    ('SF', 'Semi Finals'),
    ('F', 'Finals')]

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

class Record:
    
    def __init__(self, description):
        self._description = description
        self._wins = 0
        self._draws = 0
        self._losses = 0
    
    def __init__(self, wins, draws, losses, description):
        self._wins = wins
        self._draws = draws
        self._losses = losses
        self._description = description
    
    def __str__(self) -> str:
        return f"{self._description}: {self._wins}-{self._draws}-{self._losses} ({self.win_percentage()})"
    
    def description(self):
        return self._description
    
    def num_wins(self):
        return self._wins
    
    def num_draws(self):
        return self._draws
    
    def num_losses(self):
        return self._losses
    
    def total(self):
        return self._wins + self._draws + self._losses
    
    def win_percentage(self):
        percent =  self._wins / self.total()
        return f"{percent:.3f}"

def compareRecords(r1: Record, r2: Record) -> bool:
    """
    A comparator function to be used to sort team Records. Returns True if r1 is strictly better than r2

    Args:
        r1 (Record): first team record
        r2 (Record): second team record
    """
    
    w1 = r1.num_wins()
    t1 = r1.total()
    w2 = r2.num_wins()
    t2 = r2.total()
    # first check by win percentage. We need to check if w1/t1 > w2/t2 iff w1*t2 > w2*t1
    if w1 * t2 > w2 * t1:
        return True
    elif w1 * t2 < w2 * t1:
        return False
    else:
        # now use the draw percentage to compare, so we need d1/(d1+l1) > d2/(d2 + l2) iff d1 * (d2 + l2) > d2 * (d1 + l1)
        d1 = r1.num_draws()
        l1 = r1.num_losses()
        d2 = r2.num_draws()
        l2 = r2.num_losses()
        if d1 * (d2 + l2) > d2 * (d1 + l1):
            return True
        elif d1 * (d2 + l2) < d2 * (d1 + l1):
            return False
        else:
            # at this point we simply need to check if the first record has more total games
            return t1 > t2

def make_comparator(greater_than):
    def compare(x, y):
        if greater_than(x, y):
            return 1
        elif greater_than(y, x):
            return -1
        else:
            return 0
    return compare