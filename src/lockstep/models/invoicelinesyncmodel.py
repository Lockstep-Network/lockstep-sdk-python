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
class InvoiceLineSyncModel:
    """
    The InvoiceLineSyncModel represents information coming into Lockstep
    from an external financial system or other enterprise resource
    planning system. To import data from an external system, convert
    your original data into the InvoiceLineSyncModel format and call the
    [Upload Sync File API](https://developer.lockstep.io/reference/post_api-v1-sync-zip).
    This API retrieves all of the data you uploaded in a compressed ZIP
    file and imports it into the Lockstep platform. Once imported, this
    record will be available in the Lockstep API as an
    [InvoiceLineModel](https://developer.lockstep.io/docs/invoicelinemodel).
    For more information on writing your own connector, see [Connector
    Data](https://developer.lockstep.io/docs/connector-data).
    """

    onMatchAction: object | None = None
    erpKey: object | None = None
    invoiceErpKey: object | None = None
    lineNumber: object | None = None
    productCode: object | None = None
    description: object | None = None
    unitMeasureCode: object | None = None
    unitPrice: object | None = None
    quantity: object | None = None
    quantityShipped: object | None = None
    quantityReceived: object | None = None
    totalAmount: object | None = None
    exemptionCode: object | None = None
    reportingDate: object | None = None
    originAddressLine1: object | None = None
    originAddressLine2: object | None = None
    originAddressLine3: object | None = None
    originAddressCity: object | None = None
    originAddressRegion: object | None = None
    originAddressPostalCode: object | None = None
    originAddressCountry: object | None = None
    originAddressLatitude: object | None = None
    originAddressLongitude: object | None = None
    billToAddressLine1: object | None = None
    billToAddressLine2: object | None = None
    billToAddressLine3: object | None = None
    billToAddressCity: object | None = None
    billToAddressRegion: object | None = None
    billToAddressPostalCode: object | None = None
    billToAddressCountry: object | None = None
    billToAddressLatitude: object | None = None
    billToAddressLongitude: object | None = None
    shipToAddressLine1: object | None = None
    shipToAddressLine2: object | None = None
    shipToAddressLine3: object | None = None
    shipToAddressCity: object | None = None
    shipToAddressRegion: object | None = None
    shipToAddressPostalCode: object | None = None
    shipToAddressCountry: object | None = None
    shipToAddressLatitude: object | None = None
    shipToAddressLongitude: object | None = None
    created: object | None = None
    modified: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
