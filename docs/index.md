# IOC Fanger

Welcome to the documentation for the `ioc-fanger` package!
This documentation is interactive so you can learn and explore the package live.

## Overview

Basically, this package can fang and defang [indicators of compromise](https://digitalguardian.com/blog/what-are-indicators-compromise) (a.k.a observables).

**Defanging** (e.g. `example.com => example[.]com`) converts indicators of compromise from their normal form (in which they may become links to malicious content) to a form which cannot accidentally become a link.

**Fanging** (e.g. `example[.]com => example.com`) is the opposite process which converts indicators of compromise from a defanged form to the normal, original form.

Check out the [tests](https://github.com/ioc-fang/ioc_fanger/blob/main/tests/test_ioc_fanger.py) to see what this package can fang/defang.

## Use the Package (LIVE!)

Copy this example and paste it in the terminal below to get an idea of what this package does:

```python
import ioc_fanger

ioc_fanger.fang("example[.]com hXXp://bad[.]com/phishing[.]php")
ioc_fanger.defang("example.com http://bad.com/phishing.php")
```

<div id="terminal"></div>

This terminal uses [Pyodide](https://pyodide.org/en/stable/index.html) to provide a Python3.9 runtime in the browser using [WebAssembly](https://webassembly.org/). Enjoy!

## Feedback

If you have any ideas to improve this package, please [raise an issue](https://github.com/ioc-fang/ioc-fanger/issues)!

## Other Helpful Projects

If you are working with indicators of compromise (a.k.a. observables), you may find the [ioc-finder](https://github.com/fhightower/ioc-finder) project helpful. The ioc-finder project parses indicators of compromise from text (using grammars).

## Credits

We created this package using [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [fhightower/python-project-template](https://github.com/fhightower/python-project-template) project template.
