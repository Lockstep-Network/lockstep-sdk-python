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
class FinancialInstitutionAccountModel:
    """
    An Financial Institution Account represents an account used for
    monetary transactions. E.g. - checking, savings, or credit card
    accounts.
    """

    financialInstitutionAccountId: object | None = None
    groupKey: object | None = None
    bankAccountId: object | None = None
    erpKey: object | None = None
    appEnrollmentId: object | None = None
    name: object | None = None
    status: object | None = None
    description: object | None = None
    accountType: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
