"""
test_ioc_fanger
----------------------------------

Tests for `ioc_fanger` module.
"""

import logging

import pytest

import ioc_fanger
from ioc_fanger import ioc_fanger as ioc_fanger_module


@pytest.fixture
def defanged_email_address_text():
    return "bob[@]example.com bob(@)example.com bob{@}example.com bob[at]example.com bob(at)example.com bob{at}example.com bob AT example.com bob@example[dot]com bob@example(dot)com bob@example DOT com"


@pytest.fixture
def fanged_email_address_text():
    return ("bob@example.com " * 10).strip()


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

    s = "test@[192.168.0.1]"
    fanged_data = ioc_fanger.fang(s)
    assert fanged_data == "test@[192.168.0.1]"

    s = "john.smith(comment)@example.com"
    fanged_data = ioc_fanger.fang(s)
    assert fanged_data == "john.smith(comment)@example.com"


def test_spanish_defanging():
    s = "me (arroba) example (punto) com"
    assert ioc_fanger.fang(s) == "me@example.com"

    s = "me(arroba)example(punto)com"
    assert ioc_fanger.fang(s) == "me@example.com"

    s = "me [arroba] example [punto] com"
    assert ioc_fanger.fang(s) == "me@example.com"

    s = "me[arroba]example[punto]com"
    assert ioc_fanger.fang(s) == "me@example.com"


def test_german_defanging():
    s = "me@example (punkt) com"
    assert ioc_fanger.fang(s) == "me@example.com"

    s = "me@example(punkt)com"
    assert ioc_fanger.fang(s) == "me@example.com"

    s = "me@example [punkt] com"
    assert ioc_fanger.fang(s) == "me@example.com"

    s = "me@example[punkt]com"
    assert ioc_fanger.fang(s) == "me@example.com"


def test_issue_24():
    s = "seasharpee"
    assert ioc_fanger.fang(s) == "seasharpee"


def test_issue_25():
    s = "123howp"
    assert ioc_fanger.fang(s) == "123howp"


def test_issue_32():
    # see https://github.com/ioc-fang/ioc_fanger/issues/32
    s = "httptest@test.com"
    assert ioc_fanger.defang(s) == "httptest(at)test[.]com"


def test_parenthetical_period():
    s = "www(.)example(.)com"
    assert ioc_fanger.fang(s) == "www.example.com"


def test_odd_brackets():
    s = "www[.[example[.[com"
    assert ioc_fanger.fang(s) == "www.example.com"

    s = "www].]example].]com"
    assert ioc_fanger.fang(s) == "www.example.com"

    s = "www].[example].[com"
    assert ioc_fanger.fang(s) == "www.example.com"


def test__punctuation_with_single_bracket__not_changed():
    """These examples used to be fanged, but we removed support for fanging punctuation with a single bracket around it in #49."""
    s = "www.[example.[com"
    assert ioc_fanger.fang(s) == s

    s = "www.]example.]com"
    assert ioc_fanger.fang(s) == s

    s = "www[.example[.com"
    assert ioc_fanger.fang(s) == s

    s = "www].example].com"
    assert ioc_fanger.fang(s) == s

    s = "www],example),com"
    assert ioc_fanger.fang(s) == s


def test_odd_misc():
    s = "www\.example\.com"
    assert ioc_fanger.fang(s) == "www.example.com"

    s = "www^.example^.com"
    assert ioc_fanger.fang(s) == "www.example.com"

    s = "foo[-]bar.com"
    assert ioc_fanger.fang(s) == "foo-bar.com"

    s = "[www].example.com"
    assert ioc_fanger.fang(s) == "www.example.com"

    s = "(www).example.com"
    assert ioc_fanger.fang(s) == "www.example.com"

    s = "https://example.com\/test.php"
    assert ioc_fanger.fang(s) == "https://example.com/test.php"

    s = """diota[-]ar.com:80/.well-known/acme-challenge/mxr.pdf
diota[-]ar.com/.well-known/acme-challenge/mxr.pdf"""
    assert (
        ioc_fanger.fang(s)
        == """diota-ar.com:80/.well-known/acme-challenge/mxr.pdf
diota-ar.com/.well-known/acme-challenge/mxr.pdf"""
    )

    s = """xxxxs://proverka[.]host/ Email: silena[.]berillo(at)gmail[.]com, hto2018(at)yandex[.]ru"""
    assert ioc_fanger.fang(s) == """https://proverka.host/ Email: silena.berillo@gmail.com, hto2018@yandex.ru"""

    s = """code to (https://www.linkedin.com/feed/hashtag/?keywords=%23IOCs)<https://example.in/foo>"""
    data = ioc_fanger.fang(s)
    assert data == """code to https://www.linkedin.com/feed/hashtag/?keywords=%23IOCs)<https://example.in/foo>"""

    s = "analysis), yo"
    data = ioc_fanger.fang(s)
    assert data == s


