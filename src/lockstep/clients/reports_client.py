#
# Lockstep Platform SDK for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

from lockstep.lockstep_response import LockstepResponse
from lockstep.error_result import ErrorResult
from lockstep.models.agingmodel import AgingModel
from lockstep.models.aragingheaderinfomodel import ArAgingHeaderInfoModel
from lockstep.models.arheaderinfomodel import ArHeaderInfoModel
from lockstep.models.attachmentheaderinfomodel import AttachmentHeaderInfoModel
from lockstep.models.cashflowreportmodel import CashflowReportModel
from lockstep.models.dailysalesoutstandingreportmodel import DailySalesOutstandingReportModel
from lockstep.models.financialreportmodel import FinancialReportModel
from lockstep.models.riskratemodel import RiskRateModel

class ReportsClient:
    """
    API methods related to Reports
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def cash_flow(self, timeframe: int) -> LockstepResponse[CashflowReportModel]:
        """
        Retrieves a current Cash Flow report for this account.

        The Cash Flow report indicates the amount of payments retrieved
        and invoices billed within a given timeframe. You can use this
        report to determine the overall balance of money coming into and
        out of your accounts receivable and accounts payable businesses.

        Parameters
        ----------
        timeframe : int
            Number of days of data to include for the Cash Flow Report
            (default is 30 days from today)
        """
        path = "/api/v1/Reports/cashflow"
        result = self.client.send_request("GET", path, None, {"timeframe": timeframe}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, CashflowReportModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def daily_sales_outstanding(self, ) -> LockstepResponse[list[DailySalesOutstandingReportModel]]:
        """
        Retrieves a current Daily Sales Outstanding (DSO) report for
        this account.

        Daily Sales Outstanding, or DSO, is a metric that indicates the
        average number of days that it takes for an invoice to be fully
        paid. You can use this report to identify whether a company is
        improving on its ability to collect on invoices.

        Parameters
        ----------
        """
        path = "/api/v1/Reports/dailysalesoutstanding"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, list[DailySalesOutstandingReportModel](**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def risk_rates(self, ) -> LockstepResponse[list[RiskRateModel]]:
        """
        Retrieves a current Risk Rate report for this account.

        Risk Rate is a metric that indicates the percentage of total AR
        balance left unpaid after 90 days. You can use this report to
        identify the percentage of invoice value that is not being
        collected in a timely manner.

        Parameters
        ----------
        """
        path = "/api/v1/Reports/riskrates"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, list[RiskRateModel](**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def accounts_receivable_header(self, reportDate: str, companyId: str) -> LockstepResponse[ArHeaderInfoModel]:
        """
        Retrieves AR header information up to the date specified.

        Parameters
        ----------
        reportDate : str
            The date of the report.
        companyId : str
            Include a company to get AR data for a specific company,
            leave as null to include all Companies.
        """
        path = "/api/v1/Reports/ar-header"
        result = self.client.send_request("GET", path, None, {"reportDate": reportDate, "companyId": companyId}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ArHeaderInfoModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def invoice_aging_report(self, CompanyId: str, Recalculate: bool, CurrencyCode: str, CurrencyProvider: str, Buckets: list[int]) -> LockstepResponse[list[AgingModel]]:
        """
        The Aging Report contains information about the total dollar
        value of invoices broken down by their age. Last default or
        specified bucket treated as a catch all bucket for values that
        fit in that bucket or beyond.

        You can specify viewing parameters for the aging report such as
        currency code and date bucket configuration. You can also view
        aging data for an entire account or a specific company.

        This information is recalculated when invoice data changes.
        After each invoice data change occurs, Lockstep queues up a
        calculation based on the current invoice data at that time. This
        information is calculated and persisted for each customer so
        that the report will be available quickly.

        To force a recalculation of aging data, specify the
        `recalculate` option. Note that forcing a recalculation will
        slow your API response time.

        Parameters
        ----------
        CompanyId : str
            Company aging buckets are filtered by (all company aging
            returned if not company specified)
        Recalculate : bool
            Force api to recalculate aging data, cached data may be
            returned when set to false
        CurrencyCode : str
            Currency aging buckets are converted to (all aging data
            returned without currency conversion if no currency is
            specified)
        CurrencyProvider : str
            Currency provider currency rates should be returned from to
            convert aging amounts to (default Lockstep currency provider
            used if no data provider specified)
        Buckets : list[int]
            Customized buckets used for aging calculations (default
            buckets [0,30,60,90,120,180] will be used if buckets not
            specified)
        """
        path = "/api/v1/Reports/aging"
        result = self.client.send_request("GET", path, None, {"CompanyId": CompanyId, "Recalculate": Recalculate, "CurrencyCode": CurrencyCode, "CurrencyProvider": CurrencyProvider, "Buckets": Buckets}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, list[AgingModel](**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def accounts_receivable_aging_header(self, ) -> LockstepResponse[list[ArAgingHeaderInfoModel]]:
        """
        Retrieves AR Aging Header information report broken down by
        aging bucket.

        The AR Aging Header report contains aggregated information about
        the `TotalInvoicesPastDue`, `TotalCustomers`, and their
        respective `PercentageOfTotalAr` grouped by their aging
        `ReportBucket`.

        Parameters
        ----------
        """
        path = "/api/v1/Reports/ar-aging-header"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, list[ArAgingHeaderInfoModel](**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def attachments_header_information(self, companyId: str) -> LockstepResponse[AttachmentHeaderInfoModel]:
        """
        Retrieves Attachment Header information for the requested
        companyId.

        The Attachment Header report contains aggregated information
        about the `TotalAttachments`, `TotalArchived`, and `TotalActive`
        attachment classifications.

        Parameters
        ----------
        companyId : str
            Include a specific company to get Attachment data for, leave
            as null to include all Companies.
        """
        path = "/api/v1/Reports/attachments-header"
        result = self.client.send_request("GET", path, None, {"companyId": companyId}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, AttachmentHeaderInfoModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def trial_balance_report(self, startDate: str, endDate: str) -> LockstepResponse[FinancialReportModel]:
        """
        Generates a Trial Balance Report for the given time range.

        Parameters
        ----------
        startDate : str
            The start date of the report
        endDate : str
            The end date of the report
        """
        path = "/api/v1/Reports/trial-balance"
        result = self.client.send_request("GET", path, None, {"startDate": startDate, "endDate": endDate}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FinancialReportModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def income_statement_report(self, startDate: str, endDate: str, columnOption: str, displayDepth: int, comparisonPeriod: str, showCurrencyDifference: bool, showPercentageDifference: bool) -> LockstepResponse[FinancialReportModel]:
        """
        Generates an Income Statement for the given time range.

        Parameters
        ----------
        startDate : str
            The start date of the report
        endDate : str
            The end date of the report
        columnOption : str
            The desired column splitting of the report data. An empty
            string or anything unrecognized will result in only totals
            being displayed. Options are as follows: By Period - a
            column for every month/fiscal period within the reporting
            dates Quarterly - a column for every quarter within the
            reporting dates Annually - a column for every year within
            the reporting dates
        displayDepth : int
            The desired row splitting of the report data. For Income
            Statements, the minimum report depth is 1. Options are as
            follows: 1 - combine all accounts by their category 2 -
            combine all accounts by their subcategory 3 - display all
            accounts
        comparisonPeriod : str
            Add a column for historical data with the following options
            and use showCurrencyDifference and/or show
            percentageDifference to display a comparison of that
            historical data to the report period. Options are as follows
            (note for YTD the data will be compared as a percentage of
            YTD and showCurrencyDifference and showPercentageDifference
            should not be used): "PP" - previous period (will show the
            previous quarter or year if Quarterly or Annually is chosen
            for columnOption) "PY" - previous year (the same date range
            as the report, but for the year prior) "YTD" - year to date
            (the current financial year to the current period)
        showCurrencyDifference : bool
            A boolean to turn on a currency based difference between the
            reporting period and the comparison period.
        showPercentageDifference : bool
            A boolean to turn on a percent based difference between the
            reporting period and the comparison period.
        """
        path = "/api/v1/Reports/income-statement"
        result = self.client.send_request("GET", path, None, {"startDate": startDate, "endDate": endDate, "columnOption": columnOption, "displayDepth": displayDepth, "comparisonPeriod": comparisonPeriod, "showCurrencyDifference": showCurrencyDifference, "showPercentageDifference": showPercentageDifference}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FinancialReportModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def balance_sheet_report(self, startDate: str, endDate: str, columnOption: str, displayDepth: int, comparisonPeriod: str, showCurrencyDifference: bool, showPercentageDifference: bool) -> LockstepResponse[FinancialReportModel]:
        """
        Generates a balance sheet for the given time range.

        Parameters
        ----------
        startDate : str
            The start date of the report
        endDate : str
            The end date of the report
        columnOption : str
            The desired column splitting of the report data. An empty
            string or anything unrecognized will result in only totals
            being displayed. Options are as follows: By Period - a
            column for every month/fiscal period within the reporting
            dates Quarterly - a column for every quarter within the
            reporting dates Annually - a column for every year within
            the reporting dates
        displayDepth : int
            The desired row splitting of the report data. For Balance
            Sheets, the minimum report depth is 1. Options are as
            follows: 1 - combine all accounts by their category 2 -
            combine all accounts by their subcategory 3 - display all
            accounts
        comparisonPeriod : str
            Add a column for historical data with the following options
            and use showCurrencyDifference and/or show
            percentageDifference to display a comparison of that
            historical data to the report period. "PP" - previous period
            (will show the previous quarter or year if Quarterly or
            Annually is chosen for columnOption) "PY" - previous year
            (the same date range as the report, but for the year prior)
        showCurrencyDifference : bool
            A boolean to turn on a currency based difference between the
            reporting period and the comparison period.
        showPercentageDifference : bool
            A boolean to turn on a percent based difference between the
            reporting period and the comparison period.
        """
        path = "/api/v1/Reports/balance-sheet"
        result = self.client.send_request("GET", path, None, {"startDate": startDate, "endDate": endDate, "columnOption": columnOption, "displayDepth": displayDepth, "comparisonPeriod": comparisonPeriod, "showCurrencyDifference": showCurrencyDifference, "showPercentageDifference": showPercentageDifference}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FinancialReportModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))
