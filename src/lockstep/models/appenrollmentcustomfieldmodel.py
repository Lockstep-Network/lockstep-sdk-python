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

    appEnrollmentId: object | None = None
    appId: object | None = None
    name: object | None = None
    appType: object | None = None
    groupKey: object | None = None
    customFieldDefinitionId: object | None = None
    customFieldLabel: object | None = None
    dataType: object | None = None
    sortOrder: object | None = None
    stringValue: object | None = None
    numericValue: object | None = None
    value: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
