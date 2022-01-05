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




"""
Represents a Code Definition.  Codes can be used as shortened, human readable strings.
Additionally, this table can be used to store lists of system values for Lockstep objects.
"""
class CodeDefinitionModel:
    codeDefinitionId: str
    groupKey: str
    codeType: str
    code: str
    codeDescription: str
    created: str
    createdUserId: str
    modified: str
    modifiedUserId: str

