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
class CustomFieldSyncModel:
    """
    The CustomFieldSyncModel represents information coming into Lockstep
    from an external financial system or other enterprise resource
    planning system. [Custom Fields](https://developer.lockstep.io/docs/custom-fields#custom-fields)
    represent custom data extensions that you can use with the Lockstep
    Platform. If you need to store extra information about an object
    that does not match Lockstep's official schema, you can store it in
    the Custom Field system using CustomFieldSyncModel. To store a
    custom field for an object, create a CustomFieldSyncModel record
    containing the `TableKey` and `ErpKey` of the entity to which you
    will attach a custom field. Next specify the field's
    `CustomFieldLabel` and either a `StringValue` or `NumericValue`.
    Once imported, this record will be available in the Lockstep API as
    a [CustomFieldValueModel](https://developer.lockstep.io/docs/customfieldvaluemodel).
    For more information on writing your own connector, see [Connector
    Data](https://developer.lockstep.io/docs/connector-data).
    """

    onMatchAction: object | None = None
    erpKey: object | None = None
    tableKey: object | None = None
    customFieldLabel: object | None = None
    stringValue: object | None = None
    numericValue: object | None = None
    value: object | None = None
    created: object | None = None
    modified: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
