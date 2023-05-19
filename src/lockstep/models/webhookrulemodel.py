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
class WebhookRuleModel:
    """
    A Webhook Rule is a subscription to receive notifications whenever a
    specific event occurs. With the rule, you specify the Table and
    event you want to subscribe to. You can also optionally specify a
    filter to further refine the updates you want to receive.
    """

    webhookRuleId: object | None = None
    webhookId: object | None = None
    groupKey: object | None = None
    tableKey: object | None = None
    eventType: object | None = None
    filter: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
