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
class ApiKeyModel:
    """
    An API Key is an authentication token that you may use with the
    Lockstep API. Because API Keys do not have an expiration date, they
    are well suited for unattended processes. Each API Key is associated
    with a user, and may be revoked to prevent it from accessing the
    Lockstep API. When you create an API Key, make sure to save the
    value in a secure location. Lockstep cannot retrieve an API Key once
    it is created. For more information, see [API
    Keys](https://developer.lockstep.io/docs/api-keys).
    """

    apiKeyId: str | None = None
    groupKey: str | None = None
    name: str | None = None
    environment: str | None = None
    apiKey: str | None = None
    keyPrefix: str | None = None
    created: str | None = None
    createdUserId: str | None = None
    revoked: str | None = None
    revokedUserId: str | None = None
    expires: str | None = None

