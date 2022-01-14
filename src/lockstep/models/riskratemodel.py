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
# @version    2022.2
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

"""
Represents a risk rate calculation for a single month
"""
@dataclass
class RiskRateModel:
    groupKey: str = None
    reportPeriod: str = None
    invoiceMonthName: str = None
    totalInvoiceCount: int = None
    totalInvoiceAmount: float = None
    atRiskCount: int = None
    atRiskAmount: float = None
    atRiskCountPercentage: float = None
    atRiskPercentage: float = None

