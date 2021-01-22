from pyparsing import alphas, alphanums
from pyparsing import (
    CaselessLiteral,
    Combine,
    Literal,
    NotAny,
    Optional,
    Or,
    Regex,
    replaceWith,
    upcaseTokens,
    Word,
    WordEnd,
    WordStart,
    ZeroOrMore,
    CaselessKeyword,
    White,
)

alphanum_word_start = WordStart(wordChars=alphanums)
alphanum_word_end = WordEnd(wordChars=alphanums)

uppercase_word = Word("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
not_uppercase_word_regex = Regex("[^A-Z]")

dot_fanging_patterns = Combine(
    Optional(White(ws=' \t'))
    + Or(
        [
            # '.' - enclosed with ( and )
            CaselessLiteral("(.("),
            CaselessLiteral("(.)"),
            CaselessLiteral(").("),
            CaselessLiteral(").)"),
            CaselessLiteral("(."),
            CaselessLiteral(".("),
            # CaselessLiteral(")."), # this is commented and is NOT used to fang indicators b/c this may appear in real text
            CaselessLiteral(".)"),
            # 'dot' - enclosed with ( and )
            CaselessLiteral("(dot("),
            CaselessLiteral("(dot)"),
            CaselessLiteral(")dot("),
            CaselessLiteral(")dot)"),
            CaselessLiteral("(dot"),
            CaselessLiteral("dot("),
            CaselessLiteral(")dot"),
            CaselessLiteral("dot)"),
            # 'punkt' - enclosed with ( and )
            CaselessLiteral("(punkt("),
            CaselessLiteral("(punkt)"),
            CaselessLiteral(")punkt("),
            CaselessLiteral(")punkt)"),
            CaselessLiteral("(punkt"),
            CaselessLiteral("punkt("),
            CaselessLiteral(")punkt"),
            CaselessLiteral("punkt)"),
            # 'punto' - enclosed with ( and )
            CaselessLiteral("(punto("),
            CaselessLiteral("(punto)"),
            CaselessLiteral(")punto("),
            CaselessLiteral(")punto)"),
            CaselessLiteral("(punto"),
            CaselessLiteral("punto("),
            CaselessLiteral(")punto"),
            CaselessLiteral("punto)"),
            # '.' - enclosed with [ and ]
            CaselessLiteral("[.["),
            CaselessLiteral("[.]"),
            CaselessLiteral("].["),
            CaselessLiteral("].]"),
            CaselessLiteral("[."),
            CaselessLiteral(".["),
            CaselessLiteral("]."),
            CaselessLiteral(".]"),
            # 'dot' - enclosed with [ and ]
            CaselessLiteral("[dot["),
            CaselessLiteral("[dot]"),
            CaselessLiteral("]dot["),
            CaselessLiteral("]dot]"),
            CaselessLiteral("[dot"),
            CaselessLiteral("dot["),
            CaselessLiteral("]dot"),
            CaselessLiteral("dot]"),
            # 'punkt' - enclosed with [ and ]
            CaselessLiteral("[punkt["),
            CaselessLiteral("[punkt]"),
            CaselessLiteral("]punkt["),
            CaselessLiteral("]punkt]"),
            CaselessLiteral("[punkt"),
            CaselessLiteral("punkt["),
            CaselessLiteral("]punkt"),
            CaselessLiteral("punkt]"),
            # 'punto' - enclosed with [ and ]
            CaselessLiteral("[punto["),
            CaselessLiteral("[punto]"),
            CaselessLiteral("]punto["),
            CaselessLiteral("]punto]"),
            CaselessLiteral("[punto"),
            CaselessLiteral("punto["),
            CaselessLiteral("]punto"),
            CaselessLiteral("punto]"),
            # '.' - enclosed with { and }
            CaselessLiteral("{.{"),
            CaselessLiteral("{.}"),
            CaselessLiteral("}.{"),
            CaselessLiteral("}.}"),
            CaselessLiteral("{."),
            CaselessLiteral(".{"),
            CaselessLiteral("}."),
            CaselessLiteral(".}"),
            # 'dot' - enclosed with { and }
            CaselessLiteral("{dot{"),
            CaselessLiteral("{dot}"),
            CaselessLiteral("}dot{"),
            CaselessLiteral("}dot}"),
            CaselessLiteral("{dot"),
            CaselessLiteral("dot{"),
            CaselessLiteral("}dot"),
            CaselessLiteral("dot}"),
            # 'punkt' - enclosed with { and }
            CaselessLiteral("{punkt{"),
            CaselessLiteral("{punkt}"),
            CaselessLiteral("}punkt{"),
            CaselessLiteral("}punkt}"),
            CaselessLiteral("{punkt"),
            CaselessLiteral("punkt{"),
            CaselessLiteral("}punkt"),
            CaselessLiteral("punkt}"),
            # 'punto' - enclosed with { and }
            CaselessLiteral("{punto{"),
            CaselessLiteral("{punto}"),
            CaselessLiteral("}punto{"),
            CaselessLiteral("}punto}"),
            CaselessLiteral("{punto"),
            CaselessLiteral("punto{"),
            CaselessLiteral("}punto"),
            CaselessLiteral("punto}"),
            # a
            Literal("DOT"),
            Literal("PUNKT"),
            Literal("PUNTO"),
            CaselessLiteral("-dot-"),
            CaselessLiteral("-punkt-"),
            CaselessLiteral("-punto-"),
        ]
    )
    + Optional(White(ws=' \t'))
).addParseAction(replaceWith("."))

at_fanging_patterns = Combine(
    Optional(White(ws=' \t'))
    + Or(
        [
            # '@' - enclosed with ( and )
            CaselessLiteral("(@("),
            CaselessLiteral("(@)"),
            CaselessLiteral(")@("),
            CaselessLiteral(")@)"),
            CaselessLiteral("(@"),
            CaselessLiteral("@("),
            # CaselessLiteral(")@"),   # this is commented and is NOT used to fang indicators b/c this format is valid for some email addresses (see the test_ioc_fanger::test_email_addresses function)
            CaselessLiteral("@)"),
            # 'at' - enclosed with ( and )
            CaselessLiteral("(at("),
            CaselessLiteral("(at)"),
            CaselessLiteral(")at("),
            CaselessLiteral(")at)"),
            CaselessLiteral("(at"),
            CaselessLiteral("at("),
            CaselessLiteral(")at"),
            CaselessLiteral("at)"),
            # 'et' - enclosed with ( and )
            CaselessLiteral("(et("),
            CaselessLiteral("(et)"),
            CaselessLiteral(")et("),
            CaselessLiteral(")et)"),
            CaselessLiteral("(et"),
            CaselessLiteral("et("),
            CaselessLiteral(")et"),
            CaselessLiteral("et)"),
            # 'arroba' - enclosed with ( and )
            CaselessLiteral("(arroba("),
            CaselessLiteral("(arroba)"),
            CaselessLiteral(")arroba("),
            CaselessLiteral(")arroba)"),
            CaselessLiteral("(arroba"),
            CaselessLiteral("arroba("),
            CaselessLiteral(")arroba"),
            CaselessLiteral("arroba)"),
            # '@' - enclosed with [ and ]
            CaselessLiteral("[@["),
            CaselessLiteral("[@]"),
            CaselessLiteral("]@["),
            CaselessLiteral("]@]"),
            CaselessLiteral("[@"),
            # CaselessLiteral("@["), # this is commented and is NOT used to fang indicators b/c this format is valid for some email addresses (see the test_ioc_fanger::test_email_addresses function)
            CaselessLiteral("]@"),
            CaselessLiteral("@]"),
            # 'at' - enclosed with [ and ]
            CaselessLiteral("[at["),
            CaselessLiteral("[at]"),
            CaselessLiteral("]at["),
            CaselessLiteral("]at]"),
            CaselessLiteral("[at"),
            CaselessLiteral("at["),
            CaselessLiteral("]at"),
            CaselessLiteral("at]"),
            # 'et' - enclosed with [ and ]
            CaselessLiteral("[et["),
            CaselessLiteral("[et]"),
            CaselessLiteral("]et["),
            CaselessLiteral("]et]"),
            CaselessLiteral("[et"),
            CaselessLiteral("et["),
            CaselessLiteral("]et"),
            CaselessLiteral("et]"),
            # 'arroba' - enclosed with [ and ]
            CaselessLiteral("[arroba["),
            CaselessLiteral("[arroba]"),
            CaselessLiteral("]arroba["),
            CaselessLiteral("]arroba]"),
            CaselessLiteral("[arroba"),
            CaselessLiteral("arroba["),
            CaselessLiteral("]arroba"),
            CaselessLiteral("arroba]"),
            # '@' - enclosed with { and }
            CaselessLiteral("{@{"),
            CaselessLiteral("{@}"),
            CaselessLiteral("}@{"),
            CaselessLiteral("}@}"),
            CaselessLiteral("{@"),
            CaselessLiteral("@{"),
            CaselessLiteral("}@"),
            CaselessLiteral("@}"),
            # 'at' - enclosed with { and }
            CaselessLiteral("{at{"),
            CaselessLiteral("{at}"),
            CaselessLiteral("}at{"),
            CaselessLiteral("}at}"),
            CaselessLiteral("{at"),
            CaselessLiteral("at{"),
            CaselessLiteral("}at"),
            CaselessLiteral("at}"),
            # 'et' - enclosed with { and }
            CaselessLiteral("{et{"),
            CaselessLiteral("{et}"),
            CaselessLiteral("}et{"),
            CaselessLiteral("}et}"),
            CaselessLiteral("{et"),
            CaselessLiteral("et{"),
            CaselessLiteral("}et"),
            CaselessLiteral("et}"),
            # 'arroba' - enclosed with { and }
            CaselessLiteral("{arroba{"),
            CaselessLiteral("{arroba}"),
            CaselessLiteral("}arroba{"),
            CaselessLiteral("}arroba}"),
            CaselessLiteral("{arroba"),
            CaselessLiteral("arroba{"),
            CaselessLiteral("}arroba"),
            CaselessLiteral("arroba}"),
            # additional patterns
            CaselessLiteral("-at-"),
            CaselessLiteral("-et-"),
            CaselessLiteral("-arroba-"),
        ]
    )
    + Optional(White(ws=' \t'))
).addParseAction(replaceWith("@"))

more_at_fanging_patterns = (
    not_uppercase_word_regex
    + Combine(
        Optional(White(ws=' \t'))
        + Or([Literal("AT"), Literal("ET"), Literal("ARROBA")])
        + Optional(White(ws=' \t'))
    ).addParseAction(replaceWith("@"))
    + NotAny(uppercase_word)
)

colon_slash_slash_fanging_patterns = Combine(
    Optional(White(ws=' \t'))
    + Or(
        [
            # '://' - enclosed with ( and )
            CaselessLiteral("(://("),
            CaselessLiteral("(://)"),
            CaselessLiteral(")://("),
            CaselessLiteral(")://)"),
            CaselessLiteral("(://"),
            CaselessLiteral("://("),
            CaselessLiteral(")://"),
            CaselessLiteral("://)"),
            # '://' - enclosed with [ and ]
            CaselessLiteral("[://["),
            CaselessLiteral("[://]"),
            CaselessLiteral("]://["),
            CaselessLiteral("]://]"),
            CaselessLiteral("[://"),
            CaselessLiteral("://["),
            CaselessLiteral("]://"),
            CaselessLiteral("://]"),
            # '://' - enclosed with { and }
            CaselessLiteral("{://{"),
            CaselessLiteral("{://}"),
            CaselessLiteral("}://{"),
            CaselessLiteral("}://}"),
            CaselessLiteral("{://"),
            CaselessLiteral("://{"),
            CaselessLiteral("}://"),
            CaselessLiteral("://}"),
        ]
    )
    + Optional(White(ws=' \t'))
).addParseAction(replaceWith("://"))

colon_fanging_patterns = Combine(
    Optional(White(ws=' \t'))
    + Or(
        [
            # ':' - enclosed with ( and )
            CaselessLiteral("(:("),
            CaselessLiteral("(:)"),
            CaselessLiteral("):("),
            CaselessLiteral("):)"),
            CaselessLiteral("(:"),
            CaselessLiteral(":("),
            # CaselessLiteral("):"), # this is commented and is NOT used to fang indicators b/c this may appear in real text
            CaselessLiteral(":)"),
            # ':' - enclosed with [ and ]
            CaselessLiteral("[:["),
            CaselessLiteral("[:]"),
            CaselessLiteral("]:["),
            CaselessLiteral("]:]"),
            CaselessLiteral("[:"),
            CaselessLiteral(":["),
            CaselessLiteral("]:"),
            CaselessLiteral(":]"),
            # ':' - enclosed with { and }
            CaselessLiteral("{:{"),
            CaselessLiteral("{:}"),
            CaselessLiteral("}:{"),
            CaselessLiteral("}:}"),
            CaselessLiteral("{:"),
            CaselessLiteral(":{"),
            CaselessLiteral("}:"),
            CaselessLiteral(":}"),
        ]
    )
    + Optional(White(ws=' \t'))
).addParseAction(replaceWith(":"))

http_fanging_patterns = Combine(
    # Optional(White(ws=' \t')) +
    Or(
        [
            # 'http' - enclosed with ( and )
            CaselessLiteral("(http("),
            CaselessLiteral("(http)"),
            CaselessLiteral(")http("),
            CaselessLiteral(")http)"),
            CaselessLiteral("(http"),
            CaselessLiteral("http("),
            CaselessLiteral(")http"),
            CaselessLiteral("http)"),
            # 'http' - enclosed with [ and ]
            CaselessLiteral("[http["),
            CaselessLiteral("[http]"),
            CaselessLiteral("]http["),
            CaselessLiteral("]http]"),
            CaselessLiteral("[http"),
            CaselessLiteral("http["),
            CaselessLiteral("]http"),
            CaselessLiteral("http]"),
            # 'http' - enclosed with { and }
            CaselessLiteral("{http{"),
            CaselessLiteral("{http}"),
            CaselessLiteral("}http{"),
            CaselessLiteral("}http}"),
            CaselessLiteral("{http"),
            CaselessLiteral("http{"),
            CaselessLiteral("}http"),
            CaselessLiteral("http}"),
        ]
    )
    # + Optional(White(ws=' \t'))
).addParseAction(replaceWith("http"))

www_fanging_patterns = Combine(
    Or(
        [
            # 'www' - enclosed with ( and )
            CaselessLiteral("(www("),
            CaselessLiteral("(www)"),
            CaselessLiteral(")www("),
            CaselessLiteral(")www)"),
            CaselessLiteral("(www"),
            CaselessLiteral("www("),
            CaselessLiteral(")www"),
            CaselessLiteral("www)"),
            # 'www' - enclosed with [ and ]
            CaselessLiteral("[www["),
            CaselessLiteral("[www]"),
            CaselessLiteral("]www["),
            CaselessLiteral("]www]"),
            CaselessLiteral("[www"),
            CaselessLiteral("www["),
            CaselessLiteral("]www"),
            CaselessLiteral("www]"),
            # 'www' - enclosed with { and }
            CaselessLiteral("{www{"),
            CaselessLiteral("{www}"),
            CaselessLiteral("}www{"),
            CaselessLiteral("}www}"),
            CaselessLiteral("{www"),
            CaselessLiteral("www{"),
            CaselessLiteral("}www"),
            CaselessLiteral("www}"),
        ]
    )
).addParseAction(replaceWith("www"))

comma_fanging_patterns = Combine(
    Optional(White(ws=' \t'))
    + Or(
        [
            # ',' - enclosed with ( and )
            CaselessLiteral("(,("),
            CaselessLiteral("(,)"),
            CaselessLiteral("),("),
            CaselessLiteral("),)"),
            CaselessLiteral("(,"),
            CaselessLiteral(",("),
            # CaselessLiteral("),"), # this is commented and is NOT used to fang indicators b/c this may appear in real text
            CaselessLiteral(",)"),
            # ',' - enclosed with [ and ]
            CaselessLiteral("[,["),
            CaselessLiteral("[,]"),
            CaselessLiteral("],["),
            CaselessLiteral("],]"),
            CaselessLiteral("[,"),
            CaselessLiteral(",["),
            CaselessLiteral("],"),
            CaselessLiteral(",]"),
            # ',' - enclosed with { and }
            CaselessLiteral("{,{"),
            CaselessLiteral("{,}"),
            CaselessLiteral("},{"),
            CaselessLiteral("},}"),
            CaselessLiteral("{,"),
            CaselessLiteral(",{"),
            CaselessLiteral("},"),
            CaselessLiteral(",}"),
        ]
    )
    + Optional(White(ws=' \t'))
).addParseAction(replaceWith(","))

odd_url_scheme_form = alphanum_word_start + Or(
    [
        Combine(
            Word("Hh")
            + Word(alphas, exact=2).addParseAction(replaceWith("tt"))
            + Word("Pp")
            + Optional(Word("Ss"))
            + Word(":")
        ),
        Combine(Word(alphas, exact=5) + "://").addParseAction(replaceWith("https://")),
        Combine(Word(alphas, exact=4) + "://").addParseAction(replaceWith("http://")),
    ]
)
