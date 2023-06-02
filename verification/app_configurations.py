from django.conf import settings


class GetFieldFromSettings:
    """
    This class fetches the attributes that are defined in settings.py of your project by user OR Django itself.
    self.default_configs : is a dict with keys as the names used in this app and values being a tuple of 
                           attributes defined in settings.py and their corresponding default values if not found.
                               
                               self.default_config = {
                                ...
                                'field_name_reference': (
                                    'NAME IN SETTINGS.PY',
                                    'default value'
                                ),
                                ...
                           }

    There is a special case in "get" method, if you set "VERIFICATION_SUCCESS_TEMPLATE" as None is settings.py, it 
    will skip the intermidiate page where success information is displayed. (This is better explained in docs.)
    The "get" method takes the name of the attributes as input, checks for it in settings.py, 
            if found:
                returns the corresponding value.
            else:
                returns the default value from "self.defaults_configs".
    """

    def __init__(self):

        self.defaults_configs = {
            'debug_settings': (
                'DEBUG', 
                False
            ),

            'subject': (
                "SUBJECT", 
                "Email Verification Mail"
            ),

            'email_field_name': (
                "EMAIL_FIELD_NAME", 
                "email",
            ),

            'html_message_template': (
                "HTML_MESSAGE_TEMPLATE", 
                'verification/email_verification_msg.html'
            ),

            'from_alias': (
                "DEFAULT_FROM_EMAIL", 
                'noreply<noreply@gmail.com>',
            ),

            'verification_success_redirect': (
                'LOGIN_URL', 
                '/'
            ),

            'verification_success_template': (
                'VERIFICATION_SUCCESS_TEMPLATE',
                'verification/email_verification_successful.html'
            ),

            'verification_success_msg': (
                'VERIFICATION_SUCCESS_MSG',
                "Your Email is verified successfully and account has been activated." 
                "You can login with the credentials now..."
            ),

            'verification_failed_template': (
                'VERIFICATION_FAILED_TEMPLATE',
                'verification/email_verification_failed.html'
            ),

            'verification_failed_redirect': (
                'VERIFICATION_FAILED_REDIRECT',
                '/'
            ),

            'verification_failed_msg': (
                'VERIFICATION_FAILED_MSG',
                "There is something wrong with this link, can't verify the user..."
            ),
        }

    def get(self, field_name, raise_exception=True, default_type=str):
        attr = getattr(
            settings, 
            self.defaults_configs[field_name][0],  # get field from settings
            self.defaults_configs[field_name][1]   # get default value if field not defined
        )
        if (attr == '' or attr is None or not isinstance(field_name, default_type)) and raise_exception:
            if field_name == 'verification_success_template' and attr is None:
                return None
            raise AttributeError
        return attr