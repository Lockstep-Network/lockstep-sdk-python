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
class PaymentSummaryModel:
    """
    Contains summary information for a Payment
    """

    groupKey: str | None = None
    paymentId: str | None = None
    memoText: str | None = None
    referenceCode: str | None = None
    tenderType: str | None = None
    paymentType: str | None = None
    paymentDate: str | None = None
    currencyCode: str | None = None
    paymentAmount: float | None = None
    unappliedAmount: float | None = None
    baseCurrencyCode: str | None = None
    baseCurrencyPaymentAmount: float | None = None
    baseCurrencyUnappliedAmount: float | None = None
    isOpen: bool | None = None
    invoiceCount: int | None = None
    totalPaymentsApplied: float | None = None
    invoiceList: list[str] | None = None
    invoiceIdList: list[str] | None = None
    paymentCompanyId: str | None = None
    paymentCompanyName: str | None = None
    supportsErpPdfRetrieval: bool | None = None
    customerIds: list[str] | None = None
    customerNames: list[str] | None = None
    companyIds: list[str] | None = None
    companyNames: list[str] | None = None
    modified: str | None = None

