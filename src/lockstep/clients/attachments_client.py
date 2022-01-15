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

from lockstep.lockstep_response import LockstepResponse

class AttachmentsClient:

    def __init__(self, client):
        self.client = client

    """
    Retrieves the Attachment with the provided Attachment identifier. 

    An Attachment is a file that can be attached to various account 
    attributes within Lockstep. Attachments can be used for invoices, 
    bills, or any other external files that you wish to track and have 
    access to. Attachments represents an Attachment and a number of 
    different metadata attributes related to the creation, storage, and 
    ownership of the Attachment. 

    See 
    [Extensibility](https://developer.lockstep.io/docs/extensibility) 
    for more information.

    Parameters
    ----------
    id : str
        The unique ID number of the Attachment to retrieve
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. No collections are currently available for 
        querying but may be available in the future.
    """
    def retrieve_attachment(self, id: str, include: str) -> LockstepResponse:
        path = f"/api/v1/Attachments/{id}"
        return self.client.send_request("GET", path, None, {id: str, include: str})

    """
    Updates an existing Attachment with the information supplied to this 
    PATCH call. 

    The PATCH method allows you to change specific values on the object 
    while leaving other values alone. As input you should supply a list 
    of field names and new values. If you do not provide the name of a 
    field, that field will remain unchanged. This allows you to ensure 
    that you are only updating the specific fields desired. 

    An Attachment is a file that can be attached to various account 
    attributes within Lockstep. Attachments can be used for invoices, 
    bills, or any other external files that you wish to track and have 
    access to. Attachments represents an Attachment and a number of 
    different metadata attributes related to the creation, storage, and 
    ownership of the Attachment. 

    See 
    [Extensibility](https://developer.lockstep.io/docs/extensibility) 
    for more information.

    Parameters
    ----------
    id : str
        The unique Lockstep Platform ID number of the attachment to 
        update
    body : object
        A list of changes to apply to this Attachment
    """
    def update_attachment(self, id: str, body: object) -> LockstepResponse:
        path = f"/api/v1/Attachments/{id}"
        return self.client.send_request("PATCH", path, body, {id: str, body: object})

    """
    Flag this attachment as archived, which can distinguish between 
    attachments currently active and attachments not intended for active 
    use. This is similar to deletion but preserves information about the 
    record's existence. 

    An Attachment is a file that can be attached to various account 
    attributes within Lockstep. Attachments can be used for invoices, 
    bills, or any other external files that you wish to track and have 
    access to. Attachments represents an Attachment and a number of 
    different metadata attributes related to the creation, storage, and 
    ownership of the Attachment. 

    See 
    [Extensibility](https://developer.lockstep.io/docs/extensibility) 
    for more information.

    Parameters
    ----------
    id : str
        The unique ID number of the Attachment to be archived
    """
    def archive_attachment(self, id: str) -> LockstepResponse:
        path = f"/api/v1/Attachments/{id}"
        return self.client.send_request("DELETE", path, None, {id: str})

    """
    Returns a URI for the Attachment file to be downloaded, based on the 
    ID provided. 

    An Attachment is a file that can be attached to various account 
    attributes within Lockstep. Attachments can be used for invoices, 
    bills, or any other external files that you wish to track and have 
    access to. Attachments represents an Attachment and a number of 
    different metadata attributes related to the creation, storage, and 
    ownership of the Attachment. 

    See 
    [Extensibility](https://developer.lockstep.io/docs/extensibility) 
    for more information.

    Parameters
    ----------
    id : str
        The unique ID number of the Attachment whose URI will be 
        returned
    """
    def download_attachment(self, id: str) -> LockstepResponse:
        path = f"/api/v1/Attachments/{id}/download"
        return self.client.send_request("GET", path, None, {id: str})

    """
    Uploads and creates one or more Attachments from the provided 
    arguments. 

    An Attachment is a file that can be attached to various account 
    attributes within Lockstep. Attachments can be used for invoices, 
    bills, or any other external files that you wish to track and have 
    access to. Attachments represents an Attachment and a number of 
    different metadata attributes related to the creation, storage, and 
    ownership of the Attachment. 

    See 
    [Extensibility](https://developer.lockstep.io/docs/extensibility) 
    for more information.

    Parameters
    ----------
    tableName : str
        The name of the type of object to which this Attachment will be 
        linked
    objectId : str
        The unique ID of the object to which this Attachment will be 
        linked
    """
    def upload_attachment(self, tableName: str, objectId: str) -> LockstepResponse:
        path = f"/api/v1/Attachments"
        return self.client.send_request("POST", path, None, {tableName: str, objectId: str})

    """
    Queries Attachments for this account using the specified filtering, 
    sorting, nested fetch, and pagination rules requested. 

    More information on querying can be found on the [Searchlight Query 
    Language](https://developer.lockstep.io/docs/querying-with-searchlight) 
    page on the Lockstep Developer website. 

    An Attachment is a file that can be attached to various account 
    attributes within Lockstep. Attachments can be used for invoices, 
    bills, or any other external files that you wish to track and have 
    access to. Attachments represents an Attachment and a number of 
    different metadata attributes related to the creation, storage, and 
    ownership of the Attachment. 

    See 
    [Extensibility](https://developer.lockstep.io/docs/extensibility) 
    for more information.

    Parameters
    ----------
    filter : str
        The filter to use to select from the list of available 
        Attachments, in the [Searchlight query 
        syntax](https://github.com/tspence/csharp-searchlight).
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. No collections are currently available for 
        querying but may be available in the future.
    order : str
        The sort order for the results, in the [Searchlight order 
        syntax](https://github.com/tspence/csharp-searchlight).
    pageSize : int
        The page size for results (default 200, maximum of 10,000)
    pageNumber : int
        The page number for results (default 0)
    """
    def query_attachments(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/Attachments/query"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})
