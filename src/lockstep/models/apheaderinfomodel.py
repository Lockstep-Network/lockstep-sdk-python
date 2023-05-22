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
class ApHeaderInfoModel:
    """
    Aggregated Accounts Payable information.
    """

    groupKey: object | None = None
    baseCurrencyCode: object | None = None
    reportDate: object | None = None
    reportPeriod: object | None = None
    totalVendors: object | None = None
    totalBills: object | None = None
    totalBilledAmount: object | None = None
    totalAdvancePayments: object | None = None
    totalPaid: object | None = None
    totalApAmount: object | None = None
    totalBillsPaid: object | None = None
    totalBillsPastDue: object | None = None
    totalBills90DaysPastDue: object | None = None
    totalPastDueAmount: object | None = None
    totalPastDueAmount90Days: object | None = None
    percentageOfTotalAp: object | None = None
    totalBilledAmountCurrentYear: object | None = None
    totalBilledAmountPreviousYear: object | None = None
    totalPaidAmountCurrentYear: object | None = None
    percentageOfTotalAp90DaysPastDue: object | None = None
    vendorsPaidPastThirtyDays: object | None = None
    amountPaidPastThirtyDays: object | None = None
    advancePaymentAmountPastThirtyDays: object | None = None
    billsPaidPastThirtyDays: object | None = None
    billingVendorsPastThirtyDays: object | None = None
    amountBilledPastThirtyDays: object | None = None
    amountDuePastThirtyDays: object | None = None
    billsPastThirtyDays: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
