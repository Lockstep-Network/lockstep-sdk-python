#
# Lockstep Platform SDK for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass
from lockstep.models.companymodel import CompanyModel
from lockstep.models.erpinfomodel import ErpInfoModel

@dataclass
class ProvisioningFinalizeRequestModel:
    """
    Represents the data to finalize onboarding for a user
    """

    fullName: str | None = None
    timeZone: str | None = None
    defaultCurrency: str | None = None
    company: CompanyModel | None = None
    emailConnector: ErpInfoModel | None = None

