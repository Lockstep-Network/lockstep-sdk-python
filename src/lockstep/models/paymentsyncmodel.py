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
class PaymentSyncModel:
    """
    The PaymentSyncModel represents information coming into Lockstep
    from an external financial system or other enterprise resource
    planning system. To import data from an external system, convert
    your original data into the PaymentSyncModel format and call the
    [Upload Sync File API](https://developer.lockstep.io/reference/post_api-v1-sync-zip).
    This API retrieves all of the data you uploaded in a compressed ZIP
    file and imports it into the Lockstep platform. Once imported, this
    record will be available in the Lockstep API as a
    [PaymentModel](https://developer.lockstep.io/docs/paymentmodel). For
    more information on writing your own connector, see [Connector
    Data](https://developer.lockstep.io/docs/connector-data).
    """

    onMatchAction: object | None = None
    networkId: object | None = None
    erpKey: object | None = None
    companyErpKey: object | None = None
    companyNetworkId: object | None = None
    paymentType: object | None = None
    tenderType: object | None = None
    isOpen: object | None = None
    memoText: object | None = None
    paymentDate: object | None = None
    postDate: object | None = None
    paymentAmount: object | None = None
    unappliedAmount: object | None = None
    currencyCode: object | None = None
    created: object | None = None
    modified: object | None = None
    referenceCode: object | None = None
    isVoided: object | None = None
    inDispute: object | None = None
    currencyRate: object | None = None
    baseCurrencyPaymentAmount: object | None = None
    baseCurrencyUnappliedAmount: object | None = None
    bankAccountId: object | None = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
