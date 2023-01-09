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
from lockstep.models.customfieldvaluemodel import CustomFieldValueModel
from lockstep.models.codedefinitionmodel import CodeDefinitionModel

@dataclass
class UserAccountModel:
    """
    A User represents a person who has the ability to authenticate
    against the Lockstep Platform and use services such as Lockstep
    Inbox. A User is uniquely identified by an Azure identity, and each
    user must have an email address defined within their account. All
    Users must validate their email to make use of Lockstep platform
    services. Users may have different privileges and access control
    rights within the Lockstep Platform.
    """

    userId: str | None = None
    groupKey: str | None = None
    userName: str | None = None
    email: str | None = None
    status: str | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None
    modifiedUserName: str | None = None
    b2CUserId: str | None = None
    userRole: str | None = None
    inviteSent: str | None = None
    phoneNumber: str | None = None
    faxNumber: str | None = None
    title: str | None = None
    accountingRoleCodeDefId: str | None = None
    address1: str | None = None
    address2: str | None = None
    address3: str | None = None
    city: str | None = None
    stateRegion: str | None = None
    postalCode: str | None = None
    country: str | None = None
    timeZone: str | None = None
    imageURL: str | None = None
    description: str | None = None
    b2CLastLoggedIn: str | None = None
    defaultCurrencyCode: str | None = None
    notes: list[NoteModel] | None = None
    attachments: list[AttachmentModel] | None = None
    customFieldValues: list[CustomFieldValueModel] | None = None
    accountingRoleCodeDefinition: CodeDefinitionModel | None = None

