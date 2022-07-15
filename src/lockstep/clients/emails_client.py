#
# Lockstep Platform SDK for Python
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

from lockstep.lockstep_response import LockstepResponse
from lockstep.models.errorresult import ErrorResult
from lockstep.fetch_result import FetchResult
from lockstep.models.actionresultmodel import ActionResultModel
from lockstep.models.emailmodel import EmailModel
from requests.models import Response

class EmailsClient:
    """
    API methods related to Emails
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_email(self, id: str, include: str) -> LockstepResponse[EmailModel]:
        """
        Retrieves the email with the specified email identifier.

        An Email represents a communication sent from one company to
        another. The creator of the email is identified by the
        `CompanyId` field, recipient(s) by the `EmailTo` field, and cc
        recipient(s) by the 'EmailCC' field. The Email Model represents
        an email and a number of different metadata attributes related
        to the creation, storage, and ownership of the email.

        Parameters
        ----------
        id : str
            The unique ID number of the Email to retrieve.
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: Attachments,
            CustomFields, Notes, ResponseOrigin
        """
        path = f"/api/v1/Emails/{id}"
        result = self.client.send_request("GET", path, None, {"include": include}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, EmailModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def update_email(self, id: str, body: object) -> LockstepResponse[EmailModel]:
        """
        Updates an existing Email with the information supplied to this
        PATCH call.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. If you do not
        provide the name of a field, that field will remain unchanged.
        This allows you to ensure that you are only updating the
        specific fields desired.

        An Email represents a communication sent from one company to
        another. The creator of the email is identified by the
        `CompanyId` field, recipient(s) by the `EmailTo` field, and cc
        recipient(s) by the 'EmailCC' field. The Email Model represents
        an email and a number of different metadata attributes related
        to the creation, storage, and ownership of the email.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the email to
            update
        body : object
            A list of changes to apply to this Email
        """
        path = f"/api/v1/Emails/{id}"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, EmailModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def delete_email(self, id: str) -> LockstepResponse[ActionResultModel]:
        """
        Deletes the Email referred to by this unique identifier.

        An Email represents a communication sent from one company to
        another. The creator of the email is identified by the
        `CompanyId` field, recipient(s) by the `EmailTo` field, and cc
        recipient(s) by the 'EmailCC' field. The Email Model represents
        an email and a number of different metadata attributes related
        to the creation, storage, and ownership of the email.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Email to
            delete
        """
        path = f"/api/v1/Emails/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ActionResultModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def retrieve_email_logo(self, emailId: str, nonce: str) -> Response:
        """
        Retrieves a signature logo for the email with the specified
        identifier and increments 'ViewCount'.

        An Email represents a communication sent from one company to
        another. The creator of the email is identified by the
        `CompanyId` field, recipient(s) by the `EmailTo` field, and cc
        recipient(s) by the 'EmailCC' field. The Email Model represents
        an email and a number of different metadata attributes related
        to the creation, storage, and ownership of the email.

        Parameters
        ----------
        emailId : str
            The unique ID number of the Email to retrieve.
        nonce : str
            The random nonce applied at time of url creation.
        """
        path = f"/api/v1/Emails/{emailId}/logo/{nonce}"
        result = self.client.send_request("GET", path, None, {}, None)
        return result

    def create_emails(self, body: list[EmailModel]) -> LockstepResponse[list[EmailModel]]:
        """
        Creates one or more emails from the specified array of Email
        Models

        An Email represents a communication sent from one company to
        another. The creator of the email is identified by the
        `CompanyId` field, recipient(s) by the `EmailTo` field, and cc
        recipient(s) by the 'EmailCC' field. The Email Model represents
        an email and a number of different metadata attributes related
        to the creation, storage, and ownership of the email.

        Parameters
        ----------
        body : list[EmailModel]
            The array of emails to be created
        """
        path = "/api/v1/Emails"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, list[EmailModel](**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def query_emails(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[EmailModel]]:
        """
        Queries Emails on the Lockstep Platform using the specified
        filtering, sorting, nested fetch, and pagination rules
        requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        An Email represents a communication sent from one company to
        another. The creator of the email is identified by the
        `CompanyId` field, recipient(s) by the `EmailTo` field, and cc
        recipient(s) by the 'EmailCC' field. The Email Model represents
        an email and a number of different metadata attributes related
        to the creation, storage, and ownership of the email.

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
            The page size for results (default 200). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        """
        path = "/api/v1/Emails/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult[EmailModel](**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))
