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


from dataclasses import dataclass

@dataclass
class AtRiskInvoiceSummaryModel:
    """
    Contains summarized data for an invoice
    """

    reportDate: str | None = None
    groupKey: str | None = None
    customerId: str | None = None
    invoiceId: str | None = None
    invoiceNumber: str | None = None
    invoiceDate: str | None = None
    customerName: str | None = None
    status: str | None = None
    paymentDueDate: str | None = None
    currencyCode: str | None = None
    invoiceAmount: float | None = None
    outstandingBalance: float | None = None
    baseCurrencyCode: str | None = None
    baseCurrencyInvoiceAmount: float | None = None
    baseCurrencyOutstandingBalance: float | None = None
    invoiceTypeCode: str | None = None
    newestActivity: str | None = None
    daysPastDue: int | None = None
    paymentNumbers: list[str] | None = None
    paymentIds: list[str] | None = None

