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
class ErrorResult:
    """
    Represents a failed API request.
    """

    type: object | None = None
    title: object | None = None
    status: object | None = None
    detail: object | None = None
    instance: object | None = None
    content: object | None = None

    @classmethod
    def from_json(cls, data: dict):
        obj = cls()
        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return obj
    def to_dict(self) -> dict:
        return dataclass.asdict(self)
