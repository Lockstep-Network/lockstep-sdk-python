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
Represents a single address for an invoice
"""
@dataclass
class InvoiceAddressModel:
    invoiceAddressId: str = None
    groupKey: str = None
    invoiceId: str = None
    line1: str = None
    line2: str = None
    line3: str = None
    city: str = None
    region: str = None
    postalCode: str = None
    country: str = None
    latitude: float = None
    longitude: float = None
    created: str = None
    createdUserId: str = None
    modified: str = None
    modifiedUserId: str = None

