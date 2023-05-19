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
class InvoicePaymentDetailModel:
    """
    View to return Payment Detail information for a given Invoice
    record.
    """

    groupKey: object | None = None
    baseCurrencyCode: object | None = None
    currencyCode: object | None = None
    paymentAppliedId: object | None = None
    invoiceId: object | None = None
    paymentId: object | None = None
    applyToInvoiceDate: object | None = None
    paymentAppliedAmount: object | None = None
    baseCurrencyPaymentAppliedAmount: object | None = None
    referenceCode: object | None = None
    companyId: object | None = None
    paymentAmount: object | None = None
    unappliedAmount: object | None = None
    baseCurrencyPaymentAmount: object | None = None
    baseCurrencyUnappliedAmount: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
