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
class SyncEntityResultModel:
    """
    Contains information about a sync process for an entity.
    """

    insertCount: object | None = None
    updateCount: object | None = None
    deleteCount: object | None = None
    skipCount: object | None = None
    errorCount: object | None = None
    errors: object | None = None
    skips: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
