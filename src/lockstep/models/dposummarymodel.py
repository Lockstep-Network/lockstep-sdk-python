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
class DpoSummaryModel:
    """
    Represents a summary of outstanding amounts for bills to vendors and
    their associated daily payable outstanding value.
    """

    groupKey: object | None = None
    vendorId: object | None = None
    vendorName: object | None = None
    primaryContact: object | None = None
    bills: object | None = None
    baseCurrencyCode: object | None = None
    amountOutstanding: object | None = None
    dpo: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
