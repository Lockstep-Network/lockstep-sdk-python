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




"""
Information about the migration action for a particular group
"""
class MigrationResultModel:
    messages: list[str]
    groupKey: str
    invoiceCount: int
    addressCount: int
    invoiceFieldCount: int
    lineCount: int
    contactCount: int
    companyCount: int
    paymentCount: int
    paymentFieldCount: int
    paymentAppliedCount: int

