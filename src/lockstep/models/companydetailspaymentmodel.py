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

    groupKey: str | None = None
    paymentId: str | None = None
    paymentAppliedId: str | None = None
    paymentType: str | None = None
    invoiceId: str | None = None
    invoiceTypeCode: str | None = None
    invoiceReferenceCode: str | None = None
    invoiceCurrencyCode: str | None = None
    invoiceTotalAmount: float | None = None
    paymentDate: str | None = None
    paymentCurrencyCode: str | None = None
    paymentAmount: float | None = None

