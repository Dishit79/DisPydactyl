from dispydactyl.api import base
from dispydactyl.api.base import PterodactylAPI
from dispydactyl.exceptions import BadRequestError
from dispydactyl.responses import PaginatedResponse


class User(PterodactylAPI):
    """Class for interacting with the Pterdactyl Client API."""

    def list_users(self, search=None):
        """List all users.

        Args:
            search(str): Filter user list by search term.
        """
        params = {}
        if search is not None:
            params = {'search': search}
        endpoint = 'application/users'
        response = self._api_request(endpoint=endpoint, params=params)
        return PaginatedResponse(self, endpoint, response)

    def get_user_info(self, user_id=None, external_id=None, detail=True):
        """List detailed user information for specified user_id.

        Args:
            user_id(int): Pterodactyl user ID
            external_id(int): User ID from external system like WHMCS
            detail(bool): If True includes created and updated timestamps.
        """
        if not user_id and not external_id:
            raise BadRequestError('Must specify either user_id or external_id.')
        if user_id and external_id:
            raise BadRequestError('Specify either user_id or external_id, '
                                  'not both.')

        if user_id:
            endpoint = 'application/users/%s' % user_id
        else:
            endpoint = 'application/users/external/%s' % external_id

        response = self._api_request(endpoint=endpoint)
        return base.parse_response(response, detail=detail)

    def create_user(self, username, email, first_name, last_name,
                    external_id=None, password=None, root_admin=False,
                    language='en'):
        """Creates a primary user on the Pterodactyl panel.

        Args:
            username(str): Username, must be unique, required.
            email(str): Full email, required.
            first_name(str): User's first name, required.
            last_name(str): User's last name, required.
            external_id(str): User ID from external system like WHMCS.
            password(str): Optionally specify a password.  If not specified
                    user will receive an email to setup their password.
            root_admin(bool): Whether the account is an admin.
            language(str): Used to specify the default language for an account.
        """
        data = {'username': username,
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'external_id': external_id,
                'password': password,
                'root_admin': root_admin,
                'language': language,
                }
        response = self._api_request(endpoint='application/users',
                                     mode='POST', data=data)
        return base.parse_response(response, detail=True)

    def edit_user(self, user_id, username, email, first_name, last_name,
                  external_id=None, password=None, root_admin=False,
                  language='en'):
        """Edits an existing user on the Pterodactyl panel.

        The user_id is used to find the existing user.  All other parameters
        will be updated on that user_id.

        Args:
            user_id(int): Pterodactyl User ID for the user to update.
            username(str): Username, must be unique, required.
            email(str): Full email, required.
            first_name(str): User's first name, required.
            last_name(str): User's last name, required.
            external_id(str): User ID from external system like WHMCS.
            password(str): Optionally specify a password.  If not specified
                    user will receive an email to setup their password.
            root_admin(bool): Whether the account is an admin.
            language(str): Used to specify the default language for an account.
        """
        data = {'username': username,
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'external_id': external_id,
                'password': password,
                'root_admin': root_admin,
                'language': language,
                }
        response = self._api_request(endpoint='application/users/%s' % user_id,
                                     mode='PATCH', data=data)
        return base.parse_response(response, detail=True)

    def delete_user(self, user_id=None, external_id=None, detail=True):
        """Deletes the specified user.

        Will look up by external_id if provided.  This action cannot be
        reversed so use with care.

        Args:
            user_id(int): Pterodactyl user ID
            external_id(int): User ID from external system like WHMCS
            detail(bool): If True includes created and updated timestamps.
        """
        if not user_id and not external_id:
            raise BadRequestError('Must specify either user_id or external_id.')
        if user_id and external_id:
            raise BadRequestError('Specify either user_id or external_id, '
                                  'not both.')

        if external_id:
            response = self._api_request(
                endpoint='application/users/external/%s' % external_id)
            user_id = response['attributes']['id']

        response = self._api_request(
            endpoint='application/users/%s' % user_id, mode='DELETE')
        return base.parse_response(response, detail=detail)
