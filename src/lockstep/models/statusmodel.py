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
class StatusModel:
    """
    Represents the status of a user's credentials
    """

    userName: object | None = None
    emailAddress: object | None = None
    accountName: object | None = None
    accountCompanyId: object | None = None
    userId: object | None = None
    groupKey: object | None = None
    loggedIn: object | None = None
    errorMessage: object | None = None
    roles: list[object] | None = None
    lastLoggedIn: object | None = None
    apiKeyId: object | None = None
    userStatus: object | None = None
    environment: object | None = None
    version: object | None = None
    onboardingScheduled: object | None = None
    baseCurrencyCode: object | None = None
    countryCode: object | None = None
    magicLinkId: object | None = None
    magicLinkCompanyId: object | None = None
    magicLink: object | None = None
    supportAccess: object | None = None
    isImpersonated: object | None = None
    userGroups: list[object] | None = None
    dependencies: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