def test_odd_schemes():
    s = "xxxx://example.com/test.php"
    assert ioc_fanger.fang(s) == "http://example.com/test.php"
    s = "xxxxx://example.com/test.php"
    assert ioc_fanger.fang(s) == "https://example.com/test.php"
    s = "xXxX://example.com/test.php"
    assert ioc_fanger.fang(s) == "http://example.com/test.php"
    s = "xXxXx://example.com/test.php"
    assert ioc_fanger.fang(s) == "https://example.com/test.php"

    s = "hxxp://example.com/test.php"
    assert ioc_fanger.fang(s) == "http://example.com/test.php"
    s = "hXXp://example.com/test.php"
    assert ioc_fanger.fang(s) == "http://example.com/test.php"
    s = "hxxps://example.com/test.php"
    assert ioc_fanger.fang(s) == "https://example.com/test.php"
    s = "hXXps://example.com/test.php"
    assert ioc_fanger.fang(s) == "https://example.com/test.php"

    s = "http ://example.com/test.php"
    assert ioc_fanger.fang(s) == "http://example.com/test.php"
    s = "https ://example.com/test.php"
    assert ioc_fanger.fang(s) == "https://example.com/test.php"

    s = "http:// example.com/test.php"
    assert ioc_fanger.fang(s) == "http://example.com/test.php"
    s = "https:// example.com/test.php"
    assert ioc_fanger.fang(s) == "https://example.com/test.php"

    s = "http//example.com/test.php"
    assert ioc_fanger.fang(s) == "http://example.com/test.php"
    s = "https//example.com/test.php"
    assert ioc_fanger.fang(s) == "https://example.com/test.php"

    s = "http// example.com/test.php"
    assert ioc_fanger.fang(s) == "http://example.com/test.php"
    s = "https// example.com/test.php"
    assert ioc_fanger.fang(s) == "https://example.com/test.php"

    s = "http:///example.com/test.php"
    assert ioc_fanger.fang(s) == "http://example.com/test.php"
    s = "http:/// example.com/test.php"
    assert ioc_fanger.fang(s) == "http://example.com/test.php"
    s = "http :///example.com/test.php"
    assert ioc_fanger.fang(s) == "http://example.com/test.php"

    s = "https:///example.com/test.php"
    assert ioc_fanger.fang(s) == "https://example.com/test.php"
    s = "https:/// example.com/test.php"
    assert ioc_fanger.fang(s) == "https://example.com/test.php"
    s = "https :///example.com/test.php"
    assert ioc_fanger.fang(s) == "https://example.com/test.php"

    s = "[http]://example.com/test.php"
    assert ioc_fanger.fang(s) == "http://example.com/test.php"
    s = "[https]://example.com/test.php"
    assert ioc_fanger.fang(s) == "https://example.com/test.php"

    s = "(http)://example.com/test.php"
    assert ioc_fanger.fang(s) == "http://example.com/test.php"
    s = "(https)://example.com/test.php"
    assert ioc_fanger.fang(s) == "https://example.com/test.php"

    s = "hxxps[://]example[.]com/test[.]html"
    assert ioc_fanger.fang(s) == "https://example.com/test.html"


