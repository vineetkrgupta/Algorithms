from .fibonacci import (fib_recursion, fib_from_table,
                        fib_memoization, fib_generator, fib_iteration)
import pytest

questions_answers = [
    (0, 0),
    (1, 1),
    (54, 86267571272),
    (100, 354224848179261915075),
    (200, 280571172992510140037611932413038677189525)
]


@pytest.mark.parametrize("test_input,expected", questions_answers)
def test_fib(test_input, expected):
    for func in [
        fib_from_table,
        fib_memoization,
        fib_iteration
    ]:
        assert func(test_input) == expected
