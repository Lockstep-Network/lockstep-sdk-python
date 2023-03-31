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
from lockstep.models.emailreplygeneratorsuggestions import EmailReplyGeneratorSuggestions

@dataclass
class EmailReplyGeneratorResponse:
    """
    Represents the response from SAGE GMS API
    """

    message_id: str | None = None
    suggestions: list[EmailReplyGeneratorSuggestions] | None = None

