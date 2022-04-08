#
# Lockstep Platform SDK for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from __future__ import annotations
from dataclasses import dataclass
from lockstep.models.notemodel import NoteModel
from lockstep.models.attachmentmodel import AttachmentModel
from lockstep.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from lockstep.models.customfieldvaluemodel import CustomFieldValueModel

@dataclass
class EmailModel:
    """
    An Email represents a communication sent from one company to
    another. The creator of the email is identified by the `CompanyId`
    field, recipient(s) by the `EmailTo` field, and cc recipient(s) by
    the 'EmailCC' field. The Email Model represents an email and a
    number of different metadata attributes related to the creation,
    storage, and ownership of the email.
    """

    emailId: str | None = None
    threadId: str | None = None
    groupKey: str | None = None
    companyId: str | None = None
    emailFrom: str | None = None
    emailTo: str | None = None
    emailCC: str | None = None
    emailSubject: str | None = None
    emailBody: str | None = None
    sentDate: str | None = None
    isUnread: bool | None = None
    isPriority: bool | None = None
    isSpam: bool | None = None
    created: str | None = None
    createdUserId: str | None = None
    toBeSent: bool | None = None
    customerId: str | None = None
    receivedTimeStamp: str | None = None
    openedTimestamp: str | None = None
    viewCount: int | None = None
    appEnrollmentId: str | None = None
    externalEmailId: str | None = None
    externalThreadId: str | None = None
    emailBcc: str | None = None
    sendType: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None
    responseOriginId: str | None = None
    responseOrigin: EmailModel | None = None
    notes: list[NoteModel] | None = None
    attachments: list[AttachmentModel] | None = None
    customFieldDefinitions: list[CustomFieldDefinitionModel] | None = None
    customFieldValues: list[CustomFieldValueModel] | None = None

