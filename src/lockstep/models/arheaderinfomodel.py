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
class ArHeaderInfoModel:
    """
    Aggregated Accounts Receivable information.
    """

    groupKey: object | None = None
    baseCurrencyCode: object | None = None
    reportDate: object | None = None
    reportPeriod: object | None = None
    totalCustomers: object | None = None
    totalInvoices: object | None = None
    totalInvoicedAmount: object | None = None
    totalUnappliedPayments: object | None = None
    totalCollected: object | None = None
    totalArAmount: object | None = None
    totalInvoicesPaid: object | None = None
    totalInvoicesPastDue: object | None = None
    totalInvoices90DaysPastDue: object | None = None
    totalPastDueAmount: object | None = None
    totalPastDueAmount90Days: object | None = None
    percentageOfTotalAr: object | None = None
    dso: object | None = None
    totalInvoiceAmountCurrentYear: object | None = None
    totalInvoiceAmountPreviousYear: object | None = None
    totalPaymentAmountCurrentYear: object | None = None
    percentageOfTotalAr90DaysPastDue: object | None = None
    customersPaidPastThirtyDays: object | None = None
    amountCollectedPastThirtyDays: object | None = None
    unappliedAmountPastThirtyDays: object | None = None
    invoicesPaidPastThirtyDays: object | None = None
    customersInvoicedPastThirtyDays: object | None = None
    amountInvoicedPastThirtyDays: object | None = None
    amountDuePastThirtyDays: object | None = None
    invoicesPastThirtyDays: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
