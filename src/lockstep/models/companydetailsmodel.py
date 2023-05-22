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
class CompanyDetailsModel:
    """
    Contains company details data
    """

    groupKey: object | None = None
    customerId: object | None = None
    name: object | None = None
    address1: object | None = None
    address2: object | None = None
    address3: object | None = None
    city: object | None = None
    state: object | None = None
    postalCode: object | None = None
    country: object | None = None
    phoneNumber: object | None = None
    faxNumber: object | None = None
    email: object | None = None
    contactId: object | None = None
    contactName: object | None = None
    contactEmail: object | None = None
    outstandingInvoices: object | None = None
    groupBaseCurrencyCode: object | None = None
    outstandingAmount: object | None = None
    amountPastDue: object | None = None
    payments: list[object] | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
