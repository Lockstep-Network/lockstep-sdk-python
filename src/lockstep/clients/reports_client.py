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
from lockstep.models.agingmodel import AgingModel
from lockstep.models.apagingheaderinfomodel import ApAgingHeaderInfoModel
from lockstep.models.apheaderinfomodel import ApHeaderInfoModel
from lockstep.models.aragingheaderinfomodel import ArAgingHeaderInfoModel
from lockstep.models.arheaderinfomodel import ArHeaderInfoModel
from lockstep.models.attachmentheaderinfomodel import AttachmentHeaderInfoModel
from lockstep.models.cashflowreportmodel import CashflowReportModel
from lockstep.models.dailypayableoutstandingreportmodel import DailyPayableOutstandingReportModel
from lockstep.models.dailysalesoutstandingreportmodel import DailySalesOutstandingReportModel
from lockstep.models.dposummarygrouptotalmodel import DpoSummaryGroupTotalModel
from lockstep.models.dposummarymodel import DpoSummaryModel
from lockstep.models.financialreportmodel import FinancialReportModel
from lockstep.models.payablescomingdueheadermodel import PayablesComingDueHeaderModel
from lockstep.models.payablescomingduemodel import PayablesComingDueModel
from lockstep.models.payablescomingduewidgetmodel import PayablesComingDueWidgetModel
from lockstep.models.payablessummaryreportmodel import PayablesSummaryReportModel
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
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def payables_summary_report(self, timeframe: int) -> LockstepResponse[PayablesSummaryReportModel]:
        """
        Retrieves a current Payables Summary report for this account.

        The Payables Summary report indicates the amount of payments
        sent and bills received within a given timeframe. You can use
        this report to determine the overall balance of money coming
        into and out of your accounts receivable and accounts payable
        businesses.

        Parameters
        ----------
        timeframe : int
            Number of days of data to include for the Payables Summary
            Report (default is 30 days from today)
        """
        path = "/api/v1/Reports/payables-summary"
        result = self.client.send_request("GET", path, None, {"timeframe": timeframe}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, PayablesSummaryReportModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def daily_sales_outstanding(self, reportDate: str) -> LockstepResponse[list[DailySalesOutstandingReportModel]]:
        """
        Retrieves a current Daily Sales Outstanding (DSO) report for
        this account.

        Daily Sales Outstanding, or DSO, is a metric that indicates the
        average number of days that it takes for an invoice to be fully
        paid. You can use this report to identify whether a company is
        improving on its ability to collect on invoices.

        Parameters
        ----------
        reportDate : str
            Optional: Specify the specific report date to generate the
            from (default UTC now)
        """
        path = "/api/v1/Reports/daily-sales-outstanding"
        result = self.client.send_request("GET", path, None, {"reportDate": reportDate}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [DailySalesOutstandingReportModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def days_payable_outstanding(self, ) -> LockstepResponse[list[DailyPayableOutstandingReportModel]]:
        """
        Retrieves a current Days Payable Outstanding (DPO) report for
        this account.

        Days payable outstanding (DPO) is a financial ratio that
        indicates the average time (in days) that a company takes to pay
        its bills to its trade creditors, which may include suppliers,
        vendors, or financiers.

        Parameters
        ----------
        """
        path = "/api/v1/Reports/daily-payable-outstanding"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [DailyPayableOutstandingReportModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def payables_coming_due(self, ) -> LockstepResponse[list[PayablesComingDueWidgetModel]]:
        """
        Retrieves payable amount due for 4 time buckets (Today, 7 Days
        from Today, 14 Days from Today, and 30 Days from Today).

        Parameters
        ----------
        """
        path = "/api/v1/Reports/payables-coming-due"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [PayablesComingDueWidgetModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def payables_coming_due_summary(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[PayablesComingDueModel]]:
        """
        Payables coming due represents the amount of cash required to
        pay vendor bills based on the due dates of the bills. Each
        bucket represents total amount due within the time period based
        on open Payables as of today.

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
            The sort order for the results, in the [Searchlight order
            syntax](https://github.com/tspence/csharp-searchlight).
        pageSize : int
            The page size for results (default 250, maximum of 500)
        pageNumber : int
            The page number for results (default 0)
        """
        path = "/api/v1/Reports/payables-coming-due-summary"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), PayablesComingDueModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def payables_coming_due_header(self, reportDate: str) -> LockstepResponse[list[PayablesComingDueHeaderModel]]:
        """
        Retrieves total number of vendors, bills, the total amount
        outstanding, for a group.

        Parameters
        ----------
        reportDate : str
            The date the outstanding values are calculated on. Should be
            either the current day, 7 days after the current day, 14
            days after the current day, or 30 days after the current
            day.
        """
        path = "/api/v1/Reports/payables-coming-due-header"
        result = self.client.send_request("GET", path, None, {"reportDate": reportDate}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [PayablesComingDueHeaderModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

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
        path = "/api/v1/Reports/risk-rates"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [RiskRateModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

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
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def accounts_payable_header(self, reportDate: str, companyId: str) -> LockstepResponse[ApHeaderInfoModel]:
        """
        Retrieves AP header information up to the date specified.

        Parameters
        ----------
        reportDate : str
            The date of the report.
        companyId : str
            Include a company to get AP data for a specific company,
            leave as null to include all Companies.
        """
        path = "/api/v1/Reports/ap-header"
        result = self.client.send_request("GET", path, None, {"reportDate": reportDate, "companyId": companyId}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ApHeaderInfoModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def invoice_aging_report(self, CompanyId: str, Recalculate: bool, CurrencyCode: str, CurrencyProvider: str, Buckets: list[object], ApReport: bool) -> LockstepResponse[list[AgingModel]]:
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
        Buckets : list[object]
            Customized buckets used for aging calculations (default
            buckets [0,30,60,90,120,180] will be used if buckets not
            specified)
        ApReport : bool
            A boolean to turn on AP Aging reports
        """
        path = "/api/v1/Reports/aging"
        result = self.client.send_request("GET", path, None, {"CompanyId": CompanyId, "Recalculate": Recalculate, "CurrencyCode": CurrencyCode, "CurrencyProvider": CurrencyProvider, "Buckets": Buckets, "ApReport": ApReport}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [AgingModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

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
            return LockstepResponse(True, result.status_code, [ArAgingHeaderInfoModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def accounts_payable_aging_header(self, ) -> LockstepResponse[list[ApAgingHeaderInfoModel]]:
        """
        Retrieves AP Aging Header information report broken down by
        aging bucket.

        The AP Aging Header report contains aggregated information about
        the `TotalBillsPastDue`, `TotalVendors`, and their respective
        `PercentageOfTotalAp` grouped by their aging `ReportBucket`.

        Parameters
        ----------
        """
        path = "/api/v1/Reports/ap-aging-header"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [ApAgingHeaderInfoModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

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
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def trial_balance_report(self, startDate: str, endDate: str, appEnrollmentId: str) -> LockstepResponse[FinancialReportModel]:
        """
        Generates a Trial Balance Report for the given time range.

        Parameters
        ----------
        startDate : str
            The start date of the report
        endDate : str
            The end date of the report
        appEnrollmentId : str
            The app enrollment id of the app enrollment whose data will
            be used.
        """
        path = "/api/v1/Reports/trial-balance"
        result = self.client.send_request("GET", path, None, {"startDate": startDate, "endDate": endDate, "appEnrollmentId": appEnrollmentId}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FinancialReportModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def income_statement_report(self, startDate: str, endDate: str, appEnrollmentId: str, columnOption: str, displayDepth: int, comparisonPeriod: str, showCurrencyDifference: bool, showPercentageDifference: bool) -> LockstepResponse[FinancialReportModel]:
        """
        Generates an Income Statement for the given time range.

        Parameters
        ----------
        startDate : str
            The start date of the report
        endDate : str
            The end date of the report
        appEnrollmentId : str
            The app enrollment id of the app enrollment whose data will
            be used.
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
        result = self.client.send_request("GET", path, None, {"startDate": startDate, "endDate": endDate, "appEnrollmentId": appEnrollmentId, "columnOption": columnOption, "displayDepth": displayDepth, "comparisonPeriod": comparisonPeriod, "showCurrencyDifference": showCurrencyDifference, "showPercentageDifference": showPercentageDifference}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FinancialReportModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def balance_sheet_report(self, startDate: str, endDate: str, appEnrollmentId: str, columnOption: str, displayDepth: int, comparisonPeriod: str, showCurrencyDifference: bool, showPercentageDifference: bool) -> LockstepResponse[FinancialReportModel]:
        """
        Generates a balance sheet for the given time range.

        Parameters
        ----------
        startDate : str
            The start date of the report
        endDate : str
            The end date of the report
        appEnrollmentId : str
            The app enrollment id of the app enrollment whose data will
            be used.
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
        result = self.client.send_request("GET", path, None, {"startDate": startDate, "endDate": endDate, "appEnrollmentId": appEnrollmentId, "columnOption": columnOption, "displayDepth": displayDepth, "comparisonPeriod": comparisonPeriod, "showCurrencyDifference": showCurrencyDifference, "showPercentageDifference": showPercentageDifference}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FinancialReportModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def cash_flow_statement_report(self, startDate: str, endDate: str, appEnrollmentId: str, columnOption: str, displayDepth: int) -> LockstepResponse[FinancialReportModel]:
        """
        Generates a cash flow statement for the given time range.

        Parameters
        ----------
        startDate : str
            The start date of the report
        endDate : str
            The end date of the report
        appEnrollmentId : str
            The app enrollment id of the app enrollment whose data will
            be used.
        columnOption : str
            The desired column splitting of the report data. An empty
            string or anything unrecognized will result in only totals
            being displayed. Options are as follows: By Period - a
            column for every month/fiscal period within the reporting
            dates Quarterly - a column for every quarter within the
            reporting dates Annually - a column for every year within
            the reporting dates
        displayDepth : int
            The desired row splitting of the report data. Options are as
            follows: 0 - combine all accounts by their classification 1
            - combine all accounts by their category 2 - combine all
            accounts by their subcategory 3 - display all accounts
        """
        path = "/api/v1/Reports/cash-flow-statement"
        result = self.client.send_request("GET", path, None, {"startDate": startDate, "endDate": endDate, "appEnrollmentId": appEnrollmentId, "columnOption": columnOption, "displayDepth": displayDepth}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FinancialReportModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def days_payable_outstanding_summary(self, reportDate: str, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[DpoSummaryModel]]:
        """
        Retrieves a summary for each vendor that includes a count of
        their outstanding bills, the total amount outstanding, and their
        daily payable outstanding value.

        Days payable outstanding (DPO) is a financial ratio that
        indicates the average time (in days) that a company takes to pay
        its bills to its trade creditors, which may include suppliers,
        vendors, or financiers.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        Parameters
        ----------
        reportDate : str
            The date the outstanding values are calculated on. Should be
            either the current day or the end of a previous quarter.
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. No collections are currently available
            but may be offered in the future
        order : str
            The sort order for the results, in the [Searchlight order
            syntax](https://github.com/tspence/csharp-searchlight).
        pageSize : int
            The page size for results (default 250, maximum of 500)
        pageNumber : int
            The page number for results (default 0)
        """
        path = "/api/v1/Reports/daily-payable-outstanding-summary"
        result = self.client.send_request("GET", path, None, {"reportDate": reportDate, "filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), DpoSummaryModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def days_payable_outstanding_summary_total(self, reportDate: str) -> LockstepResponse[DpoSummaryGroupTotalModel]:
        """
        Retrieves total number of vendors, bills, the total amount
        outstanding, and the daily payable outstanding value for a
        group.

        Days payable outstanding (DPO) is a financial ratio that
        indicates the average time (in days) that a company takes to pay
        its bills to its trade creditors, which may include suppliers,
        vendors, or financiers.

        Parameters
        ----------
        reportDate : str
            The date the outstanding values are calculated on. Should be
            either the current day or the end of a previous quarter.
        """
        path = "/api/v1/Reports/daily-payable-outstanding-summary-total"
        result = self.client.send_request("GET", path, None, {"reportDate": reportDate}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, DpoSummaryGroupTotalModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
