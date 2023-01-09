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
class InvoiceHistoryModel:
    """
    An Invoice represents a bill sent from one company to another. The
    Lockstep Platform tracks changes to each Invoice so that you can
    observe the changes over time. You can view the InvoiceHistory list
    to monitor and observe the changes of this Invoice and track the
    dates when changes occurred.
    """

    groupKey: str | None = None
    invoiceHistoryId: str | None = None
    invoiceId: str | None = None
    companyId: str | None = None
    customerId: str | None = None
    erpKey: str | None = None
    purchaseOrderCode: str | None = None
    referenceCode: str | None = None
    salespersonCode: str | None = None
    salespersonName: str | None = None
    invoiceTypeCode: str | None = None
    invoiceStatusCode: str | None = None
    termsCode: str | None = None
    specialTerms: str | None = None
    currencyCode: str | None = None
    totalAmount: float | None = None
    salesTaxAmount: float | None = None
    discountAmount: float | None = None
    outstandingBalanceAmount: float | None = None
    invoiceDate: str | None = None
    discountDate: str | None = None
    postedDate: str | None = None
    invoiceClosedDate: str | None = None
    paymentDueDate: str | None = None
    importedDate: str | None = None
    primaryOriginAddressId: str | None = None
    primaryBillToAddressId: str | None = None
    primaryShipToAddressId: str | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None
    appEnrollmentId: str | None = None
    currencyRate: float | None = None

