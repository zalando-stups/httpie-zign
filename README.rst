===========
httpie-zign
===========

Zign OAuth 2 plugin for `HTTPie <https://github.com/jkbr/httpie>`_.

`Zign <http://docs.stups.io/en/latest/components/zign.html>`_ is STUPS' command line client to generate OAuth2 access tokens.


Installation
------------

.. code-block:: bash

    $ pip install httpie-zign


You should now see ``zign`` under ``--auth-type`` in ``$ http --help`` output.


Usage
-----

.. code-block:: bash

    $ zign token -n mytok # generate named OAuth token "mytok"
    $ http --auth-type=zign --auth=mytok: https://example.org
    $ http --auth-type=zign -a mytok: https://example.org
