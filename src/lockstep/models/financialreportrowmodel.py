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


from __future__ import annotations
from dataclasses import dataclass

@dataclass
class FinancialReportRowModel:
    """
    Represents a row of a financial Report report
    """

    rowType: object | None = None
    label: object | None = None
    rows: list[object] | None = None
    cells: list[object] | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
