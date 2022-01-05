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


from dataclasses import dataclass
from src.models.notemodel import NoteModel
from src.models.attachmentmodel import AttachmentModel
from src.models.customfieldvaluemodel import CustomFieldValueModel
from src.models.codedefinitionmodel import CodeDefinitionModel

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
    userId: str
    groupKey: str
    userName: str
    email: str
    status: str
    created: str
    createdUserId: str
    modified: str
    modifiedUserId: str
    modifiedUserName: str
    b2CUserId: str
    userRole: str
    inviteSent: str
    phoneNumber: str
    faxNumber: str
    title: str
    accountingRoleCodeDefId: str
    address1: str
    address2: str
    address3: str
    city: str
    stateRegion: str
    postalCode: str
    country: str
    imageURL: str
    description: str
    b2CLastLoggedIn: str
    defaultCurrencyCode: str
    notes: list[NoteModel]
    attachments: list[AttachmentModel]
    customFieldValues: list[CustomFieldValueModel]
    accountingRoleCodeDefinition: CodeDefinitionModel

