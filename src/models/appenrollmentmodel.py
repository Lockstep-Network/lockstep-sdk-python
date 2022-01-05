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



from src.models.applicationmodel import ApplicationModel
from src.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from src.models.customfieldvaluemodel import CustomFieldValueModel
from src.models.syncrequestmodel import SyncRequestModel
from src.models.erpinfodatamodel import ErpInfoDataModel
from src.models.connectorinfomodel import ConnectorInfoModel

"""
An AppEnrollment represents an app that has been enrolled to the current
account. When you sign up for an app using the Lockstep Platform, you
obtain an enrollment record for that app. Example types of apps include
connectors and feature enhancement apps. The App Enrollment object
contains information about this app, its configuration, and settings.
See [Applications and
Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments)
for more information.
"""
class AppEnrollmentModel:
    appEnrollmentId: str
    appId: str
    groupKey: str
    isActive: bool
    created: str
    createdUserId: str
    modified: str
    modifiedUserId: str
    cronSettings: str
    syncScheduleIsActive: bool
    app: ApplicationModel
    customFieldDefinitions: list[CustomFieldDefinitionModel]
    customFieldValues: list[CustomFieldValueModel]
    lastSync: SyncRequestModel
    erpInfo: ErpInfoDataModel
    connectorInfo: ConnectorInfoModel

