## About ioc-fanger

Python package to fang and defang [indicators of compromise](https://digitalguardian.com/blog/what-are-indicators-compromise) in text.

```python
import ioc_fanger

ioc_fanger.defang("example.com http://bad.com/phishing.php")  # example[.]com hXXp://bad[.]com/phishing[.]php
ioc_fanger.fang("example[.]com hXXp://bad[.]com/phishing[.]php")  # example.com http://bad.com/phishing.php
```

**Defanging** - converting indicators of compromise from the normal form (which can become links) to a form which cannot accidentally become a link:

`example.com => example[.]com`

**Fanging** - converting indicators of compromise from a defanged form to the normal, original form:

`example[.]com => example.com`

**What can it fang?**

Just about everything. Check out the [tests](https://github.com/ioc-fang/ioc_fanger/blob/master/tests/test_ioc_fanger.py) to see some examples of what this package can handle.

## Feedback

If you have any ideas to improve this package, please [raise an issue](https://github.com/ioc-fang/ioc-fanger/issues)!

## Other Helpful Projects

If you are working with indicators of compromise (a.k.a. observables), you may find the [ioc-finder](https://github.com/fhightower/ioc-finder) project helpful. The ioc-finder project parses indicators of compromise from text (using grammars).

## Credits

We created this package using [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [fhightower/python-project-template](https://github.com/fhightower/python-project-template) project template.
