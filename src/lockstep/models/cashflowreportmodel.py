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
class CashflowReportModel:
    """
    Represents the cashflow report based on a timeframe
    """

    timeframe: int | None = None
    paymentsCollected: float | None = None
    paymentsCollectedCount: int | None = None
    invoicesBilled: float | None = None
    invoicesBilledCount: int | None = None

