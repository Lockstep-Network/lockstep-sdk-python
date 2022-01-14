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


from dataclasses import dataclass

"""
An Invoice represents a bill sent from one company to another. The 
Lockstep Platform tracks changes to each Invoice so that you can observe 
the changes over time. You can view the InvoiceHistory list to monitor 
and observe the changes of this Invoice and track the dates when changes 
occurred.
"""
@dataclass
class InvoiceHistoryModel:
    groupKey: str = None
    invoiceHistoryId: str = None
    invoiceId: str = None
    companyId: str = None
    customerId: str = None
    erpKey: str = None
    purchaseOrderCode: str = None
    referenceCode: str = None
    salespersonCode: str = None
    salespersonName: str = None
    invoiceTypeCode: str = None
    invoiceStatusCode: str = None
    termsCode: str = None
    specialTerms: str = None
    currencyCode: str = None
    totalAmount: float = None
    salesTaxAmount: float = None
    discountAmount: float = None
    outstandingBalanceAmount: float = None
    invoiceDate: str = None
    discountDate: str = None
    postedDate: str = None
    invoiceClosedDate: str = None
    paymentDueDate: str = None
    importedDate: str = None
    primaryOriginAddressId: str = None
    primaryBillToAddressId: str = None
    primaryShipToAddressId: str = None
    created: str = None
    createdUserId: str = None
    modified: str = None
    modifiedUserId: str = None

