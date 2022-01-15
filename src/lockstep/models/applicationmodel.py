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
An Application represents a feature available to customers within the 
Lockstep Platform. You can create Applications by working with your 
Lockstep business development manager and publish them on the platform 
so that customers can browse and find your Application on the Lockstep 
Platform Marketplace. When a customer adds an Application to their 
account, they obtain an AppEnrollment which represents that customer's 
instance of this Application. The customer-specific AppEnrollment 
contains a customer's configuration data for the Application, which is 
not customer-specific. See [Applications and 
Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments) 
for more information. --swaggerCategory:Platform
"""
@dataclass
class ApplicationModel:
    appId: str = None
    name: str = None
    description: str = None
    appType: str = None
    ownerId: str = None
    projectUrl: str = None
    iconUrl: str = None
    priceTerms: str = None
    createdUserId: str = None
    modifiedUserId: str = None
    created: str = None
    modified: str = None
    isActive: bool = None
    wikiURL: str = None
    groupKey: str = None
    notes: list[NoteModel] = None
    attachments: list[AttachmentModel] = None
    customFieldDefinitions: list[CustomFieldDefinitionModel] = None
    customFieldValues: list[CustomFieldValueModel] = None

