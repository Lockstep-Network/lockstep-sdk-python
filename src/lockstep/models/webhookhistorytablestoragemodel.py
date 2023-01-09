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

    groupKey: str | None = None
    webhookId: str | None = None
    webhookHistoryId: str | None = None
    eventType: str | None = None
    requestSent: bool | None = None
    isSuccessful: bool | None = None
    responseStatusCode: str | None = None
    processResultMessage: str | None = None
    failureCount: int | None = None
    timestamp: str | None = None
    records: str | None = None
    requestMessage: str | None = None
    responseMessage: str | None = None

