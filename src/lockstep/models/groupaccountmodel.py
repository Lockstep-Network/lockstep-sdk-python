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
class GroupAccountModel:
    """
    Represents an account for an entire group
    """

    groupKey: str | None = None
    groupName: str | None = None
    primaryUserId: str | None = None
    groupCompanyId: str | None = None
    baseCurrencyCode: str | None = None
    isActive: bool | None = None
    onboardingScheduled: bool | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None

