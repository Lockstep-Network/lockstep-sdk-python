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

    erpKey: str | None = None
    companyErpKey: str | None = None
    customerErpKey: str | None = None
    salespersonName: str | None = None
    purchaseOrderCode: str | None = None
    referenceCode: str | None = None
    salespersonCode: str | None = None
    invoiceTypeCode: str | None = None
    invoiceStatusCode: str | None = None
    termsCode: str | None = None
    specialTerms: str | None = None
    currencyCode: str | None = None
    totalAmount: float | None = None
    salesTaxAmount: float | None = None
    discountAmount: float | None = None
    outstandingBalanceAmount: float | None = None
    invoiceDate: str | None = None
    discountDate: str | None = None
    postedDate: str | None = None
    invoiceClosedDate: str | None = None
    paymentDueDate: str | None = None
    importedDate: str | None = None
    originAddressLine1: str | None = None
    originAddressLine2: str | None = None
    originAddressLine3: str | None = None
    originAddressCity: str | None = None
    originAddressRegion: str | None = None
    originAddressPostalCode: str | None = None
    originAddressCountry: str | None = None
    originAddressLatitude: float | None = None
    originAddressLongitude: float | None = None
    billToAddressLine1: str | None = None
    billToAddressLine2: str | None = None
    billToAddressLine3: str | None = None
    billToAddressCity: str | None = None
    billToAddressRegion: str | None = None
    billToAddressPostalCode: str | None = None
    billToAddressCountry: str | None = None
    billToAddressLatitude: float | None = None
    billToAddressLongitude: float | None = None
    shipToAddressLine1: str | None = None
    shipToAddressLine2: str | None = None
    shipToAddressLine3: str | None = None
    shipToAddressCity: str | None = None
    shipToAddressRegion: str | None = None
    shipToAddressPostalCode: str | None = None
    shipToAddressCountry: str | None = None
    shipToAddressLatitude: float | None = None
    shipToAddressLongitude: float | None = None
    created: str | None = None
    modified: str | None = None
    isVoided: bool | None = None
    inDispute: bool | None = None
    preferredDeliveryMethod: str | None = None
    currencyRate: float | None = None
    baseCurrencyTotalAmount: float | None = None
    baseCurrencySalesTaxAmount: float | None = None
    baseCurrencyDiscountAmount: float | None = None
    baseCurrencyOutstandingBalanceAmount: float | None = None

