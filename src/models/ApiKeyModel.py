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




# An API Key is an authentication token that you may use with the Lockstep API.  Because API Keys
# do not have an expiration date, they are well suited for unattended processes.  Each API Key
# is associated with a user, and may be revoked to prevent it from accessing the Lockstep API.
# When you create an API Key, make sure to save the value in a secure location.  Lockstep cannot
# retrieve an API Key once it is created.
# 
# For more information, see [API Keys](https://developer.lockstep.io/docs/api-keys).
class ApiKeyModel:
    apiKeyId: str
    groupKey: str
    name: str
    apiKey: str
    keyPrefix: str
    created: str
    createdUserId: str
    revoked: str
    revokedUserId: str
    expires: str

