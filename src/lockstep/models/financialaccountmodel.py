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

    financialAccountId: object | None = None
    groupKey: object | None = None
    code: object | None = None
    erpKey: object | None = None
    appEnrollmentId: object | None = None
    name: object | None = None
    status: object | None = None
    cashflowType: object | None = None
    description: object | None = None
    classification: object | None = None
    category: object | None = None
    subcategory: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
