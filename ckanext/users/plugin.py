import ckan.plugins as p
import ckan.plugins.toolkit as t

from ckan.lib.plugins import DefaultTranslation
from ckanext.users.lib.user_authorizer import UserAuthorizer


class UsersPlugin(p.SingletonPlugin, DefaultTranslation):

    p.implements(p.IConfigurer)
    p.implements(p.ITranslation)
    p.implements(p.IAuthFunctions)

    # IConfigurer

    def update_config(self, config_):
        t.add_template_directory(config_, 'templates')

    def update_config_schema(self, schema):
        boolean_validator = t.get_validator('boolean_validator')

        schema.update({
            'ckanext.hide_user_list': [ boolean_validator ],
        })

        return schema

    ## IAuthFunctions

    def get_auth_functions(self):
        return {
            'user_show': UserAuthorizer.show,
            'user_list': UserAuthorizer.list
        }