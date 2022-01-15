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
Aggregated Accounts Receivable Aging information.
"""
@dataclass
class ArAgingHeaderInfoModel:
    groupKey: str = None
    reportBucket: str = None
    totalCustomers: int = None
    totalInvoicesOutstanding: int = None
    totalOutstandingAmount: float = None
    totalArAmount: float = None
    percentageOfTotalAr: float = None

