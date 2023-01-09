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
class PaymentDetailHeaderModel:
    """
    Contains group level payment data.
    """

    groupKey: str | None = None
    baseCurrencyCode: str | None = None
    customerCount: int | None = None
    amountCollected: float | None = None
    unappliedAmount: float | None = None
    paidInvoiceCount: int | None = None
    openInvoiceCount: int | None = None

