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
class TransactionSummaryTotalModel:
    """
    Represents transaction summary information based on the query
    request within the group account.
    """

    totalCount: int | None = None
    totalAmount: float | None = None
    outstandingAmount: float | None = None
    invoiceOpenCount: int | None = None
    invoicePastDueCount: int | None = None

