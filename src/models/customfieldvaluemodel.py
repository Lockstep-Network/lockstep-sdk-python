#
# Lockstep Software Development Kit for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Ted Spence <tspence@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @version    2021.39
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#



from src.models.customfielddefinitionmodel import CustomFieldDefinitionModel

"""
A Custom Field represents metadata added to an object within the Lockstep Platform.  Lockstep provides a
core definition for each object.  The core definition is intended to represent a level of compatibility
that provides support across most accounting systems and products.  When a user or developer requires
information beyond this core definition, you can use Custom Fields to represent this information.

See [Extensibility](https://developer.lockstep.io/docs/extensibility) for more information.
"""
class CustomFieldValueModel:
    groupKey: str
    customFieldDefinitionId: str
    recordKey: str
    stringValue: str
    numericValue: float
    created: str
    createdUserId: str
    modified: str
    modifiedUserId: str
    appEnrollmentId: str
    customFieldDefinition: CustomFieldDefinitionModel

