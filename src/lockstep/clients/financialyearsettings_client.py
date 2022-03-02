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
from lockstep.models.financialyearsettingmodel import FinancialYearSettingModel

class FinancialYearSettingsClient:

    def __init__(self, client):
        self.client = client

    def retrieve_financial_year_setting(self, id: str) -> LockstepResponse:
        """
        Retrieves the Financial Year Setting specified by this unique
        identifier.

        A Financial Year Setting is used to to set the type, beginning,
        end, and number of periods of a year used to calculate
        accounting reports. The financial setting can either be for a
        specific app enrollment id via a sync or, when the financial
        year setting is manually created, will cover all account data
        without an app enrollment id.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of this Financial
            Year Setting
        """
        path = f"/api/v1/FinancialYearSettings/{id}"
        return self.client.send_request("GET", path, None, {"id": id})

    def update_financial_year_setting(self, id: str, body: object) -> LockstepResponse:
        """
        Updates a financial year setting that matches the specified id
        with the requested information.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. If you do not
        provide the name of a field, that field will remain unchanged.
        This allows you to ensure that you are only updating the
        specific fields desired.

        A Financial Year Setting is used to to set the type, beginning,
        end, and number of periods of a year used to calculate
        accounting reports. The financial setting can either be for a
        specific app enrollment id via a sync or, when the financial
        year setting is manually created, will cover all account data
        without an app enrollment id.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Financial Year
            Setting to update
        body : object
            A list of changes to apply to this Financial Year Setting
        """
        path = f"/api/v1/FinancialYearSettings/{id}"
        return self.client.send_request("PATCH", path, body, {"id": id, "body": body})

    def delete_financial_year_setting(self, id: str) -> LockstepResponse:
        """
        Delete the Financial Year Setting referred to by this unique
        identifier.

        A Financial Year Setting is used to to set the type, beginning,
        end, and number of periods of a year used to calculate
        accounting reports. The financial setting can either be for a
        specific app enrollment id via a sync or, when the financial
        year setting is manually created, will cover all account data
        without an app enrollment id.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Financial Year
            Setting to disable
        """
        path = f"/api/v1/FinancialYearSettings/{id}"
        return self.client.send_request("DELETE", path, None, {"id": id})

    def create_financial_year_setting(self, body: FinancialYearSettingModel) -> LockstepResponse:
        """
        Creates a financial year setting from a given model.

        A Financial Year Setting is used to to set the type, beginning,
        end, and number of periods of a year used to calculate
        accounting reports. The financial setting can either be for a
        specific app enrollment id via a sync or, when the financial
        year setting is manually created, will cover all account data
        without an app enrollment id.

        Parameters
        ----------
        body : FinancialYearSettingModel
            The Financial Year Setting to create
        """
        path = f"/api/v1/FinancialYearSettings"
        return self.client.send_request("POST", path, body, {"body": body})

    def query_financial_year_settings(self, filter: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        """
        Queries Financial Year Settings for this account using the
        specified filtering, sorting, and pagination rules requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        A Financial Year Setting is used to to set the type, beginning,
        end, and number of periods of a year used to calculate
        accounting reports. The financial setting can either be for a
        specific app enrollment id via a sync or, when the financial
        year setting is manually created, will cover all account data
        without an app enrollment id.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
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
        path = f"/api/v1/FinancialYearSettings/query"
        return self.client.send_request("GET", path, None, {"filter": filter, "order": order, "pageSize": pageSize, "pageNumber": pageNumber})
