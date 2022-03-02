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
class WebhookHistoryTableStorageModel:
    """
    Represents the Webhook Trigger History
    """

    groupKey: str = None
    webhookId: str = None
    webhookHistoryId: str = None
    eventType: str = None
    requestSent: bool = None
    isSuccessful: bool = None
    responseStatusCode: str = None
    processResultMessage: str = None
    failureCount: int = None
    timestamp: str = None