def test_odd_email_address_spacing():
    s = "foo@barDOTcom"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo@bar DOT com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo@bar  DOT  com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo @ bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo  @ bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo @  bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo  @  bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "fooATbar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    # make sure that the `AT` parsing isn't too broad... it shouldn't replace 'AT' with '@' if the 'AT' is preceded by a capital letter
    s = "fooMATbar.com"
    assert ioc_fanger.fang(s) == "fooMATbar.com"

    # see the previous comment, except this makes sure that 'AT' isn't postceded by a capital letter
    s = "fooATAbar.com"
    assert ioc_fanger.fang(s) == "fooATAbar.com"

    s = "foo AT bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo  AT bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo AT  bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo  AT  bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo[AT]bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo(AT)bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo[at]bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo(at)bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo[ET]bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo(ET)bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo[et]bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo(et)bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo [AT] bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo (AT) bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo [at] bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo (at) bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo [ET] bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo (ET) bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo [et] bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"

    s = "foo (et) bar.com"
    assert ioc_fanger.fang(s) == "foo@bar.com"


def test_ip_address_defang():
    """Make sure ip addresses are defanged sensibly."""
    s = "192.168.4.2"
    assert ioc_fanger.defang(s) == "192[.]168[.]4[.]2"

    s = "8.8.8.8"
    assert ioc_fanger.defang(s) == "8[.]8[.]8[.]8"


def test_odd_hXXp_replacement():
    s = "In the UI: https://help.passivetotal.org/tags_&_classifications.html (https://help.passivetotal.org/tags_&_classifications.html)"
    assert (
        ioc_fanger.fang(s)
        == "In the UI: https://help.passivetotal.org/tags_&_classifications.html https://help.passivetotal.org/tags_&_classifications.html)"
    )

    # this is based on the text of an incident found here: https://app.threatconnect.com/auth/incident/incident.xhtml?incident=2952580883&owner=Technical%20Blogs%20and%20Reports#/
    # update (aug 2022): this used to be fanged, but we are no longer fanging this
    s = "domain (www.example.com)."
    assert ioc_fanger.fang(s) == s


def test_markdown_fanging():
    s = "[https://i.imgur.com/abc.png](https://i.imgur.com/abc.png)"
    assert ioc_fanger.fang(s) == "https://i.imgur.com/abc.png]https://i.imgur.com/abc.png)"

    s = "_o_o.lgms.nl_"
    assert ioc_fanger.fang(s) == "_o_o.lgms.nl_"


def test_debug():
    # make sure using debug still works properly
    s = "192[.]168[.]4[.]2"
    assert ioc_fanger.fang(s, debug=True) == "192.168.4.2"


def test_issue_46():
    s = "div><div><br></div><div>hxxp://zeplin[.]atwebpages[.]com/inter[.]php</div><"
    result = ioc_fanger.fang(s)
    assert result == "div><div><br></div><div>http://zeplin.atwebpages.com/inter.php</div><"


def test_issue_47():
    s = "a. [b"
    result = ioc_fanger.fang(s)
    assert result == "a. [b"

    s = "a. (b"
    result = ioc_fanger.fang(s)
    assert result == "a. (b"


def test_issue_53__percent_encoded_urls_fanged_properly():
    """Testing to make sure percent encoded URLs are properly fanged."""
    s = "https://asf.goole.com/mail?url=http%3A%2F%2Ffreasdfuewriter.com%2Fcs%2Fimage%2FCommerciaE.jpg&t=1575955624&ymreqid=733bc9eb-e8f-34cb-1cb5-120010019e00&sig=x2Pa2oOYxanG52s4vyCEFg--~Chttp://uniddloos.zddfdd.org/CBA0019_file_00002_pdf.zip"
    result = ioc_fanger.fang(s)
    assert (
        result
        == "https://asf.goole.com/mail?url=http%3A%2F%2Ffreasdfuewriter.com%2Fcs%2Fimage%2FCommerciaE.jpg&t=1575955624&ymreqid=733bc9eb-e8f-34cb-1cb5-120010019e00&sig=x2Pa2oOYxanG52s4vyCEFg--~Chttp://uniddloos.zddfdd.org/CBA0019_file_00002_pdf.zip"
    )


def test_issue_53__urls_in_query_strings_fanged():
    """Make sure URLs in query strings are properly fanged."""
    # imagining s is part of a query string, make sure s is unchanged
    s = "--~Chttp://uniddloos.zddfdd.org/CBA0019_file_00002_pdf.zip"
    result = ioc_fanger.fang(s)
    assert result == "--~Chttp://uniddloos.zddfdd.org/CBA0019_file_00002_pdf.zip"

    # imagining s is part of a query string, make sure s is unchanged
    s = "--~Chttps://uniddloos.zddfdd.org/CBA0019_file_00002_pdf.zip"
    result = ioc_fanger.fang(s)
    assert result == "--~Chttps://uniddloos.zddfdd.org/CBA0019_file_00002_pdf.zip"


