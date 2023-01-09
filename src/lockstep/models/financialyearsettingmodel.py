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

    financialYearSettingId: str | None = None
    groupKey: str | None = None
    appEnrollmentId: str | None = None
    yearType: str | None = None
    totalPeriods: int | None = None
    startDate: str | None = None
    endDate: str | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None

