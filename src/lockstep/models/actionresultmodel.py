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
class ActionResultModel:
    """
    Represents the result of an action.

    In the Lockstep API, an Action is returned when an API call does not
    produce any data but does produce messages that can be useful in
    understanding what work was performed. You may use the messages text
    to display user visible error messages or the results of various
    operations.
    """

    messages: list[object] | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
