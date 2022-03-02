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
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

from lockstep.lockstep_response import LockstepResponse
from lockstep.models.financialaccountmodel import FinancialAccountModel

class FinancialAccountClient:

    def __init__(self, client):
        self.client = client

    def create_financial_account(self, body: list[FinancialAccountModel]) -> LockstepResponse:
        """
        Creates a financial account with the specified name.

        Parameters
        ----------
        body : list[FinancialAccountModel]
            Metadata about the financial account to create.
        """
        path = f"/api/v1/FinancialAccount"
        return self.client.send_request("POST", path, body, {"body": body})

    def retrieve_financial_account(self, id: str) -> LockstepResponse:
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
        return self.client.send_request("GET", path, None, {"id": id})

    def update_financial_account(self, id: str, body: object) -> LockstepResponse:
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
        return self.client.send_request("PATCH", path, body, {"id": id, "body": body})

    def deletes_financial_account(self, id: str) -> LockstepResponse:
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
        return self.client.send_request("DELETE", path, None, {"id": id})

    def query_financial_accounts(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
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
            The page size for results (default 200). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        """
        path = f"/api/v1/FinancialAccount/query"
        return self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber})
