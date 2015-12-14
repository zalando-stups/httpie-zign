===========
httpie-zign
===========

STUPS Zign OAuth 2 plugin for the `HTTPie <https://github.com/jkbr/httpie>`_ command line HTTP client.

`Zign <http://docs.stups.io/en/latest/components/zign.html>`_ is STUPS' command line client to generate OAuth2 access tokens.


Installation
------------

.. code-block:: bash

    $ pip install httpie-zign


You should now see ``zign`` under ``--auth-type`` in ``$ http --help`` output.


Usage
-----

This plugin takes the Zign token name as the ``--auth`` username.
The ``--auth`` password is used to specify to OAuth scopes.
A named Zign OAuth 2 token is created and used with the specified scopes:

.. code-block:: bash

    $ http --auth-type=zign --auth=mytok:myscope https://example.org
    $ http --auth-type=zign -a mytok:myscope1,scope2 https://example.org
    $ http --auth-type=zign -a mytok: https://example.org  # use default scopes

You can list the created tokens using the Zign CLI:

.. code-block:: bash

    $ zign li

You can set the default ``--auth-type=zign`` option in the ``~/.httpie/config.json`` file for convenience:

.. code-block:: bash

    $ echo '{"default_options": ["--auth-type=zign"]}' > ~/.httpie/config.json
    $ http -a mytok: https://example.org # that's much shorter now :-)

