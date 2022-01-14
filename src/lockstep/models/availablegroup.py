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
Data counts for the GroupKey.
"""
@dataclass
class AvailableGroup:
    groupKey: str = None
    invoiceCount: int = None
    lineCount: int = None
    companyCount: int = None
    contactCount: int = None
    paymentCount: int = None
    paymentAppliedCount: int = None

