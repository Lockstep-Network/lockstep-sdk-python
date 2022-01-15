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
from lockstep.models.notemodel import NoteModel
from lockstep.models.attachmentmodel import AttachmentModel
from lockstep.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from lockstep.models.customfieldvaluemodel import CustomFieldValueModel

"""
A Contact contains information about a person or role within a Company. 
You can use Contacts to track information about who is responsible for a 
specific project, who handles invoices, or information about which role 
at a particular customer or vendor you should speak with about invoices.
"""
@dataclass
class ContactModel:
    contactId: str = None
    companyId: str = None
    groupKey: str = None
    erpKey: str = None
    contactName: str = None
    contactCode: str = None
    title: str = None
    roleCode: str = None
    emailAddress: str = None
    phone: str = None
    fax: str = None
    address1: str = None
    address2: str = None
    address3: str = None
    city: str = None
    stateRegion: str = None
    postalCode: str = None
    countryCode: str = None
    isActive: bool = None
    webpageUrl: str = None
    pictureUrl: str = None
    created: str = None
    createdUserId: str = None
    modified: str = None
    modifiedUserId: str = None
    appEnrollmentId: str = None
    notes: list[NoteModel] = None
    attachments: list[AttachmentModel] = None
    customFieldDefinitions: list[CustomFieldDefinitionModel] = None
    customFieldValues: list[CustomFieldValueModel] = None

