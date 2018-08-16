*******************************
IOC Fanger
*******************************

.. image:: https://img.shields.io/pypi/v/ioc_fanger.svg
        :target: https://pypi.python.org/pypi/ioc_fanger

.. image:: https://img.shields.io/travis/ioc-fang/ioc_fanger.svg
        :target: https://travis-ci.org/ioc-fang/ioc_fanger

.. image:: https://codecov.io/gh/ioc-fang/ioc_fanger/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/ioc-fang/ioc_fanger
        
.. image:: https://api.codacy.com/project/badge/Grade/d1762339ba454fba87c02a1b7ea69052
        :target: https://www.codacy.com/app/fhightower/ioc_fanger

Python package to fang and defang `indicators of compromise <https://digitalguardian.com/blog/what-are-indicators-compromise>`_ in text.

**Defanging** - converting indicators of compromise from the normal form (which can become links) to a form which cannot accidentally become a link:

``example.com => example[.]com``

**Fanging** - converting indicators of compromise from a defanged form to the normal, original form:

``example[.]com => example.com``

Installation
============

The recommended means of installation is using `pip <https://pypi.python.org/pypi/pip/>`_:

``pip install ioc_fanger``

Alternatively, you can install ioc_fanger as follows:

.. code-block:: shell

    git clone https://github.com/ioc-fang/ioc_fanger.git && cd ioc_fanger;
    python setup.py install --user;

Usage
=====

Via Python
^^^^^^^^^^

Use ioc_fanger as follows:

.. code-block:: python

    import ioc_fanger

    ioc_fanger.defang("example.com http://bad.com/phishing.php")  # example[.]com hXXp://bad[.]com/phishing[.]php
    ioc_fanger.fang("example[.]com hXXp://bad[.]com/phishing[.]php")  # example.com http://bad.com/phishing.php

Via Command Line
^^^^^^^^^^^^^^^^

Once the package is installed, there will be two commands available in the command line:

- ``fang``
- ``defang``

After each command, provide the text you would like to fang/defang:

.. code-block:: shell

    fang "example[.]com"  # example.com

.. code-block:: shell

    defang "example.com"  # example[.]com

Adding More Fanging/Defanging Options
=====================================

You can view the current fanging patterns `here <https://github.com/ioc-fang/ioc_fanger/blob/master/ioc_fanger/fang.json>`_ and the defanging patterns `here <https://github.com/ioc-fang/ioc_fanger/blob/master/ioc_fanger/defang.json>`_ .

To add more fanging options, edit `fang.json <https://github.com/ioc-fang/ioc_fanger/blob/master/ioc_fanger/fang.json>`_ and add an entry for the new pattern you would like to fang. The available keys for each entry are:

- ``find`` (required): This is the string pattern you would like to find
- ``replace`` (required): This is the string used to replace all instances to pattern specified by the ``find`` key
- ``case_sensitive`` (optional): If this is ``true``, the pattern specified by the ``find`` key will be treated as case sensitive (it will only be replaced if the case is an exact match)

Credits
=======

This package was created with Cookiecutter_ and the `fhightower/python-project-template`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`fhightower/python-project-template`: https://gitlab.com/fhightower/python-project-template
