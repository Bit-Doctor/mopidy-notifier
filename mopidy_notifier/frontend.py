from __future__ import unicode_literals

import re
import StringIO
import urllib2
import os.path
import subprocess
import tempfile
import pykka
import sys
from operator import attrgetter

from PIL import Image
from mopidy.core import CoreListener

class NotifierFrontend(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super(NotifierFrontend, self).__init__()
        self.config = config['notifier']
        self.core = core
        if self.config.get('album_art', False):
            self.dirpath = tempfile.mkdtemp()

    def notify(self, message, subtitle, album_art=None):
        if sys.platform.startswith('darwin'):
            call = ['terminal-notifier', '-title', 'Mopidy', '-subtitle', subtitle, '-message', message, '-group', 'mopidy']
            icon_arg = '--contentImage {}'.format(album_art)
        elif sys.platform.startswith('linux'):
            call = ['notify-send', 'Mopidy', message]
            icon_arg = '--icon={}'.format(album_art)
        else:
            # Unsupported system
            raise EnvironmentError((1, "This operating system is not supported."))

        if album_art:
            call.append(icon_arg)

        subprocess.call(call)

    def on_start(self):
        if self.config['on_start']:
            self.notify(self.config['on_start_message'], '')

    def on_stop(self):
        if self.config['on_stop']:
            self.notify(self.config['on_stop_message'], '')

    def notification_format(self, track):
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

    def fetch_album_art(self, track):
        album = track.album.name
        size = (self.config['album_art_size'], self.config['album_art_size'])

        if self.config['album_art']:
            album_slug = re.sub('[^0-9a-zA-Z]+', '_', album)
            album_art = '{}/{}.png'.format(self.dirpath, album_slug)
            if not os.path.isfile(album_art):
                images = self.core.library.get_images([track.uri]).get()[track.uri]
                if len(images) > 0:
                    biggest = max(images, key=attrgetter('width'))
                    raw = StringIO.StringIO(urllib2.urlopen(biggest.uri).read())
                    im = Image.open(raw)
                    im.thumbnail(size, Image.ANTIALIAS)
                    im.save(album_art, "PNG")
                else:
                    album_art = self.config['default_album_art']

        else:
            album_art = self.config['default_album_art']

        return album_art

    def track_playback_started(self, tl_track):
        track = tl_track.track
        message, subtitle = self.notification_format(track)
        album_art = self.fetch_album_art(track)
        self.notify(message, subtitle, album_art)
