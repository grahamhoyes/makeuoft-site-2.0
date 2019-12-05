from wtforms.compat import string_types
from wtforms.validators import StopValidation


class DataRequiredIfOtherFieldEmpty:
    """
    Checks the field's data is 'truthy' otherwise stops the validation chain.

    This validator checks that the ``data`` attribute on the field is a 'true'
    value (effectively, it does ``if field.data``.) Furthermore, if the data
    is a string type, a string containing only whitespace characters is
    considered false.

    If the data is empty, also removes prior errors (such as processing errors)
    from the field.

    **NOTE** this validator used to be called `Required` but the way it behaved
    (requiring coerced data, not input data) meant it functioned in a way
    which was not symmetric to the `Optional` validator and furthermore caused
    confusion with certain fields which coerced data to 'falsey' values like
    ``0``, ``Decimal(0)``, ``time(0)`` etc. Unless a very specific reason
    exists, we recommend using the :class:`InputRequired` instead.

    :param message:
        Error message to raise in case of a validation error.
    """
    field_flags = ('required', )

    def __init__(self, other_field, message=None):
        self.other_field = other_field
        self.message = message

    def __call__(self, form, field):
        other_field = getattr(form, self.other_field, None)
        if not field.data or isinstance(field.data, string_types) and not field.data.strip():
            if not other_field.data or isinstance(other_field.data, string_types) and not other_field.data.strip():
                if self.message is None:
                    message = field.gettext('This field is required.')
                else:
                    message = self.message

                field.errors[:] = []
                raise StopValidation(message)