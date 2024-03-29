## Installation

The recommended means of installation is using [pip](https://pypi.python.org/pypi/pip/):

`pip install ioc-fanger`

Alternatively, you can install ioc-fanger as follows:

```shell
git clone https://github.com/ioc-fang/ioc_fanger.git && cd ioc_fanger;
python setup.py install --user;
```

## Usage

### Via Python

Use ioc-fanger as follows:

```python
import ioc_fanger

ioc_fanger.defang("example.com http://bad.com/phishing.php")  # example[.]com hXXp://bad[.]com/phishing[.]php
ioc_fanger.fang("example[.]com hXXp://bad[.]com/phishing[.]php")  # example.com http://bad.com/phishing.php
```

(you can test this in the browser [here](/#use-the-package-live))

### Via Command Line

Once you install the package, there will be two commands available in the command line:

- `fang`
- `defang`

After each command, provide the text you would like to fang/defang:

```shell
fang "example[.]com"  # example.com
```

```shell
defang "example.com"  # example[.]com
```
