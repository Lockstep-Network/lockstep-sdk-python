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

    groupKey: object | None = None
    vendorId: object | None = None
    vendorName: object | None = None
    appEnrollmentId: object | None = None
    primaryContactName: object | None = None
    primaryContactId: object | None = None
    amountPaidLast30: object | None = None
    amountPaidPastThirtyDays: object | None = None
    advancePayLast30: object | None = None
    advancePayPastThirtyDays: object | None = None
    advancePayOutstanding: object | None = None
    amountBilledLast30: object | None = None
    amountBilledPastThirtyDays: object | None = None
    amountBilledOutstandingLast30: object | None = None
    amountBilledOutstandingPastThirtyDays: object | None = None
    amountBilledOutstanding: object | None = None
    billCountLast30: object | None = None
    billCountPastThirtyDays: object | None = None
    paidBillCountLast30: object | None = None
    paidBillCountPastThirtyDays: object | None = None
    openBillCount: object | None = None
    paidBillCount: object | None = None
    totalBillCount: object | None = None
    dpo: object | None = None
    modified: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
