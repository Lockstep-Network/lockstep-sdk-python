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
class TranscriptionRequestSubmit:
    """
    A request to transcribe the provided file content to a Lockstep
    Platform object.
    """

    fileContent: str | None = None
    fileUrl: str | None = None
    fileContentUrl: str | None = None
    fileName: str | None = None
    invoiceTypeCode: str | None = None
    transcriptionValidationRequestId: str | None = None

