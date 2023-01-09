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
class AppEnrollmentCustomFieldModel:
    """
    App enrollment and custom field merged into one
    """

    appEnrollmentId: str | None = None
    appId: str | None = None
    name: str | None = None
    appType: str | None = None
    groupKey: str | None = None
    customFieldDefinitionId: str | None = None
    customFieldLabel: str | None = None
    dataType: str | None = None
    sortOrder: int | None = None
    stringValue: str | None = None
    numericValue: float | None = None
    value: str | None = None

