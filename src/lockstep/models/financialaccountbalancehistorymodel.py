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
class FinancialAccountBalanceHistoryModel:
    """
    Represents a balance for a financial account for a given period of
    time.
    """

    financialAccountBalanceHistoryId: object | None = None
    groupKey: object | None = None
    financialAccountId: object | None = None
    appEnrollmentId: object | None = None
    financialYear: object | None = None
    periodNumber: object | None = None
    periodStartDate: object | None = None
    periodEndDate: object | None = None
    status: object | None = None
    balance: object | None = None
    balanceType: object | None = None
    balanceTypeName: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
