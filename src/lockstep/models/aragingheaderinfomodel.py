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
class ArAgingHeaderInfoModel:
    """
    Aggregated Accounts Receivable Aging information.
    """

    groupKey: str | None = None
    reportBucket: str | None = None
    totalCustomers: int | None = None
    totalInvoicesOutstanding: int | None = None
    totalInvoiceOutstandingAmount: float | None = None
    totalCreditMemoOutstandingAmount: float | None = None
    totalUnappliedPaymentAmount: float | None = None
    totalOutstandingAmount: float | None = None
    totalArAmount: float | None = None
    percentageOfTotalAr: float | None = None

