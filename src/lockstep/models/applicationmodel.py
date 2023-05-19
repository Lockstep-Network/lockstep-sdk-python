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

    appId: object | None = None
    name: object | None = None
    description: object | None = None
    appType: object | None = None
    ownerId: object | None = None
    projectUrl: object | None = None
    iconUrl: object | None = None
    createdUserId: object | None = None
    modifiedUserId: object | None = None
    created: object | None = None
    modified: object | None = None
    isActive: object | None = None
    groupKey: object | None = None
    b2CClientId: object | None = None
    notes: list[object] | None = None
    attachments: list[object] | None = None
    customFieldDefinitions: list[object] | None = None
    customFieldValues: list[object] | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
