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

    webhookRuleId: str | None = None
    webhookId: str | None = None
    groupKey: str | None = None
    tableKey: str | None = None
    eventType: str | None = None
    filter: str | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None

