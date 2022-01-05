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



from src.models.notemodel import NoteModel
from src.models.attachmentmodel import AttachmentModel
from src.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from src.models.customfieldvaluemodel import CustomFieldValueModel

"""
A Contact contains information about a person or role within a Company.
You can use Contacts to track information about who is responsible for a
specific project, who handles invoices, or information about which role
at a particular customer or vendor you should speak with about invoices.
"""
class ContactModel:
    contactId: str
    companyId: str
    groupKey: str
    erpKey: str
    contactName: str
    contactCode: str
    title: str
    roleCode: str
    emailAddress: str
    phone: str
    fax: str
    address1: str
    address2: str
    address3: str
    city: str
    stateRegion: str
    postalCode: str
    countryCode: str
    isActive: bool
    webpageUrl: str
    pictureUrl: str
    created: str
    createdUserId: str
    modified: str
    modifiedUserId: str
    appEnrollmentId: str
    notes: list[NoteModel]
    attachments: list[AttachmentModel]
    customFieldDefinitions: list[CustomFieldDefinitionModel]
    customFieldValues: list[CustomFieldValueModel]

