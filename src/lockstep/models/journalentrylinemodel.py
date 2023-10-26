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
class JournalEntryLineModel:
    """
    Contains information about a journal entry line
    """

    journalEntryLineId: object | None = None
    journalEntryId: object | None = None
    groupKey: object | None = None
    appEnrollmentId: object | None = None
    erpKey: object | None = None
    financialAccountId: object | None = None
    accountNumber: object | None = None
    accountName: object | None = None
    debit: object | None = None
    credit: object | None = None
    currencyCode: object | None = None
    baseDebit: object | None = None
    baseCredit: object | None = None
    baseCurrencyCode: object | None = None
    sourceCreatedUser: object | None = None
    memo: object | None = None
    dimensions: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None
    sourceModifiedDate: object | None = None
    journalEntry: object | None = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
