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
class UserGroupModel:
    """
    A UserGroup represents the groups that the user is a member of. A
    user may have varying permissions/access within a Group.
    """

    groupKey: object | None = None
    userRole: object | None = None
    groupName: object | None = None
    status: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
