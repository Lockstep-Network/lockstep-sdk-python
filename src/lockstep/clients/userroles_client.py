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

from lockstep.lockstep_response import LockstepResponse

class UserRolesClient:

    def __init__(self, client):
        self.client = client

    """
    Retrieves the User Role with this identifier.

    Parameters
    ----------
    id : str
        The unique ID number of the User Role to retrieve
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. No collections are currently available but 
        may be offered in the future
    """
    def retrieve_user_role(self, id: str, include: str) -> LockstepResponse:
        path = f"/api/v1/UserRoles/{id}"
        return self.client.send_request("GET", path, None, {id: str, include: str})

    """
    Queries User Roles for this account using the specified filtering, 
    sorting, nested fetch, and pagination rules requested.

    Parameters
    ----------
    filter : str
        The filter for this query. See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. No collections are currently available but 
        may be offered in the future
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
    def query_user_roles(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/UserRoles/query"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})
