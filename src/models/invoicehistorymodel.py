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
# @version    2021.39
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
    groupKey: str
    invoiceHistoryId: str
    invoiceId: str
    companyId: str
    customerId: str
    erpKey: str
    purchaseOrderCode: str
    referenceCode: str
    salespersonCode: str
    salespersonName: str
    invoiceTypeCode: str
    invoiceStatusCode: str
    termsCode: str
    specialTerms: str
    currencyCode: str
    totalAmount: float
    salesTaxAmount: float
    discountAmount: float
    outstandingBalanceAmount: float
    invoiceDate: str
    discountDate: str
    postedDate: str
    invoiceClosedDate: str
    paymentDueDate: str
    importedDate: str
    primaryOriginAddressId: str
    primaryBillToAddressId: str
    primaryShipToAddressId: str
    created: str
    createdUserId: str
    modified: str
    modifiedUserId: str

