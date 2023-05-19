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
class InvoiceAddressModel:
    """
    Represents a single address for an invoice
    """

    invoiceAddressId: object | None = None
    groupKey: object | None = None
    invoiceId: object | None = None
    line1: object | None = None
    line2: object | None = None
    line3: object | None = None
    city: object | None = None
    region: object | None = None
    postalCode: object | None = None
    country: object | None = None
    latitude: object | None = None
    longitude: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None
    appEnrollmentId: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
