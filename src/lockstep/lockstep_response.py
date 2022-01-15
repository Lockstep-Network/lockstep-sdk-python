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


# from typing import Generic, TypeVar
from lockstep.error_result import ErrorResult
from dataclasses import dataclass

# T = TypeVar("T")

"""
Represents a response from a Lockstep Platform API call
"""
@dataclass
class LockstepResponse: #(Generic[T]):
    success: bool
    value: any # This could be replaced with TypeVar("T") in the future
    error: ErrorResult

