import ioc_fanger


def test_systematic_period_square_brackets():
    """."""
    s = "foo[.]com"
    assert ioc_fanger.fang(s) == "foo.com"

    s = "foo].[com"
    assert ioc_fanger.fang(s) == "foo.com"

    s = "foo[.[com"
    assert ioc_fanger.fang(s) == "foo.com"

    s = "foo].]com"
    assert ioc_fanger.fang(s) == "foo.com"

    s = "foo[.com"
    assert ioc_fanger.fang(s) == s

    s = "foo.[com"
    assert ioc_fanger.fang(s) == s

    s = "foo].com"
    assert ioc_fanger.fang(s) == s

    s = "foo.]com"
    assert ioc_fanger.fang(s) == s


def test_systematic_period_curly_braces():
    s = "foo{.}com"
    assert ioc_fanger.fang(s) == "foo.com"

    s = "foo}.{com"
    assert ioc_fanger.fang(s) == "foo.com"

    s = "foo{.{com"
    assert ioc_fanger.fang(s) == "foo.com"

    s = "foo{.com"
    assert ioc_fanger.fang(s) == s

    s = "foo.{com"
    assert ioc_fanger.fang(s) == s

    s = "foo}.}com"
    assert ioc_fanger.fang(s) == "foo.com"

    s = "foo}.com"
    assert ioc_fanger.fang(s) == s

    s = "foo.}com"
    assert ioc_fanger.fang(s) == s


def test_systematic_dot():
    """."""
    s = "fooDOTcom"
    assert ioc_fanger.fang(s) == "foo.com"

    s = "foo[DOT]com"
    assert ioc_fanger.fang(s) == "foo.com"

    s = "foo{DOT}com"
    assert ioc_fanger.fang(s) == "foo.com"

    s = "foo(DOT)com"
    assert ioc_fanger.fang(s) == "foo.com"

    s = "foodotcom"
    assert ioc_fanger.fang(s) == "foodotcom"

    s = "foo[dot]com"
    assert ioc_fanger.fang(s) == "foo.com"

    # see https://github.com/ioc-fang/ioc_fanger/issues/30
    s = "foo{dot}com"
    assert ioc_fanger.fang(s) == "foo.com"

    s = "foo(dot)com"
    assert ioc_fanger.fang(s) == "foo.com"

    s = "foo-dot-com"
    assert ioc_fanger.fang(s) == "foo.com"


def test_issue_112_literal_dot_in_hostname_not_fanged():
    """Literal `dot`/`DOT` inside a hostname must not be treated as a defang.

    See https://github.com/ioc-fang/ioc-fanger/issues/112
    """
    # `dot-` with a hyphen on only one side is not a defang marker
    s = "http://accounts.dot-example.online"
    assert ioc_fanger.fang(s) == s

    # bare uppercase `DOT` inside a hostname containing real periods is preserved
    s = "WWW.MDOT.EXAMPLE.VIP/pay"
    assert ioc_fanger.fang(s) == s

    # lowercase variant is already preserved; keep a regression test for it too
    s = "www.mdot.example.vip/pay"
    assert ioc_fanger.fang(s) == s
