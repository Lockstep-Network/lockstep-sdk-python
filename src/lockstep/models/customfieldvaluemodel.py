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
class CustomFieldValueModel:
    """
    A Custom Field represents metadata added to an object within the
    Lockstep Platform. Lockstep provides a core definition for each
    object. The core definition is intended to represent a level of
    compatibility that provides support across most accounting systems
    and products. When a user or developer requires information beyond
    this core definition, you can use Custom Fields to represent this
    information. See [Extensibility](https://developer.lockstep.io/docs/extensibility)
    for more information.
    """

    groupKey: object | None = None
    customFieldDefinitionId: object | None = None
    recordKey: object | None = None
    tableKey: object | None = None
    customFieldLabel: object | None = None
    dataType: object | None = None
    stringValue: object | None = None
    numericValue: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None
    appEnrollmentId: object | None = None
    value: object | None = None
    customFieldDefinition: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
