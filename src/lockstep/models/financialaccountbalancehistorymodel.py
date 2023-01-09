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

    financialAccountBalanceHistoryId: str | None = None
    groupKey: str | None = None
    financialAccountId: str | None = None
    appEnrollmentId: str | None = None
    financialYear: int | None = None
    periodNumber: int | None = None
    periodStartDate: str | None = None
    periodEndDate: str | None = None
    status: str | None = None
    balance: float | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None

