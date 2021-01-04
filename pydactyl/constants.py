"""Pydactyl constants."""

__version__ = '0.1.13'

USER_AGENT = 'Dispydactyl/' + __version__
POWER_SIGNALS = ('start', 'stop', 'restart', 'kill')
USE_SSL = {True: 'https', False: 'http'}
REQUEST_TYPES = ('GET', 'POST', 'PATCH', 'DELETE')
