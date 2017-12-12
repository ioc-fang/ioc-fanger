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

.. image:: https://readthedocs.org/projects/ioc-fanger/badge/?version=latest
        :target: https://ioc-fanger.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/ioc-fang/ioc_fanger/shield.svg
     :target: https://pyup.io/repos/github/ioc-fang/ioc_fanger/
     :alt: Updates

Python package to defang and refang indicators of compromise from text.


* Free software: MIT license
* Documentation: https://ioc-fanger.readthedocs.io

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

    ioc_fanger.defang("example.com http://bad.com/phishing.php")
    ioc_fanger.fang("example[.]com hXXp://bad[.]com/phishing.php")

Via Command Line
^^^^^^^^^^^^^^^^

Command-line functionality coming soon (see `#1 <https://github.com/ioc-fang/ioc_fanger/issues/1>`_)!

Credits
=======

This package was created with Cookiecutter_ and the `fhightower/python-project-template`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`fhightower/python-project-template`: https://github.com/fhightower/python-project-template
