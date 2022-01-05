#
# Lockstep Software Development Kit for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Ted Spence <tspence@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @version    2021.39
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#




# Represents the cashflow report based on a timeframe
class CashflowReportModel:
    timeframe: int
    paymentsCollected: float
    paymentsCollectedCount: int
    invoicesBilled: float
    invoicesBilledCount: int

