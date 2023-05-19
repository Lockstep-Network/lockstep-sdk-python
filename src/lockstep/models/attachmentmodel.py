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

    attachmentId: object | None = None
    groupKey: object | None = None
    tableKey: object | None = None
    objectKey: object | None = None
    fileName: object | None = None
    fileExt: object | None = None
    isArchived: object | None = None
    erpKey: object | None = None
    appEnrollmentId: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    attachmentType: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
