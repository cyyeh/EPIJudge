import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(A: List[int]) -> None:
    left_idx = 0
    right_idx = len(A) - 1
    while left_idx < right_idx:
        if A[left_idx] % 2 == 1 and A[right_idx] % 2 == 0:
            A[left_idx], A[right_idx] = A[right_idx], A[left_idx]
            left_idx += 1
            right_idx -= 1
            continue
        if A[left_idx] % 2 == 0:
            left_idx += 1
        if A[right_idx] % 2 == 1:
            right_idx -= 1
    return


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
