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
Contains detailed information about a Payment.
"""
@dataclass
class PaymentDetailModel:
    groupKey: str = None
    paymentId: str = None
    customerId: str = None
    customerName: str = None
    memoText: str = None
    referenceCode: str = None
    primaryContact: str = None
    email: str = None
    paymentAmount: float = None
    unappliedAmount: float = None
    paymentType: str = None
    paymentDate: str = None
    postDate: str = None
    phone: str = None
    fax: str = None
    address1: str = None
    address2: str = None
    address3: str = None
    city: str = None
    stateRegion: str = None
    postalCode: str = None
    countryCode: str = None

