# -----------------------------------------------------------------------------
# Standard type settings
# -----------------------------------------------------------------------------

INTEGER_SETTING = 1

BOOLEAN_SETTING = False

STRING_SETTING = 'stringy'

TUPLES_SETTING = (
    (1, 'One'),
    (2, 'Two'),
    (3, 'Three'),
    (4, 'Four'),
)


# -----------------------------------------------------------------------------
# Model/class and module settings
# -----------------------------------------------------------------------------

VALID_MODEL = 'tests.DefaultModel'

INCORRECT_FORMAT_MODEL = 'apputils.tests.DefaultModel'

UNAVAILABLE_MODEL = 'apputils.UnavailableModel'

VALID_OBJECT = 'apputils.tests.classes.DefaultClass'

INCORRECT_FORMAT_OBJECT = 'DefaultClass'

MODULE_UNAVAILABLE_OBJECT = 'apputils.imaginary_module.Class'

OBJECT_UNAVAILABLE_OBJECT = 'apputils.tests.classes.NonExistent'

VALID_MODULE = 'apputils.tests.modules.default_module'

UNAVAILABLE_MODULE = 'apputils.tests.modules.imaginary_module'


# -----------------------------------------------------------------------------
# Deprecations
# -----------------------------------------------------------------------------

DEPRECATED_SETTING = 'i-am-deprecated'

RENAMED_SETTING = 'i-have-been-renamed'

RENAMED_TO_SETTING = 'i-am-a-direct-replacement-of-another-setting'

SUPERSEDED_SETTING = 'i-have-been-superseded'

SUCCESSOR_SETTING = 'i-have-succeeded-another-setting'
