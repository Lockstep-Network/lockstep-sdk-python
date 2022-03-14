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
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

@dataclass
class AttachmentModel:
    """
    An Attachment is a file that can be attached to various account
    attributes within Lockstep. This data model contains metadata about
    the attachment. You can upload and download attachments into the
    Lockstep Platform along with this metadata. Attachments can be used
    for invoices, payments, legal documents, or any other external files
    that you wish to track. See [Extensibility](https://developer.lockstep.io/docs/extensibility)
    for more information.
    """

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
    erpKey: str = None
    appEnrollmentId: str = None
    created: str = None
    createdUserId: str = None
    attachmentType: str = None

