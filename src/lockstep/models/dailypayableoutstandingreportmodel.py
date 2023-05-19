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
class DailyPayableOutstandingReportModel:
    """
    Represents the daily payable outstanding report
    """

    timeframe: object | None = None
    invoiceCount: object | None = None
    dailyPayableOutstanding: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
