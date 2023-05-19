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
from lockstep.models.magiclinkmodel import MagicLinkModel

class MagicLinksClient:
    """
    API methods related to MagicLinks
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_magic_link(self, id: str, include: str) -> LockstepResponse[MagicLinkModel]:
        """
        Retrieves the Magic Link specified by this unique identifier,
        optionally including nested data sets.

        Parameters
        ----------
        id : str
            The id of the Magic Link
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: User
        """
        path = f"/api/v1/useraccounts/magic-links/{id}"
        result = self.client.send_request("GET", path, None, {"include": include}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, MagicLinkModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def revoke_magic_link(self, id: str) -> LockstepResponse[ActionResultModel]:
        """
        Revokes the magic link with the specified id so it cannot be
        used to call the API.

        Revocation will be received by all servers within five minutes
        of revocation. API calls made using this magic link after the
        revocation will fail. A revoked magic link cannot be un-revoked.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of this magic link
        """
        path = f"/api/v1/useraccounts/magic-links/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ActionResultModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_magic_links(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[MagicLinkModel]]:
        """
        Queries Magic Links for this account using the specified
        filtering, sorting, nested fetch, and pagination rules
        requested.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: User
        order : str
            The sort order for the results, in the [Searchlight order
            syntax](https://github.com/tspence/csharp-searchlight).
        pageSize : int
            The page size for results (default 250, maximum of 500)
        pageNumber : int
            The page number for results (default 0)
        """
        path = "/api/v1/useraccounts/magic-links/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), MagicLinkModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
