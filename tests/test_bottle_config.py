""" Tests for `bottle_config` module. """

import bottle


def test_bottle_config():
    from bottle_config import Config
    app = bottle.Bottle()
    app.install(Config('tests.settings'))
    assert app.config['OPTION'] == 'VALUE'

    import os

    os.environ['BOTTLE_CONFIG'] = 'tests.config.production'
    app.install(Config())
    assert app.config['TEST1'] == 1
    assert app.config['TEST2'] == 1
    assert app.config['TEST3'] == 3
