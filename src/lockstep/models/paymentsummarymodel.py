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

    groupKey: object | None = None
    paymentId: object | None = None
    memoText: object | None = None
    referenceCode: object | None = None
    tenderType: object | None = None
    paymentType: object | None = None
    paymentDate: object | None = None
    currencyCode: object | None = None
    paymentAmount: object | None = None
    unappliedAmount: object | None = None
    baseCurrencyCode: object | None = None
    baseCurrencyPaymentAmount: object | None = None
    baseCurrencyUnappliedAmount: object | None = None
    isOpen: object | None = None
    invoiceCount: object | None = None
    totalPaymentsApplied: object | None = None
    invoiceList: list[object] | None = None
    invoiceIdList: list[object] | None = None
    paymentCompanyId: object | None = None
    paymentCompanyName: object | None = None
    supportsErpPdfRetrieval: object | None = None
    customerIds: list[object] | None = None
    customerNames: list[object] | None = None
    companyIds: list[object] | None = None
    companyNames: list[object] | None = None
    modified: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
