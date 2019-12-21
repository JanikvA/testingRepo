from repoName import repoName


def test_fib() -> None:
    assert repoName.fib(0) == 0
    assert repoName.fib(1) == 1
    assert repoName.fib(2) == 1
    assert repoName.fib(3) == 2
    assert repoName.fib(4) == 3
    assert repoName.fib(5) == 5
    assert repoName.fib(10) == 55
