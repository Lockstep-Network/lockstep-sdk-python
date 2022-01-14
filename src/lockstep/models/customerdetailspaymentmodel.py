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
Customer payment collected information
"""
@dataclass
class CustomerDetailsPaymentModel:
    groupKey: str = None
    paymentId: str = None
    paymentAppliedId: str = None
    paymentType: str = None
    invoiceId: str = None
    invoiceTypeCode: str = None
    invoiceReferenceCode: str = None
    invoiceTotalAmount: float = None
    paymentDate: str = None
    paymentAmount: float = None