def test_issue_52__escaped_periods():
    s = "foo 1<.>1<.>1<.>1 bar."
    result = ioc_fanger.fang(s)
    assert result == "foo 1.1.1.1 bar."


def test_alternative_schemes_preserved():
    s = "ldap://example.com/a"
    result = ioc_fanger.fang(s)
    assert result == "ldap://example.com/a"


def test_pr_99__escaped_periods():
    s = "HKLM\\SOFTWARE\\foo bar\\bing buzz boom\\b"
    result = ioc_fanger.fang(s)
    assert result == "HKLM\\SOFTWARE\\foo bar\\bing buzz boom\\b"

    s = "foo$.bar foo\\.bar"
    result = ioc_fanger.fang(s)
    assert result == "foo$.bar foo.bar"


@pytest.fixture
def reset_fang_logger():
    logger = ioc_fanger_module.logger
    original_level = logger.level
    original_handlers = logger.handlers[:]
    logger.handlers = []
    logger.setLevel(logging.NOTSET)
    yield logger
    logger.handlers = original_handlers
    logger.setLevel(original_level)


def test_fang_debug_emits_log_records(reset_fang_logger, caplog):
    """When debug=True, fang emits DEBUG-level log records via the module logger."""
    with caplog.at_level(logging.DEBUG, logger=reset_fang_logger.name):
        ioc_fanger.fang("hxxp://example[.]com", debug=True)

    debug_messages = [r.getMessage() for r in caplog.records if r.levelno == logging.DEBUG]
    assert any("Starting text: hxxp://example[.]com" in m for m in debug_messages)
    assert any(m.startswith("Mapping: ") for m in debug_messages)
    assert any(m.startswith("Text after mapping: ") for m in debug_messages)


def test_fang_debug_sets_logger_level_and_handler(reset_fang_logger):
    """debug=True sets the logger to DEBUG and attaches a handler so output is visible."""
    ioc_fanger.fang("hxxp://example[.]com", debug=True)

    assert reset_fang_logger.level == logging.DEBUG
    assert any(isinstance(h, logging.StreamHandler) for h in reset_fang_logger.handlers)


def test_postceded_only_dot_word_variants():
    """Bracket only on the trailing side of dot/punto/punkt — exercises the postceded-only fang pattern."""
    assert ioc_fanger.fang("foodot]com") == "foo.com"
    assert ioc_fanger.fang("foopunto)com") == "foo.com"
    assert ioc_fanger.fang("foopunkt}com") == "foo.com"


def test_postceded_only_lowercase_at_variants():
    """Bracket only on the trailing side of lowercase at/et/arroba — exercises the postceded-only fang pattern."""
    assert ioc_fanger.fang("fooat]bar.com") == "foo@bar.com"
    assert ioc_fanger.fang("fooet)bar.com") == "foo@bar.com"
    assert ioc_fanger.fang("fooarroba}bar.com") == "foo@bar.com"


def test_postceded_only_uppercase_AT_variants():
    """Bracket only on the trailing side of uppercase AT/ET/ARROBA — exercises the postceded-only fang pattern."""
    assert ioc_fanger.fang("fooAT]bar.com") == "foo@bar.com"
    assert ioc_fanger.fang("fooET)bar.com") == "foo@bar.com"
    assert ioc_fanger.fang("fooARROBA}bar.com") == "foo@bar.com"


def test_postceded_only_http_brackets():
    """Bracket only on the trailing side of http(s) — exercises the postceded-only fang pattern."""
    assert ioc_fanger.fang("http]://example.com") == "http://example.com"
    assert ioc_fanger.fang("https]://example.com") == "https://example.com"


def test_fang_default_does_not_emit_debug_records(reset_fang_logger, caplog):
    """Without debug=True, no DEBUG-level records are surfaced through the root config."""
    with caplog.at_level(logging.WARNING, logger=reset_fang_logger.name):
        ioc_fanger.fang("hxxp://example[.]com")

    assert [r for r in caplog.records if r.levelno == logging.DEBUG] == []
