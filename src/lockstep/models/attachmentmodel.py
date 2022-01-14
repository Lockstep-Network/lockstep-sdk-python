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

"""
Represents a user uploaded attachment
"""
@dataclass
class AttachmentModel:
    attachmentId: str = None
    groupKey: str = None
    tableKey: str = None
    objectKey: str = None
    fileName: str = None
    fileExt: str = None
    attachmentTypeId: str = None
    isArchived: bool = None
    originAttachmentId: str = None
    viewInternal: bool = None
    viewExternal: bool = None
    created: str = None
    createdUserId: str = None

