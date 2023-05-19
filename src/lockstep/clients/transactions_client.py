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
from lockstep.models.transactiondetailmodel import TransactionDetailModel
from lockstep.models.transactionmodeltransactionsummarytotalmodelsummaryfetchresult import TransactionModelTransactionSummaryTotalModelSummaryFetchResult

class TransactionsClient:
    """
    API methods related to Transactions
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def query_transactions(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int, currentDate: str) -> LockstepResponse[TransactionModelTransactionSummaryTotalModelSummaryFetchResult]:
        """
        Queries transactions (invoices/credit memos/payments) for this
        account using the specified filtering, sorting, nested fetch,
        and pagination rules requested.

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
            The sort order for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageSize : int
            The page size for results (default 250, maximum of 500). See
            [Searchlight Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        currentDate : str
            The date the days past due value will be calculated against.
            If no currentDate is provided the current UTC date will be
            used.
        """
        path = "/api/v1/Transactions/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber, "currentDate": currentDate}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, TransactionModelTransactionSummaryTotalModelSummaryFetchResult(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def retrieve_transaction_details(self, id: str) -> LockstepResponse[list[TransactionDetailModel]]:
        """
        Retrieves a list of transaction details for the supplied
        transaction id.

        A Transaction Detail contains information about the associated
        Transaction. This information can be an invoice associated to a
        payment or credit memo or a payment or credit memo used as
        payment for one or more invoices.

        Parameters
        ----------
        id : str

        """
        path = f"/api/v1/Transactions/{id}/details"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [TransactionDetailModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
