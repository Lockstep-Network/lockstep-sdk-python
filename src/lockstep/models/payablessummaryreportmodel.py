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
class PayablesSummaryReportModel:
    """
    Represents the payables summary report based on a timeframe
    """

    groupKey: str | None = None
    timeframe: int | None = None
    totalPaymentsAmount: float | None = None
    totalPaymentsCount: int | None = None
    totalAmountBilled: float | None = None
    totalBillsCount: int | None = None

