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

@dataclass
class ErrorResult:
    """
    Represents an error in an API call
    """
    type: str | None
    title: str | None
    status: int | None
    detail: str | None
    instance: str | None

