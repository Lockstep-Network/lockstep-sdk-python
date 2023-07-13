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
class InsertPaymentRequestModel:
    """
    A request to insert a new Payment
    """

    appEnrollmentId: object | None = None
    paymentId: object | None = None
    companyId: object | None = None
    companyErpKey: object | None = None
    companyExternalReference: object | None = None
    erpKey: object | None = None
    paymentType: object | None = None
    tenderType: object | None = None
    memoText: object | None = None
    paymentDate: object | None = None
    postDate: object | None = None
    paymentAmount: object | None = None
    unappliedAmount: object | None = None
    currencyCode: object | None = None
    referenceCode: object | None = None
    isVoided: object | None = None
    inDispute: object | None = None
    currencyRate: object | None = None
    baseCurrencyPaymentAmount: object | None = None
    baseCurrencyUnappliedAmount: object | None = None
    bankAccountId: object | None = None
    groupKey: object | None = None
    applications: list[object] | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
