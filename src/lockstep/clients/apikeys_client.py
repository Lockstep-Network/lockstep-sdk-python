#
# Lockstep Platform SDK for Python
#
# (c) 2021-2023 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2023 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

from lockstep.lockstep_response import LockstepResponse
from lockstep.models.errorresult import ErrorResult
from lockstep.fetch_result import FetchResult
from lockstep.models.actionresultmodel import ActionResultModel
from lockstep.models.apikeymodel import ApiKeyModel

class ApiKeysClient:
    """
    API methods related to ApiKeys
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_api_key(self, id: str, include: str) -> LockstepResponse[ApiKeyModel]:
        """
        Retrieves the API Key with this identifier.

        An API Key is an authentication token that you may use with the
        Lockstep API. Because API Keys do not have an expiration date,
        they are well suited for unattended processes. Each API Key is
        associated with a user, and may be revoked to prevent it from
        accessing the Lockstep API. When you create an API Key, make
        sure to save the value in a secure location. Lockstep cannot
        retrieve an API Key once it is created.

        For more information, see [API
        Keys](https://developer.lockstep.io/docs/api-keys).

        Parameters
        ----------
        id : str
            The unique ID number of the API Key to retrieve
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. No collections are currently available
            but may be offered in the future.
        """
        path = f"/api/v1/ApiKeys/{id}"
        result = self.client.send_request("GET", path, None, {"include": include}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ApiKeyModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def revoke_api_key(self, id: str) -> LockstepResponse[ActionResultModel]:
        """
        Immediately revokes the API Key with the specified id so it
        cannot be used to call the API.

        The Lockstep Platform guarantees that revocation will be
        received by all servers within five minutes of revocation. API
        calls made using this API key after the revocation will fail. A
        revoked API Key cannot be un-revoked and may be removed 60 days
        after revocation.

        An API Key is an authentication token that you may use with the
        Lockstep API. Because API Keys do not have an expiration date,
        they are well suited for unattended processes. Each API Key is
        associated with a user, and may be revoked to prevent it from
        accessing the Lockstep API. When you create an API Key, make
        sure to save the value in a secure location. Lockstep cannot
        retrieve an API Key once it is created.

        For more information, see [API
        Keys](https://developer.lockstep.io/docs/api-keys).

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of this API Key
        """
        path = f"/api/v1/ApiKeys/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ActionResultModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_api_key(self, body: ApiKeyModel) -> LockstepResponse[ApiKeyModel]:
        """
        Creates an API key with the specified name.

        An API Key is an authentication token that you may use with the
        Lockstep API. Because API Keys do not have an expiration date,
        they are well suited for unattended processes. Each API Key is
        associated with a user, and may be revoked to prevent it from
        accessing the Lockstep API. When you create an API Key, make
        sure to save the value in a secure location. Lockstep cannot
        retrieve an API Key once it is created.

        For more information, see [API
        Keys](https://developer.lockstep.io/docs/api-keys).

        Parameters
        ----------
        body : ApiKeyModel
            Metadata about the API Key to create.
        """
        path = "/api/v1/ApiKeys"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ApiKeyModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_api_keys(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[ApiKeyModel]]:
        """
        Queries API Keys for this user using the specified filtering,
        sorting, nested fetch, and pagination rules requested.

        An API Key is an authentication token that you may use with the
        Lockstep API. Because API Keys do not have an expiration date,
        they are well suited for unattended processes. Each API Key is
        associated with a user, and may be revoked to prevent it from
        accessing the Lockstep API. When you create an API Key, make
        sure to save the value in a secure location. Lockstep cannot
        retrieve an API Key once it is created.

        For more information, see [API
        Keys](https://developer.lockstep.io/docs/api-keys).

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. No collections are currently available
            but may be offered in the future.
        order : str
            The sort order for this query. See See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageSize : int
            The page size for results (default 250, maximum of 500). See
            [Searchlight Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        """
        path = "/api/v1/ApiKeys/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), ApiKeyModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
