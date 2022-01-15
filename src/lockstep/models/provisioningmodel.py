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
# @version    2022.2
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass
from lockstep.models.erpinfomodel import ErpInfoModel
from lockstep.models.companymodel import CompanyModel

"""
Represents the data sent during the onboarding flow
"""
@dataclass
class ProvisioningModel:
    fullName: str = None
    timeZone: str = None
    defaultCurrency: str = None
    erp: ErpInfoModel = None
    company: CompanyModel = None

