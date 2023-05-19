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
class ApAgingHeaderInfoModel:
    """
    Aggregated Accounts Payable Aging information.
    """

    groupKey: object | None = None
    reportBucket: object | None = None
    totalVendors: object | None = None
    totalBillsOutstanding: object | None = None
    totalBillsOutstandingAmount: object | None = None
    totalCreditMemoOutstandingAmount: object | None = None
    totalAdvancePaymentAmount: object | None = None
    totalOutstandingAmount: object | None = None
    totalApAmount: object | None = None
    percentageOfTotalAp: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
