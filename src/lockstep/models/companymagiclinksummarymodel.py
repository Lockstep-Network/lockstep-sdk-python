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
class CompanyMagicLinkSummaryModel:
    """
    A summary of companies combined with their most recent magic links
    """

    companyId: object | None = None
    companyName: object | None = None
    companyType: object | None = None
    groupKey: object | None = None
    primaryContactName: object | None = None
    primaryContactEmailAddress: object | None = None
    pointOfContact: object | None = None
    outstandingAmount: object | None = None
    totalOpenInvoices: object | None = None
    pastDue: object | None = None
    totalVisits: object | None = None
    linksSent: object | None = None
    latestMagicLinkDate: object | None = None
    latestMagicLinkId: object | None = None
    latestMagicLinkStatus: object | None = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
