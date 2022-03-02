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
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

@dataclass
class FinancialAccountModel:
    """
    An Financial account refers to records of assets, liabilities,
    income, expenses, and equity.
    """

    financialAccountId: str = None
    groupKey: str = None
    code: str = None
    erpKey: str = None
    appEnrollmentId: str = None
    name: str = None
    status: str = None
    cashflowType: str = None
    description: str = None
    classification: str = None
    category: str = None
    subcategory: str = None
    created: str = None
    createdUserId: str = None
    modified: str = None
    modifiedUserId: str = None

