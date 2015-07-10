===========
httpie-zign
===========

Zign OAuth 2 plugin for `HTTPie <https://github.com/jkbr/httpie>`_.


Installation
------------

.. code-block:: bash

    $ pip install httpie-zign


You should now see ``zign`` under ``--auth-type`` in ``$ http --help`` output.


Usage
-----

.. code-block:: bash

    $ http --auth-type=zign --auth='token-name:' example.org
