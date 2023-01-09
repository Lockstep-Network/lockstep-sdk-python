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
class FinancialAccountModel:
    """
    An Financial account refers to records of assets, liabilities,
    income, expenses, and equity.
    """

    financialAccountId: str | None = None
    groupKey: str | None = None
    code: str | None = None
    erpKey: str | None = None
    appEnrollmentId: str | None = None
    name: str | None = None
    status: str | None = None
    cashflowType: str | None = None
    description: str | None = None
    classification: str | None = None
    category: str | None = None
    subcategory: str | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None

