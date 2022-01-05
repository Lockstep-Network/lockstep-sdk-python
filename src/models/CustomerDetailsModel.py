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



from src.models.CustomerDetailsPaymentModel import CustomerDetailsPaymentModel

# Contains customer details data
class CustomerDetailsModel:
    groupKey: str
    customerId: str
    name: str
    address1: str
    address2: str
    address3: str
    city: str
    state: str
    postalCode: str
    country: str
    phoneNumber: str
    faxNumber: str
    email: str
    contactId: str
    contactName: str
    contactEmail: str
    outstandingInvoices: int
    outstandingAmount: float
    amountPastDue: float
    payments: list[CustomerDetailsPaymentModel]

