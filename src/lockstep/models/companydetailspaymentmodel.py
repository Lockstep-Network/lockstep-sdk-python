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
class CompanyDetailsPaymentModel:
    """
    Company payment collected information
    """

    groupKey: object | None = None
    paymentId: object | None = None
    paymentAppliedId: object | None = None
    paymentType: object | None = None
    invoiceId: object | None = None
    invoiceTypeCode: object | None = None
    invoiceReferenceCode: object | None = None
    invoiceCurrencyCode: object | None = None
    invoiceTotalAmount: object | None = None
    paymentDate: object | None = None
    paymentCurrencyCode: object | None = None
    paymentAmount: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
