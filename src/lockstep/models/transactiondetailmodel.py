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
class TransactionDetailModel:
    """
    Represents transaction detail information associated to a
    transaction. This can either be Invoices which are paid with a
    Credit Memo or Payment transaction, or Credit Memos or Payments used
    as payment for an Invoice transaction.
    """

    groupKey: object | None = None
    baseCurrencyCode: object | None = None
    referenceNumber: object | None = None
    transactionDetailId: object | None = None
    transactionDetailAppliedId: object | None = None
    transactionId: object | None = None
    transactionType: object | None = None
    transactionSubType: object | None = None
    transactionDate: object | None = None
    transactionInvoiceDate: object | None = None
    currencyCode: object | None = None
    transactionAmount: object | None = None
    outstandingAmount: object | None = None
    baseCurrencyTransactionAmount: object | None = None
    baseCurrencyOutstandingAmount: object | None = None
    supportsErpPdfRetrieval: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
