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
class CustomerSummaryModel:
    """
    Contains summarized data for a customer
    """

    groupKey: str | None = None
    companyId: str | None = None
    companyName: str | None = None
    primaryContact: str | None = None
    appEnrollmentId: str | None = None
    outstandingInvoices: int | None = None
    totalInvoicesOpen: int | None = None
    totalInvoicesPastDue: int | None = None
    closedInvoices: int | None = None
    closedInvoicesPastThirtyDays: int | None = None
    amountCollected: float | None = None
    amountCollectedPastThirtyDays: float | None = None
    outstandingAmount: float | None = None
    invoicedAmountPastThirtyDays: float | None = None
    outstandingAmountPastThirtyDays: float | None = None
    invoicesPastThirtyDays: int | None = None
    amountPastDue: float | None = None
    unappliedPayments: float | None = None
    unappliedAmountPastThirtyDays: float | None = None
    percentOfTotalAr: float | None = None
    dso: float | None = None
    newestActivity: str | None = None
    modified: str | None = None

