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
from lockstep.models.bulkdeleterequestmodel import BulkDeleteRequestModel
from lockstep.models.contactmodel import ContactModel
from lockstep.models.deleteresult import DeleteResult

class ContactsClient:
    """
    API methods related to Contacts
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_contact(self, id: str, include: str) -> LockstepResponse[ContactModel]:
        """
        Retrieves the Contact specified by this unique identifier,
        optionally including nested data sets.

        A Contact contains information about a person or role within a
        Company. You can use Contacts to track information about who is
        responsible for a specific project, who handles invoices, or
        information about which role at a particular customer or vendor
        you should speak with about invoices.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of this Contact; NOT
            the customer's ERP key
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: Attachments,
            CustomFields, Notes
        """
        path = f"/api/v1/Contacts/{id}"
        result = self.client.send_request("GET", path, None, {"include": include}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ContactModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_contact(self, id: str, body: object) -> LockstepResponse[ContactModel]:
        """
        Updates a contact that matches the specified id with the
        requested information.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. If you do not
        provide the name of a field, that field will remain unchanged.
        This allows you to ensure that you are only updating the
        specific fields desired.

        A Contact contains information about a person or role within a
        Company. You can use Contacts to track information about who is
        responsible for a specific project, who handles invoices, or
        information about which role at a particular customer or vendor
        you should speak with about invoices.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Contact to
            update; NOT the customer's ERP key
        body : object
            A list of changes to apply to this Contact
        """
        path = f"/api/v1/Contacts/{id}"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ContactModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_contact(self, id: str) -> LockstepResponse[DeleteResult]:
        """
        Delete the Contact referred to by this unique identifier.

        A Contact contains information about a person or role within a
        Company. You can use Contacts to track information about who is
        responsible for a specific project, who handles invoices, or
        information about which role at a particular customer or vendor
        you should speak with about invoices.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Contact to
            delete; NOT the customer's ERP key
        """
        path = f"/api/v1/Contacts/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, DeleteResult(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_contacts(self, body: list[object]) -> LockstepResponse[list[ContactModel]]:
        """
        Creates one or more contacts from a given model.

        A Contact contains information about a person or role within a
        Company. You can use Contacts to track information about who is
        responsible for a specific project, who handles invoices, or
        information about which role at a particular customer or vendor
        you should speak with about invoices.

        Parameters
        ----------
        body : list[object]
            The Contacts to create
        """
        path = "/api/v1/Contacts"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [ContactModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_contacts(self, body: BulkDeleteRequestModel) -> LockstepResponse[DeleteResult]:
        """
        Delete the Contacts referred to by these unique identifiers.

        A Contact contains information about a person or role within a
        Company. You can use Contacts to track information about who is
        responsible for a specific project, who handles invoices, or
        information about which role at a particular customer or vendor
        you should speak with about invoices.

        Parameters
        ----------
        body : BulkDeleteRequestModel
            The unique Lockstep Platform ID numbers of the Contacts to
            delete; NOT the customer's ERP keys
        """
        path = "/api/v1/Contacts"
        result = self.client.send_request("DELETE", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, DeleteResult(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_contacts(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[ContactModel]]:
        """
        Queries Contacts for this account using the specified filtering,
        sorting, nested fetch, and pagination rules requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

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
        path = "/api/v1/Contacts/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), ContactModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
