from __future__ import unicode_literals

import os

from mopidy import config, ext


__version__ = '0.3.3'


class Extension(ext.Extension):

    dist_name = 'Mopidy-Notifier'
    ext_name = 'notifier'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()

        schema['on_start'] = config.Boolean()
        schema['on_start_message'] = config.String()
        schema['on_stop'] = config.Boolean()
        schema['on_stop_message'] = config.String()

        schema['message_format'] = config.String(optional=True)
        schema['subtitle_format'] = config.String(optional=True)

        schema['album_art'] = config.Boolean()
        schema['album_art_size'] = config.Integer(minimum=8, maximum=512)
        schema['default_album_art'] = config.String(optional=True)

        return schema

    def setup(self, registry):
        from .frontend import NotifierFrontend
        registry.add('frontend', NotifierFrontend)
