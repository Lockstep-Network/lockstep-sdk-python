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

from lockstep.lockstep_response import LockstepResponse
from lockstep.models.errorresult import ErrorResult
from lockstep.fetch_result import FetchResult
from lockstep.models.attachmentlinkmodel import AttachmentLinkModel
from lockstep.models.deleteresult import DeleteResult

class AttachmentLinksClient:
    """
    API methods related to AttachmentLinks
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_attachment_link(self, attachmentId: str, objectKey: str, tableName: str) -> LockstepResponse[AttachmentLinkModel]:
        """
        Retrieves the Attachment Link with the provided Attachment Link
        identifier.

        An Attachment Link is a link that associates one Attachment with
        one object within Lockstep.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        attachmentId : str

        objectKey : str

        tableName : str

        """
        path = "/api/v1/AttachmentLinks"
        result = self.client.send_request("GET", path, None, {"attachmentId": attachmentId, "objectKey": objectKey, "tableName": tableName}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, AttachmentLinkModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def upload_attachment(self, body: list[object]) -> LockstepResponse[list[AttachmentLinkModel]]:
        """
        Creates one Attachment Link from the provided arguments.

        An Attachment Link is a link that associates one Attachment with
        one object within Lockstep.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        body : list[object]

        """
        path = "/api/v1/AttachmentLinks"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [AttachmentLinkModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_attachment_link(self, attachmentId: str, objectKey: str, tableName: str) -> LockstepResponse[DeleteResult]:
        """
        Delete the specified link between an object and its attachment.

        An Attachment Link is a link that associates one Attachment with
        one object within Lockstep.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        attachmentId : str

        objectKey : str

        tableName : str

        """
        path = "/api/v1/AttachmentLinks"
        result = self.client.send_request("DELETE", path, None, {"attachmentId": attachmentId, "objectKey": objectKey, "tableName": tableName}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, DeleteResult(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_attachment_links(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[AttachmentLinkModel]]:
        """
        Queries Attachment Links for this account using the specified
        filtering, sorting, nested fetch, and pagination rules
        requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        An Attachment Link is a link that associates one Attachment with
        one object within Lockstep.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        filter : str
            The filter to use to select from the list of available
            Attachments, in the [Searchlight query
            syntax](https://github.com/tspence/csharp-searchlight).
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. No collections are currently available
            for querying but may be available in the future.
        order : str
            The sort order for the results, in the [Searchlight order
            syntax](https://github.com/tspence/csharp-searchlight).
        pageSize : int
            The page size for results (default 250, maximum of 500)
        pageNumber : int
            The page number for results (default 0)
        """
        path = "/api/v1/AttachmentLinks/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), AttachmentLinkModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
