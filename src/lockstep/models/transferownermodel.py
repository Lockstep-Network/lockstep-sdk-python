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
from lockstep.models.useraccountmodel import UserAccountModel
from lockstep.models.useraccountmodel import UserAccountModel

"""
Model from the transfer ownership process.
"""
@dataclass
class TransferOwnerModel:
    previousOwner: UserAccountModel = None
    newOwner: UserAccountModel = None

