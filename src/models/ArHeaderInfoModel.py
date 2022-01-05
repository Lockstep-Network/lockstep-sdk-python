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




# Aggregated Accounts Receivable information.
class ArHeaderInfoModel:
    groupKey: str
    reportPeriod: str
    totalCustomers: int
    totalInvoices: int
    totalInvoicedAmount: float
    totalUnappliedPayments: float
    totalCollected: float
    totalArAmount: float
    totalInvoicesPaid: int
    totalInvoicesPastDue: int
    totalInvoices90DaysPastDue: int
    totalPastDueAmount: float
    totalPastDueAmount90Days: float
    percentageOfTotalAr: float
    dso: float
    totalInvoiceAmountCurrentYear: float
    totalInvoiceAmountPreviousYear: float
    totalPaymentAmountCurrentYear: float
    totalCollectedPastThirtyDays: int
    totalInvoicesPaidPastThirtyDays: int
    percentageOfTotalAr90DaysPastDue: float

