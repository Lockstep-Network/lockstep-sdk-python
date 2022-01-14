#
# Lockstep Software Development Kit for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Ted Spence <tspence@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @version    2022.2
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

"""
Contains summary information for a Payment
"""
@dataclass
class PaymentSummaryModel:
    groupKey: str = None
    paymentId: str = None
    memoText: str = None
    referenceCode: str = None
    paymentType: str = None
    paymentDate: str = None
    paymentAmount: float = None
    unappliedAmount: float = None
    invoiceCount: int = None
    totalPaymentsApplied: float = None
    invoiceList: list[str] = None
    invoiceIdList: list[str] = None
    customerName: str = None
    customerId: str = None

