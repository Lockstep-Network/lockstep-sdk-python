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
class PayablesSummaryReportModel:
    """
    Represents the payables summary report based on a timeframe
    """

    groupKey: object | None = None
    timeframe: object | None = None
    baseCurrencyCode: object | None = None
    totalPaymentsAmount: object | None = None
    totalPaymentsCount: object | None = None
    totalAmountBilled: object | None = None
    totalBillsCount: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
