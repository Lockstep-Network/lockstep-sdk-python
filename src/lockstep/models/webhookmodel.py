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
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

@dataclass
class WebhookModel:
    """
    A Webhook is a subscription to receive notifications automatically
    to the supplied callback url when changes are made to a supported
    object. Currently supported objects: * `SyncRequest` - Receive a
    notification when a new sync request has completed for the group
    key.
    """

    webhookId: str = None
    groupKey: str = None
    name: str = None
    statusCode: str = None
    statusMessage: str = None
    clientSecret: str = None
    requestContentType: str = None
    callbackHttpMethod: str = None
    callbackUrl: str = None
    expirationDate: str = None
    retryCount: int = None
    created: str = None
    createdUserId: str = None
    modified: str = None
    modifiedUserId: str = None

