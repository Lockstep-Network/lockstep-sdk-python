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
class ApplicationModel:
    """
    An Application represents a feature available to customers within
    the Lockstep Platform. You can create Applications by working with
    your Lockstep business development manager and publish them on the
    platform so that customers can browse and find your Application on
    the Lockstep Platform Marketplace. When a customer adds an
    Application to their account, they obtain an AppEnrollment which
    represents that customer's instance of this Application. The
    customer-specific AppEnrollment contains a customer's configuration
    data for the Application, which is not customer-specific. See
    [Applications and Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments)
    for more information. --swaggerCategory:Platform
    """

    appId: str | None = None
    name: str | None = None
    description: str | None = None
    appType: str | None = None
    ownerId: str | None = None
    projectUrl: str | None = None
    iconUrl: str | None = None
    priceTerms: str | None = None
    createdUserId: str | None = None
    modifiedUserId: str | None = None
    created: str | None = None
    modified: str | None = None
    isActive: bool | None = None
    wikiURL: str | None = None
    groupKey: str | None = None
    b2CClientId: str | None = None
    notes: list[NoteModel] | None = None
    attachments: list[AttachmentModel] | None = None
    customFieldDefinitions: list[CustomFieldDefinitionModel] | None = None
    customFieldValues: list[CustomFieldValueModel] | None = None

