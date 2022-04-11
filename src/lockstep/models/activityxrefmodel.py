#
# Lockstep Platform SDK for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

@dataclass
class ActivityXRefModel:
    """
    Represents links between an Activity and another record.
    """

    activityXRefId: str | None = None
    activityId: str | None = None
    groupKey: str | None = None
    tableKey: str | None = None
    objectKey: str | None = None

