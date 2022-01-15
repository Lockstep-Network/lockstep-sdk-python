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
from lockstep.models.companymodel import CompanyModel

class CompaniesClient:

    def __init__(self, client):
        self.client = client

    """
    Retrieves the Company specified by this unique identifier, 
    optionally including nested data sets. A Company represents a 
    customer, a vendor, or a company within the organization of the 
    account holder. Companies can have parents and children, 
    representing an organizational hierarchy of corporate entities. You 
    can use Companies to track projects and financial data under this 
    Company label. 

    See [Vendors, Customers, and 
    Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors) 
    for more information.

    Parameters
    ----------
    id : str
        The unique Lockstep Platform ID number of this Company; NOT the 
        customer's ERP key
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. Available collections: Attachments, 
        Contacts, CustomFields, Invoices, Notes, Classification
    """
    def retrieve_company(self, id: str, include: str) -> LockstepResponse:
        path = f"/api/v1/Companies/{id}"
        return self.client.send_request("GET", path, None, {id: str, include: str})

    """
    Updates a Company that matches the specified id with the requested 
    information. 

    The PATCH method allows you to change specific values on the object 
    while leaving other values alone. As input you should supply a list 
    of field names and new values. If you do not provide the name of a 
    field, that field will remain unchanged. This allows you to ensure 
    that you are only updating the specific fields desired. A Company 
    represents a customer, a vendor, or a company within the 
    organization of the account holder. Companies can have parents and 
    children, representing an organizational hierarchy of corporate 
    entities. You can use Companies to track projects and financial data 
    under this Company label. 

    See [Vendors, Customers, and 
    Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors) 
    for more information.

    Parameters
    ----------
    id : str
        The unique Lockstep Platform ID number of this Company; NOT the 
        customer's ERP key
    body : object
        A list of changes to apply to this Company
    """
    def update_company(self, id: str, body: object) -> LockstepResponse:
        path = f"/api/v1/Companies/{id}"
        return self.client.send_request("PATCH", path, body, {id: str, body: object})

    """
    Disable the Company referred to by this unique identifier. 

    A Company represents a customer, a vendor, or a company within the 
    organization of the account holder. Companies can have parents and 
    children, representing an organizational hierarchy of corporate 
    entities. You can use Companies to track projects and financial data 
    under this Company label. 

    See [Vendors, Customers, and 
    Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors) 
    for more information.

    Parameters
    ----------
    id : str
        The unique Lockstep Platform ID number of this Company; NOT the 
        customer's ERP key
    """
    def disable_company(self, id: str) -> LockstepResponse:
        path = f"/api/v1/Companies/{id}"
        return self.client.send_request("DELETE", path, None, {id: str})

    """
    Creates one or more Companies from a given model. A Company 
    represents a customer, a vendor, or a company within the 
    organization of the account holder. Companies can have parents and 
    children, representing an organizational hierarchy of corporate 
    entities. You can use Companies to track projects and financial data 
    under this Company label. 

    See [Vendors, Customers, and 
    Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors) 
    for more information.

    Parameters
    ----------
    body : list[CompanyModel]
        The Companies to create
    """
    def create_companies(self, body: list[CompanyModel]) -> LockstepResponse:
        path = f"/api/v1/Companies"
        return self.client.send_request("POST", path, body, {body: list[CompanyModel]})

    """
    Queries Companies for this account using the specified filtering, 
    sorting, nested fetch, and pagination rules requested. 

    More information on querying can be found on the [Searchlight Query 
    Language](https://developer.lockstep.io/docs/querying-with-searchlight) 
    page on the Lockstep Developer website. A Company represents a 
    customer, a vendor, or a company within the organization of the 
    account holder. Companies can have parents and children, 
    representing an organizational hierarchy of corporate entities. You 
    can use Companies to track projects and financial data under this 
    Company label. 

    See [Vendors, Customers, and 
    Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors) 
    for more information.

    Parameters
    ----------
    filter : str
        The filter for this query. See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. Available collections: Attachments, 
        Contacts, CustomFields, Invoices, Notes, Classification
    order : str
        The sort order for the results, in the [Searchlight order 
        syntax](https://github.com/tspence/csharp-searchlight).
    pageSize : int
        The page size for results (default 200, maximum of 10,000)
    pageNumber : int
        The page number for results (default 0)
    """
    def query_companies(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/Companies/query"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})

    """
    Queries Customer Summaries for this account using the specified 
    filtering, sorting, nested fetch, and pagination rules requested. 

    More information on querying can be found on the [Searchlight Query 
    Language](https://developer.lockstep.io/docs/querying-with-searchlight) 
    page on the Lockstep Developer website. The Customer Summary View 
    represents a slightly different view of the data and includes some 
    extra fields that might be useful. For more information, see the 
    data format of the Customer Summary Model. See [Vendors, Customers, 
    and 
    Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors) 
    for more information.

    Parameters
    ----------
    filter : str
        The filter for this query. See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. No collections are currently available but 
        may be offered in the future
    order : str
        The sort order for the results, in the [Searchlight order 
        syntax](https://github.com/tspence/csharp-searchlight).
    pageSize : int
        The page size for results (default 200, maximum of 10,000)
    pageNumber : int
        The page number for results (default 0)
    """
    def query_customer_summary(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/Companies/views/customer-summary"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})

    """
    Retrieves the Customer Details specified by this unique identifier, 
    optionally including nested data sets. The Customer Detail View 
    represents a slightly different view of the data and includes some 
    extra fields that might be useful. For more information, see the 
    data format of the Customer Detail Model. See [Vendors, Customers, 
    and 
    Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors) 
    for more information.

    Parameters
    ----------
    id : str
        The unique Lockstep Platform ID number of this Company; NOT the 
        customer's ERP key
    """
    def retrieve_customer_detail(self, id: str) -> LockstepResponse:
        path = f"/api/v1/Companies/views/customer-details/{id}"
        return self.client.send_request("GET", path, None, {id: str})
