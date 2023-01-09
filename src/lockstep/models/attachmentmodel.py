#
# Lockstep Platform SDK for Python
#
# (c) 2021-2023 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2023 Lockstep, Inc.
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

    attachmentId: str | None = None
    groupKey: str | None = None
    tableKey: str | None = None
    objectKey: str | None = None
    fileName: str | None = None
    fileExt: str | None = None
    attachmentTypeId: str | None = None
    isArchived: bool | None = None
    originAttachmentId: str | None = None
    viewInternal: bool | None = None
    viewExternal: bool | None = None
    erpKey: str | None = None
    appEnrollmentId: str | None = None
    created: str | None = None
    createdUserId: str | None = None
    attachmentType: str | None = None

