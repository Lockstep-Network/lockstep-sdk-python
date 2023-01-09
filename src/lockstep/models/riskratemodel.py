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
class RiskRateModel:
    """
    Represents a risk rate calculation for a single month
    """

    groupKey: str | None = None
    baseCurrencyCode: str | None = None
    reportPeriod: str | None = None
    reportDate: str | None = None
    invoiceMonthName: str | None = None
    totalInvoiceCount: int | None = None
    totalInvoiceAmount: float | None = None
    atRiskCount: int | None = None
    atRiskAmount: float | None = None
    atRiskCountPercentage: float | None = None
    atRiskPercentage: float | None = None

