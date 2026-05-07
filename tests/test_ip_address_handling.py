import pytest

import ioc_fanger


@pytest.mark.parametrize(
    "input,expected_output",
    [
        (" 1,2,3,4,5,6 ", " 1,2,3,4,5,6 "),
        (
            "1,2,3,4\n1,2,3,4,5,6 \n1,2,3,4,5,6\n5,6,7,8 9,10,11,12",
            "1.2.3.4\n1,2,3,4,5,6 \n1,2,3,4,5,6\n5.6.7.8 9.10.11.12",
        ),
        (" 1,2,3,4 ", " 1.2.3.4 "),
        ("1,2,3,4", "1.2.3.4"),
        ("1,2,3,4 1,2,3,4", "1.2.3.4 1.2.3.4"),
    ],
)
def test_issue_71__overzealous_fanging_of_comma_seperated_nums(input, expected_output):
    assert ioc_fanger.fang(input) == expected_output


@pytest.mark.parametrize(
    "input,expected_output",
    [
        # 999 is not a valid IPv4 octet, leave it alone
        ("999,999,999,999", "999,999,999,999"),
        # Out-of-range last octet leaves the whole match alone
        ("1,2,3,256", "1,2,3,256"),
        # Out-of-range first octet leaves the whole match alone
        ("300,1,1,1", "300,1,1,1"),
        # Boundary: 255.255.255.255 is valid
        ("255,255,255,255", "255.255.255.255"),
        # Boundary: 0.0.0.0 is valid
        ("0,0,0,0", "0.0.0.0"),
        # A valid IP next to an invalid one only fangs the valid one
        ("1,2,3,4 999,999,999,999", "1.2.3.4 999,999,999,999"),
    ],
)
def test_issue_93__only_fang_octets_in_0_to_255(input, expected_output):
    assert ioc_fanger.fang(input) == expected_output
