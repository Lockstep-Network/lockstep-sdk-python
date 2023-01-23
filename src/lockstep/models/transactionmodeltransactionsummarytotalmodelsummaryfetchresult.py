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
from lockstep.models.transactionmodel import TransactionModel
from lockstep.models.transactionsummarytotalmodel import TransactionSummaryTotalModel
from lockstep.models.summaryagingtotalsmodel import SummaryAgingTotalsModel

@dataclass
class TransactionModelTransactionSummaryTotalModelSummaryFetchResult:

    totalCount: int | None = None
    pageSize: int | None = None
    pageNumber: int | None = None
    records: list[TransactionModel] | None = None
    summary: TransactionSummaryTotalModel | None = None
    agingSummary: list[SummaryAgingTotalsModel] | None = None

