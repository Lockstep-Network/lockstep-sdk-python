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
from lockstep.models.accountingprofilecontactmodel import AccountingProfileContactModel
from lockstep.models.accountingprofilecontactresultmodel import AccountingProfileContactResultModel
from lockstep.models.deleteresult import DeleteResult

class ProfilesAccountingContactsClient:
    """
    API methods related to ProfilesAccountingContacts
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_accounting_profile_contact(self, id: str) -> LockstepResponse[AccountingProfileContactModel]:
        """
        Retrieves the Accounting Profile Contact specified by this
        unique identifier, optionally including nested data sets.

        A Contact has a link to a Contact that is associated with your
        company's Accounting Profile. A profile has one primary contact
        and any number of secondary contacts.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of this Accounting
            Profile Contact
        """
        path = f"/api/v1/profiles/accounting/contacts/{id}"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, AccountingProfileContactModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_accounting_profile_contact(self, id: str) -> LockstepResponse[DeleteResult]:
        """
        Delete the Accounting Profile Contact referred to by this unique
        identifier.

        An Accounting Profile Contact has a link to a Contact that is
        associated with your company's Accounting Profile. A profile has
        one primary contact and any number of secondary contacts.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Accounting
            Profile Contact to delete
        """
        path = f"/api/v1/profiles/accounting/contacts/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, DeleteResult(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_accounting_profile_contacts(self, body: list[object]) -> LockstepResponse[list[AccountingProfileContactModel]]:
        """
        Creates one or more Accounting Profile Contacts from a given
        model.

        An Accounting Profile Contact has a link to a Contact that is
        associated with your company's Accounting Profile. A profile has
        one primary contact and any number of secondary contacts.

        Parameters
        ----------
        body : list[object]
            The Accounting Profile Contacts to create
        """
        path = "/api/v1/profiles/accounting/contacts"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [AccountingProfileContactModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_accounting_profile_contacts(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[AccountingProfileContactModel]]:
        """
        Queries Accounting Profile Contacts for this account using the
        specified filtering, sorting, nested fetch, and pagination rules
        requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        An Accounting Profile Contact has a link to a Contact that is
        associated with your company's Accounting Profile. A profile has
        one primary contact and any number of secondary contacts.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: None
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
        path = "/api/v1/profiles/accounting/contacts/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), AccountingProfileContactModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_linked_accounting_profile_contacts(self, filter: str, order: str, include: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[AccountingProfileContactResultModel]]:
        """
        Queries Accounting Profile Contacts and Contacts for this
        account using the specified filtering, sorting, nested fetch,
        and pagination rules requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        An Accounting Profile Contact has a link to a Contact that is
        associated with your company's Accounting Profile. A profile has
        one primary contact and any number of secondary contacts.

        A Contact contains information about a person or role within a
        Company. You can use Contacts to track information about who is
        responsible for a specific project, who handles invoices, or
        information about which role at a particular customer or vendor
        you should speak with about invoices.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        order : str
            The sort order for this query. See See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: None
        pageSize : int
            The page size for results (default 250, maximum of 500). See
            [Searchlight Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        """
        path = "/api/v1/profiles/accounting/contacts/query/models"
        result = self.client.send_request("GET", path, None, {"filter": filter, "order": order, "include": include, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), AccountingProfileContactResultModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def set_secondary_contact_as_primary(self, id: str) -> LockstepResponse[AccountingProfileContactModel]:
        """
        Reverses the isPrimary fields on the primary and secondary
        contact to reflect a swap and returns the new primary accounting
        profile contact model.

        An Accounting Profile Contact has a link to a Contact that is
        associated with your company's Accounting Profile. A profile has
        one primary contact and any number of secondary contacts.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Accounting
            Profile Contact to set as primary
        """
        path = f"/api/v1/profiles/accounting/contacts/{id}/primary"
        result = self.client.send_request("PATCH", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, AccountingProfileContactModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
