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
class ContactModel:
    """
    A Contact contains information about a person or role within a
    Company. You can use Contacts to track information about who is
    responsible for a specific project, who handles invoices, or
    information about which role at a particular customer or vendor you
    should speak with about invoices.
    """

    contactId: object | None = None
    companyId: object | None = None
    groupKey: object | None = None
    erpKey: object | None = None
    contactName: object | None = None
    contactCode: object | None = None
    title: object | None = None
    roleCode: object | None = None
    emailAddress: object | None = None
    phone: object | None = None
    fax: object | None = None
    address1: object | None = None
    address2: object | None = None
    address3: object | None = None
    city: object | None = None
    stateRegion: object | None = None
    postalCode: object | None = None
    countryCode: object | None = None
    isActive: object | None = None
    webpageUrl: object | None = None
    pictureUrl: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None
    appEnrollmentId: object | None = None
    notes: list[object] | None = None
    attachments: list[object] | None = None
    customFieldDefinitions: list[object] | None = None
    customFieldValues: list[object] | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
