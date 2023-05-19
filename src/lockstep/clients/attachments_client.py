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
from lockstep.models.actionresultmodel import ActionResultModel
from lockstep.models.attachmentmodel import AttachmentModel
from lockstep.models.urimodel import UriModel
from requests.models import Response

class AttachmentsClient:
    """
    API methods related to Attachments
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_attachment(self, id: str, include: str) -> LockstepResponse[AttachmentModel]:
        """
        Retrieves the Attachment with the provided Attachment
        identifier.

        An Attachment is a file that can be attached to various account
        attributes within Lockstep. Attachments can be used for
        invoices, bills, or any other external files that you wish to
        track and have access to. Attachments represents an Attachment
        and a number of different metadata attributes related to the
        creation, storage, and ownership of the Attachment.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        id : str
            The unique ID number of the Attachment to retrieve
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. No collections are currently available
            for querying but may be available in the future.
        """
        path = f"/api/v1/Attachments/{id}"
        result = self.client.send_request("GET", path, None, {"include": include}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, AttachmentModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_attachment(self, id: str, body: object) -> LockstepResponse[AttachmentModel]:
        """
        Updates an existing Attachment with the information supplied to
        this PATCH call.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. If you do not
        provide the name of a field, that field will remain unchanged.
        This allows you to ensure that you are only updating the
        specific fields desired.

        An Attachment is a file that can be attached to various account
        attributes within Lockstep. Attachments can be used for
        invoices, bills, or any other external files that you wish to
        track and have access to. Attachments represents an Attachment
        and a number of different metadata attributes related to the
        creation, storage, and ownership of the Attachment.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the attachment to
            update
        body : object
            A list of changes to apply to this Attachment
        """
        path = f"/api/v1/Attachments/{id}"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, AttachmentModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def archive_attachment(self, id: str) -> LockstepResponse[ActionResultModel]:
        """
        Flag this attachment as archived, which can distinguish between
        attachments currently active and attachments not intended for
        active use. This is similar to deletion but preserves
        information about the record's existence.

        An Attachment is a file that can be attached to various account
        attributes within Lockstep. Attachments can be used for
        invoices, bills, or any other external files that you wish to
        track and have access to. Attachments represents an Attachment
        and a number of different metadata attributes related to the
        creation, storage, and ownership of the Attachment.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        id : str
            The unique ID number of the Attachment to be archived
        """
        path = f"/api/v1/Attachments/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ActionResultModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def download_attachment_url(self, id: str) -> LockstepResponse[UriModel]:
        """
        Returns a URI for the Attachment file to be downloaded, based on
        the ID provided.

        An Attachment is a file that can be attached to various account
        attributes within Lockstep. Attachments can be used for
        invoices, bills, or any other external files that you wish to
        track and have access to. Attachments represents an Attachment
        and a number of different metadata attributes related to the
        creation, storage, and ownership of the Attachment.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        id : str
            The unique ID number of the Attachment whose URI will be
            returned
        """
        path = f"/api/v1/Attachments/{id}/download-url"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, UriModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def download_attachment_file(self, id: str) -> Response:
        """
        Returns the Attachment file to be downloaded, based on the ID
        provided.

        An Attachment is a file that can be attached to various account
        attributes within Lockstep. Attachments can be used for
        invoices, bills, or any other external files that you wish to
        track and have access to. Attachments represents an Attachment
        and a number of different metadata attributes related to the
        creation, storage, and ownership of the Attachment.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        id : str
            The unique ID number of the Attachment whose URI will be
            returned
        """
        path = f"/api/v1/Attachments/{id}/download-file"
        result = self.client.send_request("GET", path, None, {}, None)
        return result

    def upload_attachment(self, tableName: str, objectId: str, attachmentType: str, filename: str) -> LockstepResponse[list[AttachmentModel]]:
        """
        Uploads and creates one or more Attachments from the provided
        arguments.

        An Attachment is a file that can be attached to various account
        attributes within Lockstep. Attachments can be used for
        invoices, bills, or any other external files that you wish to
        track and have access to. Attachments represents an Attachment
        and a number of different metadata attributes related to the
        creation, storage, and ownership of the Attachment.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        tableName : str
            The name of the type of object to which this Attachment will
            be linked
        objectId : str
            The unique ID of the object to which this Attachment will be
            linked
        attachmentType : str
            The type of this attachment
        filename : str
            The full path of a file to upload to the API
        """
        path = "/api/v1/Attachments"
        result = self.client.send_request("POST", path, None, {"tableName": tableName, "objectId": objectId, "attachmentType": attachmentType}, filename)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [AttachmentModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_attachments(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[AttachmentModel]]:
        """
        Queries Attachments for this account using the specified
        filtering, sorting, nested fetch, and pagination rules
        requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        An Attachment is a file that can be attached to various account
        attributes within Lockstep. Attachments can be used for
        invoices, bills, or any other external files that you wish to
        track and have access to. Attachments represents an Attachment
        and a number of different metadata attributes related to the
        creation, storage, and ownership of the Attachment.

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
        path = "/api/v1/Attachments/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), AttachmentModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
