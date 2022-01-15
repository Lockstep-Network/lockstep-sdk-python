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
An Email represents a communication sent from one company to another. 
The creator of the email is identified by the `CompanyId` field, 
recipient(s) by the `EmailTo` field, and cc recipient(s) by the 
'EmailCC' field. The Email Model represents an email and a number of 
different metadata attributes related to the creation, storage, and 
ownership of the email.
"""
@dataclass
class EmailModel:
    emailId: str = None
    threadId: str = None
    groupKey: str = None
    companyId: str = None
    emailFrom: str = None
    emailTo: str = None
    emailCC: str = None
    emailSubject: str = None
    emailBody: str = None
    sentDate: str = None
    isUnread: bool = None
    isPriority: bool = None
    isSpam: bool = None
    created: str = None
    createdUserId: str = None
    toBeSent: bool = None
    customerId: str = None
    receivedTimeStamp: str = None
    openedTimestamp: str = None
    viewCount: int = None
    appEnrollmentId: str = None
    externalEmailId: str = None
    externalThreadId: str = None
    emailBcc: str = None
    sendType: str = None
    modified: str = None
    modifiedUserId: str = None
    responseOriginId: str = None
    responseOrigin: 'EmailModel' = None
    notes: list[NoteModel] = None
    attachments: list[AttachmentModel] = None
    customFieldDefinitions: list[CustomFieldDefinitionModel] = None
    customFieldValues: list[CustomFieldValueModel] = None

