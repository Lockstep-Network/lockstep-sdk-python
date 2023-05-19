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
class WebhookHistoryTableStorageModel:
    """
    Represents the Webhook Trigger History
    """

    groupKey: object | None = None
    webhookId: object | None = None
    webhookHistoryId: object | None = None
    eventType: object | None = None
    requestSent: object | None = None
    isSuccessful: object | None = None
    responseStatusCode: object | None = None
    processResultMessage: object | None = None
    failureCount: object | None = None
    timestamp: object | None = None
    records: object | None = None
    requestMessage: object | None = None
    responseMessage: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
