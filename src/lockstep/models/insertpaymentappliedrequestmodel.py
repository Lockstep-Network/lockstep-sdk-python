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
class InsertPaymentAppliedRequestModel:
    """
    A request to insert a payment application
    """

    paymentAppliedId: object | None = None
    invoiceId: object | None = None
    paymentId: object | None = None
    erpKey: object | None = None
    invoiceErpKey: object | None = None
    applyToInvoiceDate: object | None = None
    paymentAppliedAmount: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
