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
class WebhookModel:
    """
    A Webhook is a subscription to receive notifications automatically
    to the supplied callback url when changes are made to a supported
    object. You will need to create at least one Webhook rule to receive
    notifications when a specific type of object is inserted, deleted,
    or updated.
    """

    webhookId: object | None = None
    groupKey: object | None = None
    name: object | None = None
    statusCode: object | None = None
    statusMessage: object | None = None
    clientSecret: object | None = None
    requestContentType: object | None = None
    callbackHttpMethod: object | None = None
    callbackUrl: object | None = None
    expirationDate: object | None = None
    retryCount: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None
    webhookRules: list[object] | None = None
    partitionKey: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
