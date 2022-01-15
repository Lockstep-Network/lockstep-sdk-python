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
from lockstep.models.contactmodel import ContactModel

class ContactsClient:

    def __init__(self, client):
        self.client = client

    """
    Retrieves the Contact specified by this unique identifier, 
    optionally including nested data sets. A Contact contains 
    information about a person or role within a Company. You can use 
    Contacts to track information about who is responsible for a 
    specific project, who handles invoices, or information about which 
    role at a particular customer or vendor you should speak with about 
    invoices.

    Parameters
    ----------
    id : str
        The unique Lockstep Platform ID number of this Contact; NOT the 
        customer's ERP key
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. Available collections: Attachments, 
        CustomFields, Notes
    """
    def retrieve_contact(self, id: str, include: str) -> LockstepResponse:
        path = f"/api/v1/Contacts/{id}"
        return self.client.send_request("GET", path, None, {id: str, include: str})

    """
    Updates a contact that matches the specified id with the requested 
    information. 

    The PATCH method allows you to change specific values on the object 
    while leaving other values alone. As input you should supply a list 
    of field names and new values. If you do not provide the name of a 
    field, that field will remain unchanged. This allows you to ensure 
    that you are only updating the specific fields desired. A Contact 
    contains information about a person or role within a Company. You 
    can use Contacts to track information about who is responsible for a 
    specific project, who handles invoices, or information about which 
    role at a particular customer or vendor you should speak with about 
    invoices.

    Parameters
    ----------
    id : str
        The unique Lockstep Platform ID number of the Contact to update; 
        NOT the customer's ERP key
    body : object
        A list of changes to apply to this Contact
    """
    def update_contact(self, id: str, body: object) -> LockstepResponse:
        path = f"/api/v1/Contacts/{id}"
        return self.client.send_request("PATCH", path, body, {id: str, body: object})

    """
    Disable the Contact referred to by this unique identifier. 

    A Contact contains information about a person or role within a 
    Company. You can use Contacts to track information about who is 
    responsible for a specific project, who handles invoices, or 
    information about which role at a particular customer or vendor you 
    should speak with about invoices.

    Parameters
    ----------
    id : str
        The unique Lockstep Platform ID number of the Contact to 
        disable; NOT the customer's ERP key
    """
    def disable_contact(self, id: str) -> LockstepResponse:
        path = f"/api/v1/Contacts/{id}"
        return self.client.send_request("DELETE", path, None, {id: str})

    """
    Creates one or more contacts from a given model. 

    A Contact contains information about a person or role within a 
    Company. You can use Contacts to track information about who is 
    responsible for a specific project, who handles invoices, or 
    information about which role at a particular customer or vendor you 
    should speak with about invoices.

    Parameters
    ----------
    body : list[ContactModel]
        The Contacts to create
    """
    def create_contacts(self, body: list[ContactModel]) -> LockstepResponse:
        path = f"/api/v1/Contacts"
        return self.client.send_request("POST", path, body, {body: list[ContactModel]})

    """
    Queries Contacts for this account using the specified filtering, 
    sorting, nested fetch, and pagination rules requested. 

    More information on querying can be found on the [Searchlight Query 
    Language](https://developer.lockstep.io/docs/querying-with-searchlight) 
    page on the Lockstep Developer website. A Contact contains 
    information about a person or role within a Company. You can use 
    Contacts to track information about who is responsible for a 
    specific project, who handles invoices, or information about which 
    role at a particular customer or vendor you should speak with about 
    invoices.

    Parameters
    ----------
    filter : str
        The filter for this query. See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. Available collections: Attachments, 
        CustomFields, Notes
    order : str
        The sort order for this query. See See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageSize : int
        The page size for results (default 200). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageNumber : int
        The page number for results (default 0). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    """
    def query_contacts(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/Contacts/query"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})
