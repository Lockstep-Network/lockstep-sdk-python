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
class FinancialYearSettingModel:
    """
    A Financial Year Setting is used to to set the type, beginning, end,
    and number of periods of a year used to calculate accounting
    reports. The financial setting can either be for a specific app
    enrollment id via a sync or, when the financial year setting is
    manually created, will cover all account data without an app
    enrollment id.
    """

    financialYearSettingId: object | None = None
    groupKey: object | None = None
    appEnrollmentId: object | None = None
    yearType: object | None = None
    totalPeriods: object | None = None
    startDate: object | None = None
    endDate: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
