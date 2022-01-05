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




"""
Contains detailed information about a Payment.
"""
class PaymentDetailModel:
    groupKey: str
    paymentId: str
    customerId: str
    customerName: str
    memoText: str
    referenceCode: str
    primaryContact: str
    email: str
    paymentAmount: float
    unappliedAmount: float
    paymentType: str
    paymentDate: str
    postDate: str
    phone: str
    fax: str
    address1: str
    address2: str
    address3: str
    city: str
    stateRegion: str
    postalCode: str
    countryCode: str

