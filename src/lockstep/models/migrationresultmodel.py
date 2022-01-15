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
Information about the migration action for a particular group
"""
@dataclass
class MigrationResultModel:
    messages: list[str] = None
    groupKey: str = None
    invoiceCount: int = None
    addressCount: int = None
    invoiceFieldCount: int = None
    lineCount: int = None
    contactCount: int = None
    companyCount: int = None
    paymentCount: int = None
    paymentFieldCount: int = None
    paymentAppliedCount: int = None

