#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ioc_fanger
----------------------------------

Tests for `ioc_fanger` module.
"""

import ioc_fanger
import pytest


@pytest.fixture
def defanged_text():
    return "example[.]com hxxp://example[.]com hXXp://example[.]com example\.com example.com http://example.com hxxp://example[.]com 1[.]2[.]3[.]4 bob[@]example[.]com mary[@]example.com carlos[at]example.com juanita(at)example.com http[:]//example.org https[:]//example.org hXxps[:]//example.org/test?target=bad[@]test.com bad-dot-com example-dot-ru 5[,]6[,]7(,)8 9,10,11,12"


@pytest.fixture
def fanged_text():
    return "example.com http://example.com http://example.com example.com example.com http://example.com http://example.com 1.2.3.4 bob@example.com mary@example.com carlos@example.com juanita@example.com http://example.org https://example.org https://example.org/test?target=bad@test.com bad.com example.ru 5.6.7.8 9.10.11.12"


@pytest.fixture
def defanged_email_address_text():
    return "bob[@]example.com bob(@)example.com bob[at]example.com bob(at)example.com bob AT example.com bob@example[dot]com bob@example(dot)com bob@example DOT com"


@pytest.fixture
def fanged_email_address_text():
    return ("bob@example.com "*8).strip()


def test_fanging(defanged_text, fanged_text):
    """Test fanging."""
    test_fanged_text = ioc_fanger.fang(defanged_text)
    assert test_fanged_text == fanged_text


def test_defanging(fanged_text):
    """Test defanging."""
    defanged_text = ioc_fanger.defang(fanged_text)

    assert "hXXp://example[.]com" in defanged_text
    assert "1[.]2[.]3[.]4" in defanged_text
    assert "bob(at)example[.]com" in defanged_text
    assert "5[.]6[.]7[.]8" in defanged_text
    print("defanged_text {}".format(defanged_text))
    assert "9[.]10[.]11[.]12" in defanged_text


def test_email_addresses(defanged_email_address_text, fanged_email_address_text):
    """Make sure email addresses are properly fanged."""
    fanged_addresses = ioc_fanger.fang(defanged_email_address_text)
    assert fanged_addresses == fanged_email_address_text


def test_spanish_defanging():
    s = 'me (arroba) example (punto) com'
    assert ioc_fanger.fang(s) == 'me@example.com'

    s = 'me(arroba)example(punto)com'
    assert ioc_fanger.fang(s) == 'me@example.com'

    s = 'me [arroba] example [punto] com'
    assert ioc_fanger.fang(s) == 'me@example.com'

    s = 'me[arroba]example[punto]com'
    assert ioc_fanger.fang(s) == 'me@example.com'


def test_german_defanging():
    s = 'me@example (punkt) com'
    assert ioc_fanger.fang(s) == 'me@example.com'

    s = 'me@example(punkt)com'
    assert ioc_fanger.fang(s) == 'me@example.com'

    s = 'me@example [punkt] com'
    assert ioc_fanger.fang(s) == 'me@example.com'

    s = 'me@example[punkt]com'
    assert ioc_fanger.fang(s) == 'me@example.com'


def test_issue_16():
    s = "www[.example.com"
    assert ioc_fanger.fang(s) == 'www.example.com'


def test_issue_24():
    s = 'seasharpee'
    assert ioc_fanger.fang(s) == 'seasharpee'


def test_parenthetical_period():
    s = "www(.)example(.)com"
    assert ioc_fanger.fang(s) == 'www.example.com'


def test_odd_brackets():
    s = "www[.[example[.[com"
    assert ioc_fanger.fang(s) == 'www.example.com'

    s = "www].]example].]com"
    assert ioc_fanger.fang(s) == 'www.example.com'

    s = "www].[example].[com"
    assert ioc_fanger.fang(s) == 'www.example.com'

    s = "www.[example.[com"
    assert ioc_fanger.fang(s) == 'www.example.com'

    s = "www.]example.]com"
    assert ioc_fanger.fang(s) == 'www.example.com'

    s = "www[.example[.com"
    assert ioc_fanger.fang(s) == 'www.example.com'

    s = "www].example].com"
    assert ioc_fanger.fang(s) == 'www.example.com'


def test_odd_misc():
    s = "www\.example\.com"
    assert ioc_fanger.fang(s) == 'www.example.com'

    s = "foo[-]bar.com"
    assert ioc_fanger.fang(s) == 'foo-bar.com'

    s = "[www].example.com"
    assert ioc_fanger.fang(s) == 'www.example.com'

    s = "(www).example.com"
    assert ioc_fanger.fang(s) == 'www.example.com'

    s = 'https://example.com\/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'

    s = """diota[-]ar.com:80/.well-known/acme-challenge/mxr.pdf
diota[-]ar.com/.well-known/acme-challenge/mxr.pdf"""
    assert ioc_fanger.fang(s) == """diota-ar.com:80/.well-known/acme-challenge/mxr.pdf
