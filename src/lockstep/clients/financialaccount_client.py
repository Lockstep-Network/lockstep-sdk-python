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
from lockstep.models.financialaccountmodel import FinancialAccountModel

class FinancialAccountClient:
    """
    API methods related to FinancialAccount
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def create_financial_account(self, body: list[object]) -> LockstepResponse[FinancialAccountModel]:
        """
        Creates a financial account with the specified name.

        Parameters
        ----------
        body : list[object]
            Metadata about the financial account to create.
        """
        path = "/api/v1/FinancialAccount"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FinancialAccountModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def retrieve_financial_account(self, id: str) -> LockstepResponse[FinancialAccountModel]:
        """
        Retrieves the financial account specified by this unique
        identifier.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of this Account; NOT
            the customer's ERP key
        """
        path = f"/api/v1/FinancialAccount/{id}"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FinancialAccountModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_financial_account(self, id: str, body: object) -> LockstepResponse[FinancialAccountModel]:
        """


        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Account to
            update; NOT the customer's ERP key
        body : object
            A list of changes to apply to this Account
        """
        path = f"/api/v1/FinancialAccount/{id}"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FinancialAccountModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_financial_account(self, id: str) -> LockstepResponse[ActionResultModel]:
        """
        Deletes the Financial Account referred to by this unique
        identifier.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Financial
            Account to disable; NOT the customer's ERP key
        """
        path = f"/api/v1/FinancialAccount/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ActionResultModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_financial_accounts(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[FinancialAccountModel]]:
        """


        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve.
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
        path = "/api/v1/FinancialAccount/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), FinancialAccountModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
