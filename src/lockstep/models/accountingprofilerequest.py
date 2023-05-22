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
class AccountingProfileRequest:
    """
    An Accounting Profile is a child of a Company Profile, and
    collectively, they comprise the identity and necessary information
    for an accounting team to work with trading partners, financial
    institutions, auditors, and others. You can use Accounting Profiles
    to define an accounting function by what the function does and how
    to interface with the function.
    """

    accountingProfileId: object | None = None
    companyId: object | None = None
    groupKey: object | None = None
    name: object | None = None
    type: object | None = None
    emailAddress: object | None = None
    phone: object | None = None
    address1: object | None = None
    address2: object | None = None
    address3: object | None = None
    city: object | None = None
    region: object | None = None
    postalCode: object | None = None
    country: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None
    notes: list[object] | None = None
    attachments: list[object] | None = None
    customFieldDefinitions: list[object] | None = None
    customFieldValues: list[object] | None = None
    primaryContactId: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
