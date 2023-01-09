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

    groupKey: str | None = None
    baseCurrencyCode: str | None = None
    reportDate: str | None = None
    reportPeriod: str | None = None
    totalVendors: int | None = None
    totalBills: int | None = None
    totalBilledAmount: float | None = None
    totalAdvancePayments: float | None = None
    totalPaid: float | None = None
    totalApAmount: float | None = None
    totalBillsPaid: int | None = None
    totalBillsPastDue: int | None = None
    totalBills90DaysPastDue: int | None = None
    totalPastDueAmount: float | None = None
    totalPastDueAmount90Days: float | None = None
    percentageOfTotalAp: float | None = None
    totalBilledAmountCurrentYear: float | None = None
    totalBilledAmountPreviousYear: float | None = None
    totalPaidAmountCurrentYear: float | None = None
    percentageOfTotalAp90DaysPastDue: float | None = None
    vendorsPaidPastThirtyDays: int | None = None
    amountPaidPastThirtyDays: float | None = None
    advancePaymentAmountPastThirtyDays: float | None = None
    billsPaidPastThirtyDays: int | None = None
    billingVendorsPastThirtyDays: int | None = None
    amountBilledPastThirtyDays: float | None = None
    amountDuePastThirtyDays: float | None = None
    billsPastThirtyDays: int | None = None

