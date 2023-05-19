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

    groupKey: object | None = None
    baseCurrencyCode: object | None = None
    reportPeriod: object | None = None
    reportDate: object | None = None
    invoiceMonthName: object | None = None
    totalInvoiceCount: object | None = None
    totalInvoiceAmount: object | None = None
    atRiskCount: object | None = None
    atRiskAmount: object | None = None
    atRiskCountPercentage: object | None = None
    atRiskPercentage: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
