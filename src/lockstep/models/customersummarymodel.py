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
Contains summarized data for a customer
"""
@dataclass
class CustomerSummaryModel:
    groupKey: str = None
    companyId: str = None
    companyName: str = None
    primaryContact: str = None
    outstandingInvoices: int = None
    totalInvoicesOpen: int = None
    totalInvoicesPastDue: int = None
    closedInvoices: int = None
    amountCollected: float = None
    outstandingAmount: float = None
    amountPastDue: float = None
    unappliedPayments: float = None
    percentOfTotalAr: float = None
    dso: float = None
    newestActivity: str = None

