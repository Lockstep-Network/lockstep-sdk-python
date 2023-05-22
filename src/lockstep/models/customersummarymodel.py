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

    groupKey: object | None = None
    companyId: object | None = None
    companyName: object | None = None
    primaryContact: object | None = None
    appEnrollmentId: object | None = None
    outstandingInvoices: object | None = None
    totalInvoicesOpen: object | None = None
    totalInvoicesPastDue: object | None = None
    closedInvoices: object | None = None
    closedInvoicesPastThirtyDays: object | None = None
    amountCollected: object | None = None
    amountCollectedPastThirtyDays: object | None = None
    outstandingAmount: object | None = None
    invoicedAmountPastThirtyDays: object | None = None
    outstandingAmountPastThirtyDays: object | None = None
    invoicesPastThirtyDays: object | None = None
    amountPastDue: object | None = None
    unappliedPayments: object | None = None
    unappliedAmountPastThirtyDays: object | None = None
    percentOfTotalAr: object | None = None
    dso: object | None = None
    newestActivity: object | None = None
    modified: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
