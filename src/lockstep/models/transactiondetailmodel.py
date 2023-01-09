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

    groupKey: str | None = None
    baseCurrencyCode: str | None = None
    referenceNumber: str | None = None
    transactionDetailId: str | None = None
    transactionDetailAppliedId: str | None = None
    transactionId: str | None = None
    transactionType: str | None = None
    transactionSubType: str | None = None
    transactionDate: str | None = None
    transactionInvoiceDate: str | None = None
    currencyCode: str | None = None
    transactionAmount: float | None = None
    outstandingAmount: float | None = None
    baseCurrencyTransactionAmount: float | None = None
    baseCurrencyOutstandingAmount: float | None = None
    supportsErpPdfRetrieval: bool | None = None

