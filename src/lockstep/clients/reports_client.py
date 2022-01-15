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
# @version    2022.2
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

from lockstep.lockstep_response import LockstepResponse

class ReportsClient:

    def __init__(self, client):
        self.client = client

    """
    Retrieves a current Cash Flow report for this account. 

    The Cash Flow report indicates the amount of payments retrieved and 
    invoices billed within a given timeframe. You can use this report to 
    determine the overall balance of money coming into and out of your 
    accounts receivable and accounts payable businesses.

    Parameters
    ----------
    timeframe : int
        Number of days of data to include for the Cash Flow Report 
        (default is 30 days from today)
    """
    def cash_flow(self, timeframe: int) -> LockstepResponse:
        path = f"/api/v1/Reports/cashflow"
        return self.client.send_request("GET", path, None, {timeframe: int})

    """
    Retrieves a current Daily Sales Outstanding (DSO) report for this 
    account. 

    Daily Sales Outstanding, or DSO, is a metric that indicates the 
    average number of days that it takes for an invoice to be fully 
    paid. You can use this report to identify whether a company is 
    improving on its ability to collect on invoices.

    Parameters
    ----------
    """
    def daily_sales_outstanding(self, ) -> LockstepResponse:
        path = f"/api/v1/Reports/dailysalesoutstanding"
        return self.client.send_request("GET", path, None, None)

    """
    Retrieves a current Risk Rate report for this account. 

    Risk Rate is a metric that indicates the percentage of total AR 
    balance left unpaid after 90 days. You can use this report to 
    identify the percentage of invoice value that is not being collected 
    in a timely manner.

    Parameters
    ----------
    """
    def risk_rates(self, ) -> LockstepResponse:
        path = f"/api/v1/Reports/riskrates"
        return self.client.send_request("GET", path, None, None)

    """
    Retrieves AR header information up to the date specified.

    Parameters
    ----------
    reportDate : str
        The date of the report.
    companyId : str
        Include a company to get AR data for a specific company, leave 
        as null to include all Companies.
    """
    def accounts_receivable_header(self, reportDate: str, companyId: str) -> LockstepResponse:
        path = f"/api/v1/Reports/ar-header"
        return self.client.send_request("GET", path, None, {reportDate: str, companyId: str})

    """
    The Aging Report contains information about the total dollar value 
    of invoices broken down by their age. Last default or specified 
    bucket treated as a catch all bucket for values that fit in that 
    bucket or beyond. 

    You can specify viewing parameters for the aging report such as 
    currency code and date bucket configuration. You can also view aging 
    data for an entire account or a specific company. 

    This information is recalculated when invoice data changes. After 
    each invoice data change occurs, Lockstep queues up a calculation 
    based on the current invoice data at that time. This information is 
    calculated and persisted for each customer so that the report will 
    be available quickly. 

    To force a recalculation of aging data, specify the `recalculate` 
    option. Note that forcing a recalculation will slow your API 
    response time.

    Parameters
    ----------
    CompanyId : str
        Company aging buckets are filtered by (all company aging 
        returned if not company specified)
    Recalculate : bool
        Force api to recalculate aging data, cached data may be returned 
        when set to false
    CurrencyCode : str
        Currency aging buckets are converted to (all aging data returned 
        without currency conversion if no currency is specified)
    CurrencyProvider : str
        Currency provider currency rates should be returned from to 
        convert aging amounts to (default Lockstep currency provider 
        used if no data provider specified)
    Buckets : list[int]
        Customized buckets used for aging calculations (default buckets 
        [0,30,60,90,120,180] will be used if buckets not specified)
    """
    def invoice_aging_report(self, CompanyId: str, Recalculate: bool, CurrencyCode: str, CurrencyProvider: str, Buckets: list[int]) -> LockstepResponse:
        path = f"/api/v1/Reports/aging"
        return self.client.send_request("GET", path, None, {CompanyId: str, Recalculate: bool, CurrencyCode: str, CurrencyProvider: str, Buckets: list[int]})

    """
    Retrieves AR Aging Header information report broken down by aging 
    bucket. 

    The AR Aging Header report contains aggregated information about the 
    `TotalInvoicesPastDue`, `TotalCustomers`, and their respective 
    `PercentageOfTotalAr` grouped by their aging `ReportBucket`.

    Parameters
    ----------
    """
    def accounts_receivable_aging_header(self, ) -> LockstepResponse:
        path = f"/api/v1/Reports/ar-aging-header"
        return self.client.send_request("GET", path, None, None)

    """
    Retrieves Attachment Header information for the requested companyId. 
    

    The Attachment Header report contains aggregated information about 
    the `TotalAttachments`, `TotalArchived`, and `TotalActive` 
    attachment classifications.

    Parameters
    ----------
    companyId : str
        Include a specific company to get Attachment data for, leave as 
        null to include all Companies.
    """
    def attachments_header_information(self, companyId: str) -> LockstepResponse:
        path = f"/api/v1/Reports/attachments-header"
        return self.client.send_request("GET", path, None, {companyId: str})
