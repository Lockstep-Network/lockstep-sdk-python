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




"""
Contains summarized data for a customer
"""
class CustomerSummaryModel:
    groupKey: str
    companyId: str
    companyName: str
    primaryContact: str
    outstandingInvoices: int
    totalInvoicesOpen: int
    totalInvoicesPastDue: int
    closedInvoices: int
    amountCollected: float
    outstandingAmount: float
    amountPastDue: float
    unappliedPayments: float
    percentOfTotalAr: float
    dso: float
    newestActivity: str

