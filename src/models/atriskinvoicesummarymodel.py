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
Contains summarized data for an invoice
"""
@dataclass
class AtRiskInvoiceSummaryModel:
    reportDate: str
    groupKey: str
    customerId: str
    invoiceId: str
    invoiceNumber: str
    invoiceDate: str
    customerName: str
    status: str
    paymentDueDate: str
    invoiceAmount: float
    outstandingBalance: float
    invoiceTypeCode: str
    newestActivity: str
    daysPastDue: int
    paymentNumbers: list[str]
    paymentIds: list[str]

