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
from lockstep.models.customfieldvaluemodel import CustomFieldValueModel
from lockstep.models.codedefinitionmodel import CodeDefinitionModel

"""
A User represents a person who has the ability to authenticate against 
the Lockstep Platform and use services such as Lockstep Insights. A User 
is uniquely identified by an Azure identity, and each user must have an 
email address defined within their account. All Users must validate 
their email to make use of Lockstep platform services. Users may have 
different privileges and access control rights within the Lockstep 
Platform.
"""
@dataclass
class UserAccountModel:
    userId: str = None
    groupKey: str = None
    userName: str = None
    email: str = None
    status: str = None
    created: str = None
    createdUserId: str = None
    modified: str = None
    modifiedUserId: str = None
    modifiedUserName: str = None
    b2CUserId: str = None
    userRole: str = None
    inviteSent: str = None
    phoneNumber: str = None
    faxNumber: str = None
    title: str = None
    accountingRoleCodeDefId: str = None
    address1: str = None
    address2: str = None
    address3: str = None
    city: str = None
    stateRegion: str = None
    postalCode: str = None
    country: str = None
    imageURL: str = None
    description: str = None
    b2CLastLoggedIn: str = None
    defaultCurrencyCode: str = None
    notes: list[NoteModel] = None
    attachments: list[AttachmentModel] = None
    customFieldValues: list[CustomFieldValueModel] = None
    accountingRoleCodeDefinition: CodeDefinitionModel = None

