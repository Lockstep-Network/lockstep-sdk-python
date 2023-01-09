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

    groupKey: str | None = None
    baseCurrencyCode: str | None = None
    currencyCode: str | None = None
    paymentAppliedId: str | None = None
    invoiceId: str | None = None
    paymentId: str | None = None
    applyToInvoiceDate: str | None = None
    paymentAppliedAmount: float | None = None
    baseCurrencyPaymentAppliedAmount: float | None = None
    referenceCode: str | None = None
    companyId: str | None = None
    paymentAmount: float | None = None
    unappliedAmount: float | None = None
    baseCurrencyPaymentAmount: float | None = None
    baseCurrencyUnappliedAmount: float | None = None

