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

    groupKey: str | None = None
    baseCurrencyCode: str | None = None
    referenceNumber: str | None = None
    transactionId: str | None = None
    transactionStatus: str | None = None
    transactionType: str | None = None
    transactionSubType: str | None = None
    transactionDate: str | None = None
    dueDate: str | None = None
    daysPastDue: int | None = None
    currencyCode: str | None = None
    transactionAmount: float | None = None
    outstandingAmount: float | None = None
    baseCurrencyTransactionAmount: float | None = None
    baseCurrencyOutstandingAmount: float | None = None
    transactionDetailCount: int | None = None
    supportsErpPdfRetrieval: bool | None = None

