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
class PaymentDetailModel:
    """
    Contains detailed information about a Payment.
    """

    groupKey: object | None = None
    paymentId: object | None = None
    customerId: object | None = None
    customerName: object | None = None
    memoText: object | None = None
    referenceCode: object | None = None
    primaryContact: object | None = None
    email: object | None = None
    erpWriteStatus: object | None = None
    erpWriteStatusName: object | None = None
    currencyCode: object | None = None
    paymentAmount: object | None = None
    unappliedAmount: object | None = None
    baseCurrencyCode: object | None = None
    baseCurrencyPaymentAmount: object | None = None
    baseCurrencyUnappliedAmount: object | None = None
    paymentType: object | None = None
    tenderType: object | None = None
    paymentDate: object | None = None
    postDate: object | None = None
    phone: object | None = None
    fax: object | None = None
    address1: object | None = None
    address2: object | None = None
    address3: object | None = None
    city: object | None = None
    stateRegion: object | None = None
    postalCode: object | None = None
    countryCode: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
