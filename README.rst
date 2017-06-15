***************
Mopidy-Notifier
***************

.. image:: https://pypip.in/v/Mopidy-Notifier/badge.png
    :target: https://pypi.python.org/pypi/Mopidy-Notifier/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/Mopidy-Notifier/badge.png
    :target: https://pypi.python.org/pypi/Mopidy-Notifier/
    :alt: Number of PyPI downloads


`Mopidy <http://www.mopidy.com>`_ extension for displaying the Trackinfo (Song,
Artist and Album) in notifications in either the Notification Center of Mac OS
X 10.8 and higher, using the command-line tool `terminal-notifier
<https://github.com/alloy/terminal-notifier>`_ , or via libnotify on Linux
systems, using `notify-send` (usually bundled with libnotify).


Installation
============

Install the ``mopidy-notifier`` package from the
`mopidy/mopidy <https://github.com/mopidy/homebrew-mopidy>`_ Homebrew tap::

    brew install mopidy-notifier

Now you should be all set up!

Alternatively, first install `terminal-notifier <https://github.com/alloy/terminal-notifier>`_
via Homebrew::

    brew install terminal-notifier

Then install ``mopidy-notifier`` from PyPI::

    pip install mopidy-notifier


Configuration
=============

The extension is enabled by default when it is installed.
To disable it, add the following to your Mopidy config file::

    [notifier]
    enabled = false

The following configuration values are available:

- ``notifier/enabled``: If the extension should be eneabled or not. Defaults to ``true``.
- ``notifier/on_start``: Whether a notification should be displayed on mopidy start. Defaults to ``true``.
- ``notifier/on_start_message``: The notification's message displayed on mopidy start. Defaults to ``Starting...``.
- ``notifier/on_stop``: Whether a notification should be displayed on mopidy close. Defaults to ``true``.
- ``notifier/on_stop_message``: The notification's message displayed on mopidy start. Defaults to ``Shutting down...``.
- ``notifier/message_format``: Format of the notification main message. Defaults to ``{artists} - {album}`` on OSX and ``{song}\\n{artists} - {album}`` on Linux.
- ``notifier/subtitle_format``: Format of the notification's subtitle. Only available on OSX. Defaults to ``{song}``.
- ``notifier/album_art``: Whether or not the album art for the current song should be fetched and sent with the notification. Defaults to ``false``.
- ``notifier/album_art_size``: Size of the album art icon sent to the notification. Defaults to ``64``.
- ``notifier/default_album_art``: Path to the default image when no album art could be fetched.


Project resources
=================

- `Source code <https://github.com/sauberfred/mopidy-notifier>`_
- `Issue tracker <https://github.com/sauberfred/mopidy-notifier/issues>`_
- `Download development snapshot <https://github.com/sauberfred/mopidy-notifier/tarball/master#egg=Mopidy-Notifier-dev>`_


Changelog
=========

v0.3.3 (2015-04-17)
-------------------

- Fixes a bug with displaying the songname on Linux

v0.3.2 (2015-02-14)
-------------------

- Now displays the songname

v0.3.1 (2014-12-28)
-------------------

- Support for Linux/libnotify.

v0.3.0 (2014-02-04)
-------------------

- Require Mopidy >= 0.18.

v0.2.0 (2013-10-20)
-------------------

- Initial release.
