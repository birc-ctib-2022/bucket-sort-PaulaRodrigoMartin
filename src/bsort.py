"""Module for bucket sorting."""

from platform import java_ver
from typing import Any


def count_keys(keys: list[int]) -> list[int]:
    """
    Count how many times we see each key in `keys`.

    You can assume that all elements in `keys` are
    non-negative. This is not a requirement for
    bucket sort in general--it can handle negative
    numbers--but it is a little more complicated and
    we will keep it simple here.

    You should return a list, `counts`. The list you
    return should have `len(counts) == max(keys) + 1`
    so we can index into any key (including those
    that might not be included in `keys`) and for each
    key `0 <= k <= max(keys)` `counts[k]` should be
    the number of times `k` occurs in `x`.

    The function should take time `O(len(keys))` and
    not more.

    >>> count_keys([1, 2, 2, 1, 4])
    [0, 2, 2, 0, 1]
    """
    # we can get the number of keys from keys if
    # it is non-empty. Otherwise we must assume that
    # there are no keys.
    no_keys = max(keys) + 1 if keys else 0 #length of keys
    counts = [0] * no_keys #counts is a list of 0s of length of keys
    # print(keys)
    # FIXME: count the keys
    for i in keys:
        counts[i] += 1
    return counts

print(count_keys([1, 2, 2, 1, 4]))



def count_sort(x: list[int]) -> list[int]:
    """
    Sort the values in x using count sort.

    The values in x must satisfy the constraints
    mentioned in `count_keys()`.

    >>> count_sort([])
    []
    >>> count_sort([1, 2, 1, 2, 4])
    [1, 1, 2, 2, 4]
    """
    counts = count_keys(x)
    out = [0] * len(x)

    ## to iterate over the whole list, could also put --> for i in range(len(counts)-1)
    ## this is to iterate over the list, but I don't know how to put it into "out"
    for i in range(1,len(counts)): 
        ## to assess the index and the value to start (float("inf") is a very big number to start, could also be 99999999... and it would work, but to make sure)
        min_idx, min_val = 0, float("inf")
        ## to iterate over the list and find the smalles number
        for j in range(i, len(counts)):
            if counts[j] < min_val:
                min_idx, min_val = j, counts[j]
        ## and change the minimum value with the first position         
        counts[i], counts[min_idx] = min_val, counts[i]
    ## i don't know how to put the values to another list "out", instead of ordering them in the same list
    return counts

print(count_sort([1, 2, 1, 2, 4])) #-->[0,0,1,2,2]

def cumsum(x: list[int]) -> list[int]:
    """
    Calculate the cumulative sum of x.

    >>> cumsum([1, 2, 3])
    [0, 1, 3]
    >>> cumsum([0, 2, 2, 0, 1])
    [0, 0, 2, 4, 4]
    """
    out = [0] * len(x)
    # FIXME: Compute the cumulative sum
    
    return out


def bucket_sort(x: list[tuple[int, Any]]) -> list[tuple[int, Any]]:
    """
    Sort the keys and values in x using count sort.

    The keys in x must satisfy the constraints
    mentioned in `count_keys()`.

    >>> bucket_sort([])
    []
    >>> bucket_sort([(1, "a"), (2, "b"), (1, "c"), (2, "d"), (4, "e")])
    [(1, 'a'), (1, 'c'), (2, 'b'), (2, 'd'), (4, 'e')]
    """
    buckets = cumsum(count_keys([k for k, _ in x]))
    out = [(0, None)] * len(x)
    # Place the pairs in their buckets
    return out

