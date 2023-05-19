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
from lockstep.models.invoiceaddressmodel import InvoiceAddressModel

class InvoiceAddressesClient:
    """
    API methods related to InvoiceAddresses
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_invoice_address(self, id: str, include: str) -> LockstepResponse[InvoiceAddressModel]:
        """
        Retrieves the invoice address specified by this unique
        identifier, optionally including nested data sets.

        An Invoice Address contains address information about an
        invoice. You can use Invoice Addresses to track information
        about locations important to an invoice such as: where a
        company's goods are shipped from, where a company's goods are
        shipped to or billing addresses to name a few.

        Parameters
        ----------
        id : str
            The unique ID number of this invoice address
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve.
        """
        path = f"/api/v1/invoice-addresses/{id}"
        result = self.client.send_request("GET", path, None, {"include": include}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, InvoiceAddressModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_invoice_address(self, id: str) -> LockstepResponse[ActionResultModel]:
        """
        Deletes the Invoice Address by this unique identifier.

        An Invoice Address contains address information about an
        invoice. You can use Invoice Addresses to track information
        about locations important to an invoice such as: where a
        company's goods are shipped from, where a company's goods are
        shipped to or billing addresses to name a few.

        Parameters
        ----------
        id : str
            The unique ID of the Invoice Address to delete
        """
        path = f"/api/v1/invoice-addresses/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ActionResultModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_invoice_address(self, id: str, body: object) -> LockstepResponse[InvoiceAddressModel]:
        """
        Updates an existing Invoice Address with the information
        supplied to this PATCH call.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. If you do not
        provide the name of a field, that field will remain unchanged.
        This allows you to ensure that you are only updating the
        specific fields desired.

        An Invoice Address contains address information about an
        invoice. You can use Invoice Addresses to track information
        about locations important to an invoice such as: where a
        company's goods are shipped from, where a company's goods are
        shipped to or billing addresses to name a few.

        Parameters
        ----------
        id : str
            The unique ID number of the Invoice Address to update
        body : object
            A list of changes to apply to this Invoice Address
        """
        path = f"/api/v1/invoice-addresses/{id}"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, InvoiceAddressModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_invoice_address(self, body: list[object]) -> LockstepResponse[list[InvoiceAddressModel]]:
        """
        Creates one or more Invoice Addresses within this account and
        returns the records as created.

        An Invoice Address contains address information about an
        invoice. You can use Invoice Addresses to track information
        about locations important to an invoice such as: where a
        company's goods are shipped from, where a company's goods are
        shipped to or billing addresses to name a few.

        Parameters
        ----------
        body : list[object]
            The Invoice Address to create
        """
        path = "/api/v1/invoice-addresses"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [InvoiceAddressModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_invoice_addresses(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[InvoiceAddressModel]]:
        """
        Queries Invoice Addresses for this account using the specified
        filtering, sorting, nested fetch, and pagination rules
        requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. No collections are currently available
            but may be offered in the future
        order : str
            The sort order for this query. See See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageSize : int
            The page size for results (default 200). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        """
        path = "/api/v1/invoice-addresses/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), InvoiceAddressModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
