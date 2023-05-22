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
class EmailReplyGeneratorSuggestions:
    """
    Represents the email reply suggestion from the SAGE GMS API
    """

    kind: object | None = None
    body: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
