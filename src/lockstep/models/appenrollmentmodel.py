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

    appEnrollmentId: object | None = None
    appId: object | None = None
    groupKey: object | None = None
    isActive: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None
    cronSettings: object | None = None
    syncScheduleIsActive: object | None = None
    isDeleted: object | None = None
    app: object | None = None
    customFieldDefinitions: list[object] | None = None
    customFieldValues: list[object] | None = None
    lastSync: object | None = None
    lastSuccessfulSync: object | None = None
    connectorInfo: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
