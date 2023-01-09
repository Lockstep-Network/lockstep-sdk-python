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
from lockstep.models.notemodel import NoteModel
from lockstep.models.attachmentmodel import AttachmentModel
from lockstep.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from lockstep.models.customfieldvaluemodel import CustomFieldValueModel

@dataclass
class ContactModel:
    """
    A Contact contains information about a person or role within a
    Company. You can use Contacts to track information about who is
    responsible for a specific project, who handles invoices, or
    information about which role at a particular customer or vendor you
    should speak with about invoices.
    """

    contactId: str | None = None
    companyId: str | None = None
    groupKey: str | None = None
    erpKey: str | None = None
    contactName: str | None = None
    contactCode: str | None = None
    title: str | None = None
    roleCode: str | None = None
    emailAddress: str | None = None
    phone: str | None = None
    fax: str | None = None
    address1: str | None = None
    address2: str | None = None
    address3: str | None = None
    city: str | None = None
    stateRegion: str | None = None
    postalCode: str | None = None
    countryCode: str | None = None
    isActive: bool | None = None
    webpageUrl: str | None = None
    pictureUrl: str | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None
    appEnrollmentId: str | None = None
    notes: list[NoteModel] | None = None
    attachments: list[AttachmentModel] | None = None
    customFieldDefinitions: list[CustomFieldDefinitionModel] | None = None
    customFieldValues: list[CustomFieldValueModel] | None = None

