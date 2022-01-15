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
Aggregated Accounts Receivable information.
"""
@dataclass
class ArHeaderInfoModel:
    groupKey: str = None
    reportPeriod: str = None
    totalCustomers: int = None
    totalInvoices: int = None
    totalInvoicedAmount: float = None
    totalUnappliedPayments: float = None
    totalCollected: float = None
    totalArAmount: float = None
    totalInvoicesPaid: int = None
    totalInvoicesPastDue: int = None
    totalInvoices90DaysPastDue: int = None
    totalPastDueAmount: float = None
    totalPastDueAmount90Days: float = None
    percentageOfTotalAr: float = None
    dso: float = None
    totalInvoiceAmountCurrentYear: float = None
    totalInvoiceAmountPreviousYear: float = None
    totalPaymentAmountCurrentYear: float = None
    totalCollectedPastThirtyDays: int = None
    totalInvoicesPaidPastThirtyDays: int = None
    percentageOfTotalAr90DaysPastDue: float = None

