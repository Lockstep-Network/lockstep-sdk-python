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
class CreditMemoInvoiceModel:
    """
    Contains information about a credit memo invoice
    """

    groupKey: object | None = None
    baseCurrencyCode: object | None = None
    currencyCode: object | None = None
    creditMemoAppliedId: object | None = None
    invoiceId: object | None = None
    creditMemoInvoiceId: object | None = None
    applyToInvoiceDate: object | None = None
    creditMemoAppliedAmount: object | None = None
    baseCurrencyCreditMemoAppliedAmount: object | None = None
    referenceCode: object | None = None
    companyId: object | None = None
    customerId: object | None = None
    invoiceStatusCode: object | None = None
    totalAmount: object | None = None
    outstandingBalanceAmount: object | None = None
    baseCurrencyTotalAmount: object | None = None
    baseCurrencyOutstandingBalanceAmount: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
