import ckan.plugins.toolkit as t


class UserAuthorizer(object):

    @classmethod
    def show(cls, context, data_dict=None):
        current_user = context['auth_user_obj']
        requested_user_name = t.c.id

        if current_user == None:
            success = False
        elif current_user.name == requested_user_name:
            success = True
        else:
            success = not cls.is_restricted()

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
        return t.asbool(t.config.get('ckanext.hide_user_list'))