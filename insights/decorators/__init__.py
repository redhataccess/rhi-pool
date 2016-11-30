import unittest
from insights.configs import settings
from functools import wraps


def setting_is_set(option):
    """Return either ``True`` or ``False`` if a Insights section setting is
    set or not respectively.
    """
    if not settings.configured:
        settings.configure()
    # Example: `settings.sat62`
    if getattr(settings, option).validate():
        return False
    return True


def skip_if_not_set(*options):
    """Skips test if expected configuration is not set.
        Decorating a method::
            @skip_if_not_set('sat62')
            def test_something(self):
                self.assertTrue(True)
        Decorating an entire class::
            class FeatureTestCase(insights.test.TestCase):
                @skip_if_not_set('sat62')
                def setUp(self):
                    pass
                def test_something(self):
                    self.assertTrue(True)
    """

    options_set = set(options)
    if not options_set.issubset(settings.all_features):
        invalid = options_set.difference(settings.all_features)
        raise ValueError(
            'Features: "{0}" not found. Available ones are: "{1}"',
            format(
                ', '.join(invalid),
                ', '.join(settings.all_features)
            )
        )

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            missing = []
            for option in options:
                #Example: settings.sat62
                if not setting_is_set(option):
                    missing.append(option)
            if not missing:
                return func(*args, **kwargs)
            raise unittest.SkipTest(
                'Missing configuration for: {0}.'.format(', '.join(missing)))
        return wrapper
    return decorator

