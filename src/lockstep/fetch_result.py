#
# Lockstep Software Development Kit for Python
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


from typing import Generic, TypeVar, Type
from dataclasses import dataclass

T = TypeVar('T')

@dataclass
class FetchResult(Generic[T]):
    """
    Represents a query response from a Lockstep Platform API call
    """
    records: list[T] | None
    totalCount: int | None
    pageSize: int | None
    pageNumber: int | None

    @classmethod
    def from_json(cls, data: dict, model_class: Type[T]):
        """
        Create a FetchResult from the json payload and instantiate
        records with the proper type.
        """
        records = [model_class(**record) for record in data.get('records', [])]
        return cls(records=records, totalCount=data.get('totalCount'),
                   pageSize=data.get('pageSize'), pageNumber=data.get('pageNumber'))