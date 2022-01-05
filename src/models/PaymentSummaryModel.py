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
# @version    2021.39
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#




# Contains summary information for a Payment
class PaymentSummaryModel:
    groupKey: str
    paymentId: str
    memoText: str
    referenceCode: str
    paymentType: str
    paymentDate: str
    paymentAmount: float
    unappliedAmount: float
    invoiceCount: int
    totalPaymentsApplied: float
    invoiceList: list[str]
    invoiceIdList: list[str]
    customerName: str
    customerId: str

