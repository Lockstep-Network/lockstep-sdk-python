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



from src.models.emailmodel import EmailModel
from src.models.notemodel import NoteModel
from src.models.attachmentmodel import AttachmentModel
from src.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from src.models.customfieldvaluemodel import CustomFieldValueModel

"""
An Email represents a communication sent from one company to another.
The creator of the email is identified by the `CompanyId` field,
recipient(s) by the `EmailTo` field, and cc recipient(s) by the
'EmailCC' field. The Email Model represents an email and a number of
different metadata attributes related to the creation, storage, and
ownership of the email.
"""
class EmailModel:
    emailId: str
    threadId: str
    groupKey: str
    companyId: str
    emailFrom: str
    emailTo: str
    emailCC: str
    emailSubject: str
    emailBody: str
    sentDate: str
    isUnread: bool
    isPriority: bool
    isSpam: bool
    created: str
    createdUserId: str
    toBeSent: bool
    customerId: str
    receivedTimeStamp: str
    openedTimestamp: str
    viewCount: int
    appEnrollmentId: str
    externalEmailId: str
    externalThreadId: str
    emailBcc: str
    sendType: str
    modified: str
    modifiedUserId: str
    responseOriginId: str
    responseOrigin: EmailModel
    notes: list[NoteModel]
    attachments: list[AttachmentModel]
    customFieldDefinitions: list[CustomFieldDefinitionModel]
    customFieldValues: list[CustomFieldValueModel]

