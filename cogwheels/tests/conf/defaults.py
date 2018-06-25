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

INCORRECT_FORMAT_MODEL = 'cogwheels.tests.DefaultModel'

UNAVAILABLE_MODEL = 'cogwheels.UnavailableModel'

VALID_OBJECT = 'cogwheels.tests.classes.DefaultClass'

INCORRECT_FORMAT_OBJECT = 'DefaultClass'

MODULE_UNAVAILABLE_OBJECT = 'cogwheels.imaginary_module.Class'

OBJECT_UNAVAILABLE_OBJECT = 'cogwheels.tests.classes.NonExistent'

VALID_MODULE = 'cogwheels.tests.modules.default_module'

UNAVAILABLE_MODULE = 'cogwheels.tests.modules.imaginary_module'


# -----------------------------------------------------------------------------
# Deprecations
# -----------------------------------------------------------------------------

DEPRECATED_SETTING = 'deprecated'

RENAMED_SETTING_OLD = 'renamed_old'

RENAMED_SETTING_NEW = 'renamed_new'

REPLACED_SETTING_OLD = 'replaced_old'

REPLACED_SETTING_NEW = 'replaced_new'