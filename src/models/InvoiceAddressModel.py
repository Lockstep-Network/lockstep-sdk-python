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




# Represents a single address for an invoice
class InvoiceAddressModel:
    invoiceAddressId: str
    groupKey: str
    invoiceId: str
    line1: str
    line2: str
    line3: str
    city: str
    region: str
    postalCode: str
    country: str
    latitude: float
    longitude: float
    created: str
    createdUserId: str
    modified: str
    modifiedUserId: str

