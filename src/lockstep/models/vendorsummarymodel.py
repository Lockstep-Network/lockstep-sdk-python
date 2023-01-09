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
class VendorSummaryModel:
    """
    Contains summarized data for a vendor
    """

    groupKey: str | None = None
    vendorId: str | None = None
    vendorName: str | None = None
    appEnrollmentId: str | None = None
    primaryContactName: str | None = None
    primaryContactId: str | None = None
    amountPaidLast30: float | None = None
    amountPaidPastThirtyDays: float | None = None
    advancePayLast30: float | None = None
    advancePayPastThirtyDays: float | None = None
    advancePayOutstanding: float | None = None
    amountBilledLast30: float | None = None
    amountBilledPastThirtyDays: float | None = None
    amountBilledOutstandingLast30: float | None = None
    amountBilledOutstandingPastThirtyDays: float | None = None
    amountBilledOutstanding: float | None = None
    billCountLast30: int | None = None
    billCountPastThirtyDays: int | None = None
    paidBillCountLast30: int | None = None
    paidBillCountPastThirtyDays: int | None = None
    openBillCount: int | None = None
    paidBillCount: int | None = None
    totalBillCount: int | None = None
    dpo: float | None = None
    modified: str | None = None

