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
class InvoiceSyncModel:
    """
    The InvoiceSyncModel represents information coming into Lockstep
    from an external financial system or other enterprise resource
    planning system. To import data from an external system, convert
    your original data into the InvoiceSyncModel format and call the
    [Upload Sync File API](https://developer.lockstep.io/reference/post_api-v1-sync-zip).
    This API retrieves all of the data you uploaded in a compressed ZIP
    file and imports it into the Lockstep platform. Once imported, this
    record will be available in the Lockstep API as an
    [InvoiceModel](https://developer.lockstep.io/docs/invoicemodel). For
    more information on writing your own connector, see [Connector
    Data](https://developer.lockstep.io/docs/connector-data).
    """

    erpKey: str = None
    companyErpKey: str = None
    customerErpKey: str = None
    salespersonName: str = None
    purchaseOrderCode: str = None
    referenceCode: str = None
    salespersonCode: str = None
    invoiceTypeCode: str = None
    invoiceStatusCode: str = None
    termsCode: str = None
    specialTerms: str = None
    currencyCode: str = None
    totalAmount: float = None
    salesTaxAmount: float = None
    discountAmount: float = None
    outstandingBalanceAmount: float = None
    invoiceDate: str = None
    discountDate: str = None
    postedDate: str = None
    invoiceClosedDate: str = None
    paymentDueDate: str = None
    importedDate: str = None
    originAddressLine1: str = None
    originAddressLine2: str = None
    originAddressLine3: str = None
    originAddressCity: str = None
    originAddressRegion: str = None
    originAddressPostalCode: str = None
    originAddressCountry: str = None
    originAddressLatitude: float = None
    originAddressLongitude: float = None
    billToAddressLine1: str = None
    billToAddressLine2: str = None
    billToAddressLine3: str = None
    billToAddressCity: str = None
    billToAddressRegion: str = None
    billToAddressPostalCode: str = None
    billToAddressCountry: str = None
    billToAddressLatitude: float = None
    billToAddressLongitude: float = None
    shipToAddressLine1: str = None
    shipToAddressLine2: str = None
    shipToAddressLine3: str = None
    shipToAddressCity: str = None
    shipToAddressRegion: str = None
    shipToAddressPostalCode: str = None
    shipToAddressCountry: str = None
    shipToAddressLatitude: float = None
    shipToAddressLongitude: float = None
    created: str = None
    modified: str = None
    isVoided: bool = None
    inDispute: bool = None

