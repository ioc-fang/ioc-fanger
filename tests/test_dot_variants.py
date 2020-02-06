#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ioc_fanger


def test_systematic_period_square_brackets():
    """."""
    s = 'foo[.]com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo].[com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo[.[com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo].]com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo[.com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo.[com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo].com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo.]com'
    assert ioc_fanger.fang(s) == 'foo.com'


def test_systematic_period_curly_braces():
    s = 'foo{.}com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo}.{com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo{.{com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo{.com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo.{com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo}.}com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo}.com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo.}com'
    assert ioc_fanger.fang(s) == 'foo.com'


def test_systematic_dot():
    """."""
    s = 'fooDOTcom'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo[DOT]com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo{DOT}com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo(DOT)com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foodotcom'
    assert ioc_fanger.fang(s) == 'foodotcom'

    s = 'foo[dot]com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo{dot}com'
    assert ioc_fanger.fang(s) == 'foo.com'

    s = 'foo(dot)com'
    assert ioc_fanger.fang(s) == 'foo.com'
