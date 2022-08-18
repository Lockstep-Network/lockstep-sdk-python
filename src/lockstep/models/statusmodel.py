#
# Lockstep Platform SDK for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass
from lockstep.models.usergroupmodel import UserGroupModel

@dataclass
class StatusModel:
    """
    Represents the status of a user's credentials
    """

    userName: str | None = None
    accountName: str | None = None
    accountCompanyId: str | None = None
    userId: str | None = None
    groupKey: str | None = None
    loggedIn: bool | None = None
    errorMessage: str | None = None
    roles: list[str] | None = None
    lastLoggedIn: str | None = None
    apiKeyId: str | None = None
    userStatus: str | None = None
    environment: str | None = None
    version: str | None = None
    onboardingScheduled: bool | None = None
    dependencies: object | None = None
    userGroups: list[UserGroupModel] | None = None

