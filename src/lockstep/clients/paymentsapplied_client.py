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
from lockstep.models.paymentappliedmodel import PaymentAppliedModel

class PaymentsAppliedClient:
    """
    API methods related to PaymentsApplied
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_payment_applied(self, id: str, include: str) -> LockstepResponse[PaymentAppliedModel]:
        """
        Retrieves the Payment Applied specified by this unique
        identifier, optionally including nested data sets.

        A Payment Applied is created by a business who receives a
        Payment from a customer. A customer may make a single Payment to
        match an Invoice exactly, a partial Payment for an Invoice, or a
        single Payment may be made for multiple smaller Invoices. The
        Payment Applied contains information about which Invoices are
        connected to which Payments and for which amounts.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of this Payment
            Applied; NOT the customer's ERP key
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: Invoice,
            Payment
        """
        path = f"/api/v1/payments-applied/{id}"
        result = self.client.send_request("GET", path, None, {"include": include}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, PaymentAppliedModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_payment_applied(self, id: str, body: object) -> LockstepResponse[PaymentAppliedModel]:
        """
        Updates an existing Payment Applied with the information
        supplied to this PATCH call.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. If you do not
        provide the name of a field, that field will remain unchanged.
        This allows you to ensure that you are only updating the
        specific fields desired.

        A Payment Applied is created by a business who receives a
        Payment from a customer. A customer may make a single Payment to
        match an Invoice exactly, a partial Payment for an Invoice, or a
        single Payment may be made for multiple smaller Invoices. The
        Payment Applied contains information about which Invoices are
        connected to which Payments and for which amounts.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Payment
            Applied to update; NOT the customer's ERP key
        body : object
            A list of changes to apply to this Payment Applied
        """
        path = f"/api/v1/payments-applied/{id}"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, PaymentAppliedModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_payment_applied(self, id: str) -> LockstepResponse[ActionResultModel]:
        """
        Deletes the Payment Applied referred to by this unique
        identifier.

        A Payment Applied is created by a business who receives a
        Payment from a customer. A customer may make a single Payment to
        match an Invoice exactly, a partial Payment for an Invoice, or a
        single Payment may be made for multiple smaller Invoices. The
        Payment Applied contains information about which Invoices are
        connected to which Payments and for which amounts.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Payment
            Applied to delete; NOT the customer's ERP key
        """
        path = f"/api/v1/payments-applied/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ActionResultModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_payments_applied(self, body: list[object]) -> LockstepResponse[list[PaymentAppliedModel]]:
        """
        Creates one or more Payments Applied within this account and
        returns the records as created.

        A Payment Applied is created by a business who receives a
        Payment from a customer. A customer may make a single Payment to
        match an Invoice exactly, a partial Payment for an Invoice, or a
        single Payment may be made for multiple smaller Invoices. The
        Payment Applied contains information about which Invoices are
        connected to which Payments and for which amounts.

        Parameters
        ----------
        body : list[object]
            The Payments Applied to create
        """
        path = "/api/v1/payments-applied"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [PaymentAppliedModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_payments_applied(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[PaymentAppliedModel]]:
        """
        Queries Payments Applied for this account using the specified
        filtering, sorting, nested fetch, and pagination rules
        requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        A Payment Applied is created by a business who receives a
        Payment from a customer. A customer may make a single Payment to
        match an Invoice exactly, a partial Payment for an Invoice, or a
        single Payment may be made for multiple smaller Invoices. The
        Payment Applied contains information about which Invoices are
        connected to which Payments and for which amounts.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: Invoice
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
        path = "/api/v1/payments-applied/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), PaymentAppliedModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
