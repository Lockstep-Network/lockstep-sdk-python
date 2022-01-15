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
from lockstep.models.emailmodel import EmailModel

class EmailsClient:

    def __init__(self, client):
        self.client = client

    """
    Retrieves the email with the specified email identifier. 

    An Email represents a communication sent from one company to 
    another. The creator of the email is identified by the `CompanyId` 
    field, recipient(s) by the `EmailTo` field, and cc recipient(s) by 
    the 'EmailCC' field. The Email Model represents an email and a 
    number of different metadata attributes related to the creation, 
    storage, and ownership of the email.

    Parameters
    ----------
    id : str
        The unique ID number of the Email to retrieve.
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. Available collections: Attachments, 
        CustomFields, Notes, ResponseOrigin
    """
    def retrieve_email(self, id: str, include: str) -> LockstepResponse:
        path = f"/api/v1/Emails/{id}"
        return self.client.send_request("GET", path, None, {id: str, include: str})

    """
    Updates an existing Email with the information supplied to this 
    PATCH call. 

    The PATCH method allows you to change specific values on the object 
    while leaving other values alone. As input you should supply a list 
    of field names and new values. If you do not provide the name of a 
    field, that field will remain unchanged. This allows you to ensure 
    that you are only updating the specific fields desired. 

    An Email represents a communication sent from one company to 
    another. The creator of the email is identified by the `CompanyId` 
    field, recipient(s) by the `EmailTo` field, and cc recipient(s) by 
    the 'EmailCC' field. The Email Model represents an email and a 
    number of different metadata attributes related to the creation, 
    storage, and ownership of the email.

    Parameters
    ----------
    id : str
        The unique Lockstep Platform ID number of the email to update
    body : object
        A list of changes to apply to this Email
    """
    def update_email(self, id: str, body: object) -> LockstepResponse:
        path = f"/api/v1/Emails/{id}"
        return self.client.send_request("PATCH", path, body, {id: str, body: object})

    """
    Deletes the Email referred to by this unique identifier. 

    An Email represents a communication sent from one company to 
    another. The creator of the email is identified by the `CompanyId` 
    field, recipient(s) by the `EmailTo` field, and cc recipient(s) by 
    the 'EmailCC' field. The Email Model represents an email and a 
    number of different metadata attributes related to the creation, 
    storage, and ownership of the email.

    Parameters
    ----------
    id : str
        The unique Lockstep Platform ID number of the Email to delete
    """
    def delete_email(self, id: str) -> LockstepResponse:
        path = f"/api/v1/Emails/{id}"
        return self.client.send_request("DELETE", path, None, {id: str})

    """
    Retrieves a signature logo for the email with the specified 
    identifier and increments 'ViewCount'. 

    An Email represents a communication sent from one company to 
    another. The creator of the email is identified by the `CompanyId` 
    field, recipient(s) by the `EmailTo` field, and cc recipient(s) by 
    the 'EmailCC' field. The Email Model represents an email and a 
    number of different metadata attributes related to the creation, 
    storage, and ownership of the email.

    Parameters
    ----------
    emailId : str
        The unique ID number of the Email to retrieve.
    nonce : str
        The random nonce applied at time of url creation.
    """
    def retrieve_email_logo(self, emailId: str, nonce: str) -> LockstepResponse:
        path = f"/api/v1/Emails/{emailId}/logo/{nonce}"
        return self.client.send_request("GET", path, None, {emailId: str, nonce: str})

    """
    Creates one or more emails from the specified array of Email Models 

    An Email represents a communication sent from one company to 
    another. The creator of the email is identified by the `CompanyId` 
    field, recipient(s) by the `EmailTo` field, and cc recipient(s) by 
    the 'EmailCC' field. The Email Model represents an email and a 
    number of different metadata attributes related to the creation, 
    storage, and ownership of the email.

    Parameters
    ----------
    body : list[EmailModel]
        The array of emails to be created
    """
    def create_emails(self, body: list[EmailModel]) -> LockstepResponse:
        path = f"/api/v1/Emails"
        return self.client.send_request("POST", path, body, {body: list[EmailModel]})

    """
    Queries Emails on the Lockstep Platform using the specified 
    filtering, sorting, nested fetch, and pagination rules requested. 

    More information on querying can be found on the [Searchlight Query 
    Language](https://developer.lockstep.io/docs/querying-with-searchlight) 
    page on the Lockstep Developer website. 

    An Email represents a communication sent from one company to 
    another. The creator of the email is identified by the `CompanyId` 
    field, recipient(s) by the `EmailTo` field, and cc recipient(s) by 
    the 'EmailCC' field. The Email Model represents an email and a 
    number of different metadata attributes related to the creation, 
    storage, and ownership of the email.

    Parameters
    ----------
    filter : str
        The filter to use to select from the list of available 
        applications, in the [Searchlight query 
        syntax](https://github.com/tspence/csharp-searchlight).
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. Available collections: Attachments, 
        CustomFields, Notes, ResponseOrigin
    order : str
        The sort order for the results, in the [Searchlight order 
        syntax](https://github.com/tspence/csharp-searchlight).
    pageSize : int
        The page size for results (default 200). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageNumber : int
        The page number for results (default 0). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    """
    def query_emails(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/Emails/query"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})
