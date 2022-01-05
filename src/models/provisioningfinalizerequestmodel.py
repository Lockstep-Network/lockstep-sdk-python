#
# Lockstep Software Development Kit for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Ted Spence <tspence@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @version    2021.39
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass
from src.models.companymodel import CompanyModel
from src.models.erpinfomodel import ErpInfoModel

"""
Represents the data to finalize onboarding for a user
"""
@dataclass
class ProvisioningFinalizeRequestModel:
    fullName: str
    timeZone: str
    defaultCurrency: str
    company: CompanyModel
    emailConnector: ErpInfoModel

