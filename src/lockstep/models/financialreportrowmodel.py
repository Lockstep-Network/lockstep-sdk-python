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
from lockstep.models.financialreportcellmodel import FinancialReportCellModel

@dataclass
class FinancialReportRowModel:
    """
    Represents a row of a financial Report report
    """

    rowType: str | None = None
    label: str | None = None
    rows: list[FinancialReportRowModel] | None = None
    cells: list[FinancialReportCellModel] | None = None

