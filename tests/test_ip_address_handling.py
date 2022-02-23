import pytest

import ioc_fanger


@pytest.mark.parametrize(
    "input,expected_output",
    [
        (' 1,2,3,4,5,6 ', ' 1,2,3,4,5,6 '),
        (
            '1,2,3,4\n1,2,3,4,5,6 \n1,2,3,4,5,6\n5,6,7,8 9,10,11,12',
            '1.2.3.4\n1,2,3,4,5,6 \n1,2,3,4,5,6\n5.6.7.8 9.10.11.12',
        ),
        (' 1,2,3,4 ', ' 1.2.3.4 '),
        ('1,2,3,4', '1.2.3.4'),
        ('1,2,3,4 1,2,3,4', '1.2.3.4 1.2.3.4'),
    ],
)
def test_issue_71__overzealous_fanging_of_comma_seperated_nums(input, expected_output):
    assert ioc_fanger.fang(input) == expected_output
