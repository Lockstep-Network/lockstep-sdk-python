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
class InvoiceSummaryModel:
    """
    Contains summarized data for an invoice
    """

    groupKey: object | None = None
    customerId: object | None = None
    invoiceId: object | None = None
    invoiceNumber: object | None = None
    invoiceDate: object | None = None
    invoiceClosedDate: object | None = None
    customerName: object | None = None
    status: object | None = None
    paymentDueDate: object | None = None
    currencyCode: object | None = None
    invoiceAmount: object | None = None
    outstandingBalance: object | None = None
    baseCurrencyCode: object | None = None
    baseCurrencyInvoiceAmount: object | None = None
    baseCurrencyOutstandingBalance: object | None = None
    invoiceTypeCode: object | None = None
    newestActivity: object | None = None
    daysPastDue: object | None = None
    paymentCount: object | None = None
    supportsErpPdfRetrieval: object | None = None
    paymentNumbers: list[object] | None = None
    paymentIds: list[object] | None = None
    modified: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
