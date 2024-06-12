import pytest

from fun import hi, min, get_from_list

@pytest.mark.parametrize(
    "a, b, result",
    [
        (0, 10, 0),
        (5, 5, 5),
        (-115, -5, -115)
    ],
)
def test_min_success(a, b, result):
    assert min(a, b) == result

@pytest.mark.parametrize(
    "a, b, result",
    [
        (0, 10, 1),
        (5, 5, 35),
        (-115, -5, -1215)
    ],
)
def test_min_fail(a, b, result):
    assert min(a, b) != result


@pytest.mark.parametrize(
    "list, index, result",
    [
        ([0, 1, 2], 0, 0),
        ([4, 5, 5], 1, 5),
        ([-115, -5, -116], 2, -116)
    ],
)
def test_get_from_list_success(list, index, result):
    assert get_from_list(list, index) == result


@pytest.mark.parametrize(
    "list, index, result",
    [
        ([0, 1, 2], 0, 54),
        ([4, 5, 5], 1, 453),
        ([-115, -5, -116], 2, -134516)
    ],
)
def test_get_from_list_fail(list, index, result):
    assert get_from_list(list, index) != result



def test_get_from_list_exception():
    with pytest.raises(IndexError):
        get_from_list([1, 3, 2], 4)


# Test cases for the hi function
@pytest.mark.parametrize(
    "expected_output",
    [
        ("Hi, User!"),  # Correct output
    ]
)
def test_hi_success(expected_output):
    assert hi() == expected_output

# Test cases for failure scenarios
@pytest.mark.parametrize(
    "incorrect_output",
    [
        ("Hello, User!"),  # Incorrect output
        ("Hi, user!"),     # Case-sensitive incorrect output
        ("Hi User"),       # Missing comma
        ("Hi, Users!"),    # Plural form
    ]
)
def test_hi_fail(incorrect_output):
    assert hi() != incorrect_output