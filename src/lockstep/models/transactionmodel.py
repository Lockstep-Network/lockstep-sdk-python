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
class TransactionModel:
    """
    Represents detailed transaction information which represents either
    Invoices, Credit Memos or Payments within the group account.
    """

    groupKey: object | None = None
    baseCurrencyCode: object | None = None
    referenceNumber: object | None = None
    transactionId: object | None = None
    transactionStatus: object | None = None
    transactionType: object | None = None
    transactionSubType: object | None = None
    transactionDate: object | None = None
    dueDate: object | None = None
    daysPastDue: object | None = None
    currencyCode: object | None = None
    transactionAmount: object | None = None
    outstandingAmount: object | None = None
    baseCurrencyTransactionAmount: object | None = None
    baseCurrencyOutstandingAmount: object | None = None
    transactionDetailCount: object | None = None
    supportsErpPdfRetrieval: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
