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

    groupKey: str | None = None
    reportBucket: str | None = None
    totalVendors: int | None = None
    totalBillsOutstanding: int | None = None
    totalBillsOutstandingAmount: float | None = None
    totalCreditMemoOutstandingAmount: float | None = None
    totalAdvancePaymentAmount: float | None = None
    totalOutstandingAmount: float | None = None
    totalApAmount: float | None = None
    percentageOfTotalAp: float | None = None

