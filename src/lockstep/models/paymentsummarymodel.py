#
# Lockstep Platform SDK for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
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
    paymentType: str | None = None
    paymentDate: str | None = None
    paymentAmount: float | None = None
    unappliedAmount: float | None = None
    invoiceCount: int | None = None
    totalPaymentsApplied: float | None = None
    invoiceList: list[str] | None = None
    invoiceIdList: list[str] | None = None
    customerName: str | None = None
    customerId: str | None = None

