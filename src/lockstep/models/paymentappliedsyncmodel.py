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
class PaymentAppliedSyncModel:
    """
    The PaymentAppliedSyncModel represents information coming into
    Lockstep from an external financial system or other enterprise
    resource planning system. To import data from an external system,
    convert your original data into the PaymentAppliedSyncModel format
    and call the [Upload Sync File API](https://developer.lockstep.io/reference/post_api-v1-sync-zip).
    This API retrieves all of the data you uploaded in a compressed ZIP
    file and imports it into the Lockstep platform. Once imported, this
    record will be available in the Lockstep API as a
    [PaymentAppliedModel](https://developer.lockstep.io/docs/paymentappliedmodel).
    For more information on writing your own connector, see [Connector
    Data](https://developer.lockstep.io/docs/connector-data).
    """

    onMatchAction: object | None = None
    erpKey: object | None = None
    invoiceErpKey: object | None = None
    paymentErpKey: object | None = None
    entryNumber: object | None = None
    applyToInvoiceDate: object | None = None
    paymentAppliedAmount: object | None = None
    created: object | None = None
    modified: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
