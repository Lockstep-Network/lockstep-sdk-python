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

    onMatchAction: object | None = None
    erpKey: object | None = None
    companyErpKey: object | None = None
    customerErpKey: object | None = None
    salespersonName: object | None = None
    purchaseOrderCode: object | None = None
    referenceCode: object | None = None
    salespersonCode: object | None = None
    invoiceTypeCode: object | None = None
    invoiceStatusCode: object | None = None
    termsCode: object | None = None
    specialTerms: object | None = None
    currencyCode: object | None = None
    totalAmount: object | None = None
    salesTaxAmount: object | None = None
    discountAmount: object | None = None
    outstandingBalanceAmount: object | None = None
    invoiceDate: object | None = None
    discountDate: object | None = None
    postedDate: object | None = None
    invoiceClosedDate: object | None = None
    paymentDueDate: object | None = None
    importedDate: object | None = None
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
    isVoided: object | None = None
    inDispute: object | None = None
    preferredDeliveryMethod: object | None = None
    currencyRate: object | None = None
    baseCurrencyTotalAmount: object | None = None
    baseCurrencySalesTaxAmount: object | None = None
    baseCurrencyDiscountAmount: object | None = None
    baseCurrencyOutstandingBalanceAmount: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
