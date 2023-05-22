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
from lockstep.models.deleteresult import DeleteResult
from lockstep.models.invoicelinemodel import InvoiceLineModel

class InvoiceLinesClient:
    """
    API methods related to InvoiceLines
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def create_invoiceline(self, body: list[object]) -> LockstepResponse[list[InvoiceLineModel]]:
        """
        Creates one or more invoice lines within this account and
        returns the created records

        Parameters
        ----------
        body : list[object]

        """
        path = "/api/v1/invoice-lines"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [InvoiceLineModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_invoice_lines(self, body: BulkDeleteRequestModel) -> LockstepResponse[DeleteResult]:
        """


        Parameters
        ----------
        body : BulkDeleteRequestModel
            The unique Lockstep Platform ID numbers of the Invoice Lines
            to delete; NOT the customer's ERP keys
        """
        path = "/api/v1/invoice-lines"
        result = self.client.send_request("DELETE", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, DeleteResult(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def retrieves_invoice_line(self, invoiceLineId: str) -> LockstepResponse[InvoiceLineModel]:
        """


        Parameters
        ----------
        invoiceLineId : str
            Unique id of the the InvoiceLine
        """
        path = f"/api/v1/invoice-lines/{invoiceLineId}"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, InvoiceLineModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_invoice_line(self, invoiceLineId: str, body: object) -> LockstepResponse[InvoiceLineModel]:
        """
        Updates an existing Invoice Line with the information supplied
        to this PATCH call.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. If you do not
        provide the name of a field, that field will remain unchanged.
        This allows you to ensure that you are only updating the
        specific fields desired.

        Parameters
        ----------
        invoiceLineId : str
            Unique id of the the InvoiceLine
        body : object
            A list of changes to apply to this Invoice Line
        """
        path = f"/api/v1/invoice-lines/{invoiceLineId}"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, InvoiceLineModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def deletes_invoice_line(self, invoiceLineId: str) -> LockstepResponse[DeleteResult]:
        """


        Parameters
        ----------
        invoiceLineId : str
            Unique id of the the InvoiceLine
        """
        path = f"/api/v1/invoice-lines/{invoiceLineId}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, DeleteResult(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_invoice_lines(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[InvoiceLineModel]]:
        """
        Queries Invoice Lines for the account using specified filtering
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
            elements to retrieve.
        order : str
            The sort order for the results, in the [Searchlight order
            syntax]
        pageSize : int
            The page size for results (default 200, maximum of 10,000)
        pageNumber : int
            The page number for results (default 0)
        """
        path = "/api/v1/invoice-lines/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), InvoiceLineModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
