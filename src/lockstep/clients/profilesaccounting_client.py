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
from lockstep.models.accountingprofilemodel import AccountingProfileModel
from lockstep.models.accountingprofilerequest import AccountingProfileRequest
from lockstep.models.actionresultmodel import ActionResultModel

class ProfilesAccountingClient:
    """
    API methods related to ProfilesAccounting
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_accounting_profile(self, id: str, include: str) -> LockstepResponse[AccountingProfileModel]:
        """
        Retrieves the Accounting Profile specified by this unique
        identifier, optionally including nested data sets.

        An Accounting Profile is a child of a Company Profile, and
        collectively, they comprise the identity and necessary
        information for an accounting team to work with trading
        partners, financial institutions, auditors, and others. You can
        use Accounting Profiles to define an accounting function by what
        the function does and how to interface with the function.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of this Accounting
            Profile
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: Attachments,
            CustomFields, Notes
        """
        path = f"/api/v1/profiles/accounting/{id}"
        result = self.client.send_request("GET", path, None, {"include": include}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, AccountingProfileModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_accounting_profile(self, id: str, body: object) -> LockstepResponse[AccountingProfileModel]:
        """
        Updates an accounting profile that matches the specified id with
        the requested information.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. If you do not
        provide the name of a field, that field will remain unchanged.
        This allows you to ensure that you are only updating the
        specific fields desired.

        An Accounting Profile is a child of a Company Profile, and
        collectively, they comprise the identity and necessary
        information for an accounting team to work with trading
        partners, financial institutions, auditors, and others. You can
        use Accounting Profiles to define an accounting function by what
        the function does and how to interface with the function.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Accounting
            Profile to update
        body : object
            A list of changes to apply to this Accounting Profile
        """
        path = f"/api/v1/profiles/accounting/{id}"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, AccountingProfileModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_accounting_profile(self, id: str) -> LockstepResponse[ActionResultModel]:
        """
        Delete the Accounting Profile referred to by this unique
        identifier.

        An Accounting Profile is a child of a Company Profile, and
        collectively, they comprise the identity and necessary
        information for an accounting team to work with trading
        partners, financial institutions, auditors, and others. You can
        use Accounting Profiles to define an accounting function by what
        the function does and how to interface with the function.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Accounting
            Profile to disable
        """
        path = f"/api/v1/profiles/accounting/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ActionResultModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_accounting_profiles(self, body: list[object]) -> LockstepResponse[list[AccountingProfileModel]]:
        """
        Creates one or more accounting profiles from a given model.

        An Accounting Profile is a child of a Company Profile, and
        collectively, they comprise the identity and necessary
        information for an accounting team to work with trading
        partners, financial institutions, auditors, and others. You can
        use Accounting Profiles to define an accounting function by what
        the function does and how to interface with the function.

        Parameters
        ----------
        body : list[object]
            The Accounting Profiles to create
        """
        path = "/api/v1/profiles/accounting"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [AccountingProfileModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_accounting_profiles(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[AccountingProfileModel]]:
        """
        Queries Accounting Profiles for this account using the specified
        filtering, sorting, nested fetch, and pagination rules
        requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        An Accounting Profile is a child of a Company Profile, and
        collectively, they comprise the identity and necessary
        information for an accounting team to work with trading
        partners, financial institutions, auditors, and others. You can
        use Accounting Profiles to define an accounting function by what
        the function does and how to interface with the function.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: Attachments,
            CustomFields, Notes
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
        path = "/api/v1/profiles/accounting/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), AccountingProfileModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
