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
from lockstep.models.customerdetailspaymentmodel import CustomerDetailsPaymentModel

"""
Contains customer details data
"""
@dataclass
class CustomerDetailsModel:
    groupKey: str = None
    customerId: str = None
    name: str = None
    address1: str = None
    address2: str = None
    address3: str = None
    city: str = None
    state: str = None
    postalCode: str = None
    country: str = None
    phoneNumber: str = None
    faxNumber: str = None
    email: str = None
    contactId: str = None
    contactName: str = None
    contactEmail: str = None
    outstandingInvoices: int = None
    outstandingAmount: float = None
    amountPastDue: float = None
    payments: list[CustomerDetailsPaymentModel] = None

