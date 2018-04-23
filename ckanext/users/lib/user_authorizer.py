import ckan.plugins.toolkit as t


class UserAuthorizer(object):

    @classmethod
    def show(cls, context, data_dict=None):
        controller_name = t.c.controller
        action_name = t.c.action
        current_user = context['auth_user_obj']

        if not cls.is_restricted():
            success = True
        elif current_user == None:
            success = False
        elif controller_name == 'user' and action_name == 'read':
            requested_user_name = t.c.id
            success = (current_user.name == requested_user_name)
        else:
            success = True

        return { 'success': success }

    @classmethod
    def list(cls, context, data_dict=None):
        current_user = context['auth_user_obj']

        if current_user == None:
            success = False
        else:
            success = not cls.is_restricted()

        return { 'success': success }

    @classmethod
    def is_restricted(cls):
        setting_value = t.config.get('ckanext.hide_user_list')
        if not setting_value:
            setting_value = False

        return t.asbool(setting_value)