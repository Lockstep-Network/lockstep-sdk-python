#
# Lockstep Platform SDK for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

@dataclass
class ArHeaderInfoModel:
    """
    Aggregated Accounts Receivable information.
    """

    groupKey: str | None = None
    reportPeriod: str | None = None
    totalCustomers: int | None = None
    totalInvoices: int | None = None
    totalInvoicedAmount: float | None = None
    totalUnappliedPayments: float | None = None
    totalCollected: float | None = None
    totalArAmount: float | None = None
    totalInvoicesPaid: int | None = None
    totalInvoicesPastDue: int | None = None
    totalInvoices90DaysPastDue: int | None = None
    totalPastDueAmount: float | None = None
    totalPastDueAmount90Days: float | None = None
    percentageOfTotalAr: float | None = None
    dso: float | None = None
    totalInvoiceAmountCurrentYear: float | None = None
    totalInvoiceAmountPreviousYear: float | None = None
    totalPaymentAmountCurrentYear: float | None = None
    totalCollectedPastThirtyDays: int | None = None
    totalInvoicesPaidPastThirtyDays: int | None = None
    percentageOfTotalAr90DaysPastDue: float | None = None

