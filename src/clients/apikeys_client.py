#
# Lockstep Software Development Kit for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Ted Spence <tspence@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @version    2022.2
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


class ApiKeysClient:
    from src.api.lockstep_response import LockstepResponse
    from src.api.lockstep_api import LockstepApi
    from src.models.apikeymodel import ApiKeyModel

    def __init__(self, client: LockstepApi):
        self.client = client

    """
    Retrieves the API Key with this identifier. 

    An API Key is an authentication token that you may use with the 
    Lockstep API. Because API Keys do not have an expiration date, they 
    are well suited for unattended processes. Each API Key is associated 
    with a user, and may be revoked to prevent it from accessing the 
    Lockstep API. When you create an API Key, make sure to save the 
    value in a secure location. Lockstep cannot retrieve an API Key once 
    it is created. For more information, see [API 
    Keys](https://developer.lockstep.io/docs/api-keys).

    Parameters
    ----------
    id : str
        The unique ID number of the API Key to retrieve
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. No collections are currently available but 
        may be offered in the future.
    """
    def retrieve_api_key(self, id: str, include: str) -> LockstepResponse:
        path = f"/api/v1/ApiKeys/{id}"
        return self.client.send_request("GET", path, None, {id: str, include: str})

    """
    Immediately revokes the API Key with the specified id so it cannot 
    be used to call the API. The Lockstep Platform guarantees that 
    revocation will be received by all servers within five minutes of 
    revocation. API calls made using this API key after the revocation 
    will fail. A revoked API Key cannot be un-revoked and may be removed 
    60 days after revocation. 

    An API Key is an authentication token that you may use with the 
    Lockstep API. Because API Keys do not have an expiration date, they 
    are well suited for unattended processes. Each API Key is associated 
    with a user, and may be revoked to prevent it from accessing the 
    Lockstep API. When you create an API Key, make sure to save the 
    value in a secure location. Lockstep cannot retrieve an API Key once 
    it is created. For more information, see [API 
    Keys](https://developer.lockstep.io/docs/api-keys).

    Parameters
    ----------
    id : str
        The unique Lockstep Platform ID number of this API Key
    """
    def revoke_api_key(self, id: str) -> LockstepResponse:
        path = f"/api/v1/ApiKeys/{id}"
        return self.client.send_request("DELETE", path, None, {id: str})

    """
    Creates an API key with the specified name. 

    An API Key is an authentication token that you may use with the 
    Lockstep API. Because API Keys do not have an expiration date, they 
    are well suited for unattended processes. Each API Key is associated 
    with a user, and may be revoked to prevent it from accessing the 
    Lockstep API. When you create an API Key, make sure to save the 
    value in a secure location. Lockstep cannot retrieve an API Key once 
    it is created. For more information, see [API 
    Keys](https://developer.lockstep.io/docs/api-keys).

    Parameters
    ----------
    body : ApiKeyModel
        Metadata about the API Key to create.
    """
    def create_api_key(self, body: ApiKeyModel) -> LockstepResponse:
        path = f"/api/v1/ApiKeys"
        return self.client.send_request("POST", path, body, {body: ApiKeyModel})

    """
    Queries API Keys for this user using the specified filtering, 
    sorting, nested fetch, and pagination rules requested. An API Key is 
    an authentication token that you may use with the Lockstep API. 
    Because API Keys do not have an expiration date, they are well 
    suited for unattended processes. Each API Key is associated with a 
    user, and may be revoked to prevent it from accessing the Lockstep 
    API. When you create an API Key, make sure to save the value in a 
    secure location. Lockstep cannot retrieve an API Key once it is 
    created. For more information, see [API 
    Keys](https://developer.lockstep.io/docs/api-keys).

    Parameters
    ----------
    filter : str
        The filter for this query. See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. No collections are currently available but 
        may be offered in the future.
    order : str
        The sort order for this query. See See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageSize : int
        The page size for results (default 200). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageNumber : int
        The page number for results (default 0). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    """
    def query_api_keys(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/ApiKeys/query"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})
