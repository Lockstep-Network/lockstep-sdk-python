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
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

@dataclass
class CreditMemoAppliedSyncModel:
    """
    The CreditMemoAppliedSyncModel represents information coming into
    Lockstep from an external financial system or other enterprise
    resource planning system. To import data from an external system,
    convert your original data into the CreditMemoAppliedSyncModel
    format and call the [Upload Sync File
    API](https://developer.lockstep.io/reference/post_api-v1-sync-zip).
    This API retrieves all of the data you uploaded in a compressed ZIP
    file and imports it into the Lockstep platform. Once imported, this
    record will be available in the Lockstep API as a
    [CreditMemoAppliedModel](https://developer.lockstep.io/docs/creditmemoappliedmodel).
    For more information on writing your own connector, see [Connector
    Data](https://developer.lockstep.io/docs/connector-data).
    """

    erpKey: str = None
    invoiceErpKey: str = None
    creditMemoInvoiceErpKey: str = None
    entryNumber: int = None
    applyToInvoiceDate: str = None
    creditMemoAppliedAmount: float = None
    created: str = None
    modified: str = None

