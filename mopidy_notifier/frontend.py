from __future__ import unicode_literals

import subprocess
import pykka
import sys

from mopidy.core import CoreListener


class NotifierFrontend(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super(NotifierFrontend, self).__init__()
        self.config = config['notifier']
        self.core = core

    def notify(self, message, subtitle):
        if sys.platform.startswith('darwin'):
            call = ['terminal-notifier', '-title', 'Mopidy', '-subtitle', subtitle, '-message', message, '-group', 'mopidy']
        elif sys.platform.startswith('linux'):
            call = ['notify-send', 'Mopidy', message, '--icon=multimedia-player']
        else:
            # Unsupported system
            raise EnvironmentError((1, "This operating system is not supported."))
        subprocess.call(call)

    def on_start(self):
        if self.config['on_start']:
            self.notify(self.config['on_start_message'], '')

    def on_stop(self):
        if self.config['on_stop']:
            self.notify(self.config['on_stop_message'], '')

    def notification_format(self, tl_track):
        track = tl_track.track
        song = track.name
        artists = ', '.join([a.name for a in track.artists])
        album = track.album.name

        subtitle_format = self.config['subtitle_format']
        message_format = self.config['message_format']

        if sys.platform.startswith('darwin'):
            subtitle_format = subtitle_format or '{artists} - {album}'
            message_format = message_format or '{song}'
        elif sys.platform.startswith('linux'):
            subtitle_format = ''
            message_format = message_format or '{song}\\n{artists} - {album}'
        else:
            # Unsupported system
            raise EnvironmentError((1, "This operating system is not supported."))

        message = message_format.format(song=song, artists=artists, album=album)
        subtitle = subtitle_format.format(song=song, artists=artists, album=album)
        return (message, subtitle)

    def track_playback_started(self, tl_track):
        message, subtitle = self.notification_format(tl_track)
        self.notify(message, subtitle)
