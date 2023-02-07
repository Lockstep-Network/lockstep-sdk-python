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
class AccountingProfileRequest:
    """
    An Accounting Profile is a child of a Company Profile, and
    collectively, they comprise the identity and necessary information
    for an accounting team to work with trading partners, financial
    institutions, auditors, and others. You can use Accounting Profiles
    to define an accounting function by what the function does and how
    to interface with the function.
    """

    accountingProfileId: str | None = None
    companyId: str | None = None
    groupKey: str | None = None
    name: str | None = None
    type: str | None = None
    emailAddress: str | None = None
    phone: str | None = None
    address1: str | None = None
    address2: str | None = None
    address3: str | None = None
    city: str | None = None
    region: str | None = None
    postalCode: str | None = None
    country: str | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None
    notes: list[NoteModel] | None = None
    attachments: list[AttachmentModel] | None = None
    customFieldDefinitions: list[CustomFieldDefinitionModel] | None = None
    customFieldValues: list[CustomFieldValueModel] | None = None
    primaryContactId: str | None = None

