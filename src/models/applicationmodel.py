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
from src.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from src.models.customfieldvaluemodel import CustomFieldValueModel

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
    appId: str
    name: str
    description: str
    appType: str
    ownerId: str
    projectUrl: str
    iconUrl: str
    priceTerms: str
    createdUserId: str
    modifiedUserId: str
    created: str
    modified: str
    isActive: bool
    wikiURL: str
    groupKey: str
    notes: list[NoteModel]
    attachments: list[AttachmentModel]
    customFieldDefinitions: list[CustomFieldDefinitionModel]
    customFieldValues: list[CustomFieldValueModel]

