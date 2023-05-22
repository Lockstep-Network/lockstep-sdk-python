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
from lockstep.models.financialyearsettingmodel import FinancialYearSettingModel

class FinancialYearSettingsClient:
    """
    API methods related to FinancialYearSettings
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_financial_year_setting(self, id: str) -> LockstepResponse[FinancialYearSettingModel]:
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
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FinancialYearSettingModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_financial_year_setting(self, id: str, body: object) -> LockstepResponse[FinancialYearSettingModel]:
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
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FinancialYearSettingModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_financial_year_setting(self, id: str) -> LockstepResponse[ActionResultModel]:
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
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ActionResultModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_financial_year_setting(self, body: FinancialYearSettingModel) -> LockstepResponse[FinancialYearSettingModel]:
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
        path = "/api/v1/FinancialYearSettings"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FinancialYearSettingModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_financial_year_settings(self, filter: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[FinancialYearSettingModel]]:
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
            The page size for results (default 250, maximum of 500). See
            [Searchlight Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        """
        path = "/api/v1/FinancialYearSettings/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), FinancialYearSettingModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