diota-ar.com/.well-known/acme-challenge/mxr.pdf"""

    s = """xxxxs://proverka[.]host/ Email: silena[.]berillo(at)gmail[.]com, hto2018(at)yandex[.]ru"""
    assert ioc_fanger.fang(s) == """https://proverka.host/ Email: silena.berillo@gmail.com, hto2018@yandex.ru"""

    s = """code to (https://www.linkedin.com/feed/hashtag/?keywords=%23IOCs)<https://example.in/foo>"""
    data = ioc_fanger.fang(s)
    assert data == """code to https://www.linkedin.com/feed/hashtag/?keywords=%23IOCs)<https://example.in/foo>"""

    s = 'analysis), yo'
    data = ioc_fanger.fang(s)
    assert data == s


def test_odd_schemes():
    s = 'xxxx://example.com/test.php'
    assert ioc_fanger.fang(s) == 'http://example.com/test.php'
    s = 'xxxxx://example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'
    s = 'xXxX://example.com/test.php'
    assert ioc_fanger.fang(s) == 'http://example.com/test.php'
    s = 'xXxXx://example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'

    s = 'hxxp://example.com/test.php'
    assert ioc_fanger.fang(s) == 'http://example.com/test.php'
    s = 'hXXp://example.com/test.php'
    assert ioc_fanger.fang(s) == 'http://example.com/test.php'
    s = 'hxxps://example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'
    s = 'hXXps://example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'

    s = 'http ://example.com/test.php'
    assert ioc_fanger.fang(s) == 'http://example.com/test.php'
    s = 'https ://example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'

    s = 'http:// example.com/test.php'
    assert ioc_fanger.fang(s) == 'http://example.com/test.php'
    s = 'https:// example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'

    s = 'http//example.com/test.php'
    assert ioc_fanger.fang(s) == 'http://example.com/test.php'
    s = 'https//example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'

    s = 'http// example.com/test.php'
    assert ioc_fanger.fang(s) == 'http://example.com/test.php'
    s = 'https// example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'

    s = 'http:///example.com/test.php'
    assert ioc_fanger.fang(s) == 'http://example.com/test.php'
    s = 'http:/// example.com/test.php'
    assert ioc_fanger.fang(s) == 'http://example.com/test.php'
    s = 'http :///example.com/test.php'
    assert ioc_fanger.fang(s) == 'http://example.com/test.php'

    s = 'https:///example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'
    s = 'https:/// example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'
    s = 'https :///example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'

    s = '[http]://example.com/test.php'
    assert ioc_fanger.fang(s) == 'http://example.com/test.php'
    s = '[https]://example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'

    s = '(http)://example.com/test.php'
    assert ioc_fanger.fang(s) == 'http://example.com/test.php'
    s = '(https)://example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'

    s = 'http!://example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'
    s = 'https!://example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'
    s = 'https@://example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'
    s = 'httpA://example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'
    s = 'https&://example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php'

    s = 'https&://example.com/test.php https://example.com/test.php http&://example.com/test.php xxXpA://example.com/test.php'
    assert ioc_fanger.fang(s) == 'https://example.com/test.php https://example.com/test.php https://example.com/test.php https://example.com/test.php'


def test_odd_email_address_spacing():
    s = "foo@barDOTcom"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo@bar DOT com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo@bar  DOT  com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo @ bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo  @ bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo @  bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo  @  bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "fooATbar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    # make sure that the `AT` parsing isn't too broad... it shouldn't replace 'AT' with '@' if the 'AT' is preceded by a capital letter
    s = "fooMATbar.com"
    assert ioc_fanger.fang(s) == 'fooMATbar.com'

    # see the previous comment, except this makes sure that 'AT' isn't postceded by a capital letter
    s = "fooATAbar.com"
    assert ioc_fanger.fang(s) == 'fooATAbar.com'

    s = "foo AT bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo  AT bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo AT  bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo  AT  bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo[AT]bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo(AT)bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo[at]bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo(at)bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo[ET]bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo(ET)bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo[et]bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo(et)bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo [AT] bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo (AT) bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo [at] bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo (at) bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo [ET] bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo (ET) bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo [et] bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'

    s = "foo (et) bar.com"
    assert ioc_fanger.fang(s) == 'foo@bar.com'


def test_ip_address_defang():
    """Make sure ip addresses are defanged sensibly."""
    s = '192.168.4.2'
    assert ioc_fanger.defang(s) == '192[.]168[.]4[.]2'

    s = '8.8.8.8'
    assert ioc_fanger.defang(s) == '8[.]8[.]8[.]8'


def test_odd_hXXp_replacement():
    s = 'In the UI: https://help.passivetotal.org/tags_&_classifications.html (https://help.passivetotal.org/tags_&_classifications.html)'
    assert ioc_fanger.fang(s, debug=True) == 'In the UI: https://help.passivetotal.org/tags_&_classifications.html https://help.passivetotal.org/tags_&_classifications.html)'
