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
from lockstep.models.applicationmodel import ApplicationModel
from lockstep.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from lockstep.models.customfieldvaluemodel import CustomFieldValueModel
from lockstep.models.syncrequestmodel import SyncRequestModel
from lockstep.models.syncrequestmodel import SyncRequestModel
from lockstep.models.connectorinfomodel import ConnectorInfoModel

@dataclass
class AppEnrollmentModel:
    """
    An AppEnrollment represents an app that has been enrolled to the
    current account. When you sign up for an app using the Lockstep
    Platform, you obtain an enrollment record for that app. Example
    types of apps include connectors and feature enhancement apps. The
    App Enrollment object contains information about this app, its
    configuration, and settings. See [Applications and
    Enrollments](https://developer.lockstep.io/docs/applications-and-enrollments)
    for more information.
    """

    appEnrollmentId: str | None = None
    appId: str | None = None
    groupKey: str | None = None
    isActive: bool | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None
    cronSettings: str | None = None
    syncScheduleIsActive: bool | None = None
    isDeleted: bool | None = None
    app: ApplicationModel | None = None
    customFieldDefinitions: list[CustomFieldDefinitionModel] | None = None
    customFieldValues: list[CustomFieldValueModel] | None = None
    lastSync: SyncRequestModel | None = None
    lastSuccessfulSync: SyncRequestModel | None = None
    connectorInfo: ConnectorInfoModel | None = None

