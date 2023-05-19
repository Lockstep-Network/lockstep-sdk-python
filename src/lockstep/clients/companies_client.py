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
from lockstep.models.bulkdeleterequestmodel import BulkDeleteRequestModel
from lockstep.models.companydetailsmodel import CompanyDetailsModel
from lockstep.models.companymodel import CompanyModel
from lockstep.models.customersummarymodel import CustomerSummaryModel
from lockstep.models.deleteresult import DeleteResult
from lockstep.models.vendorsummarymodel import VendorSummaryModel
from lockstep.models.viewboxsettingsmodel import ViewBoxSettingsModel

class CompaniesClient:
    """
    API methods related to Companies
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_company(self, id: object, include: object) -> LockstepResponse[CompanyModel]:
        """
        Retrieves the Company specified by this unique identifier,
        optionally including nested data sets.

        A Company represents a customer, a vendor, or a company within
        the organization of the account holder. Companies can have
        parents and children, representing an organizational hierarchy
        of corporate entities. You can use Companies to track projects
        and financial data under this Company label.

        See [Vendors, Customers, and
        Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors)
        for more information.

        Parameters
        ----------
        id : object
            The unique Lockstep Platform ID number of this Company; NOT
            the customer's ERP key
        include : object
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: Attachments,
            Contacts, CustomFields, Invoices, Notes, Classification
        """
        path = f"/api/v1/Companies/{id}"
        result = self.client.send_request("GET", path, None, {"include": include}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, CompanyModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_company(self, id: object, body: object) -> LockstepResponse[CompanyModel]:
        """
        Updates a Company that matches the specified id with the
        requested information.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. If you do not
        provide the name of a field, that field will remain unchanged.
        This allows you to ensure that you are only updating the
        specific fields desired.

        A Company represents a customer, a vendor, or a company within
        the organization of the account holder. Companies can have
        parents and children, representing an organizational hierarchy
        of corporate entities. You can use Companies to track projects
        and financial data under this Company label.

        See [Vendors, Customers, and
        Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors)
        for more information.

        Parameters
        ----------
        id : object
            The unique Lockstep Platform ID number of this Company; NOT
            the customer's ERP key
        body : object
            A list of changes to apply to this Company
        """
        path = f"/api/v1/Companies/{id}"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, CompanyModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_company(self, id: object) -> LockstepResponse[DeleteResult]:
        """
        Delete the Company referred to by this unique identifier.

        A Company represents a customer, a vendor, or a company within
        the organization of the account holder. Companies can have
        parents and children, representing an organizational hierarchy
        of corporate entities. You can use Companies to track projects
        and financial data under this Company label.

        See [Vendors, Customers, and
        Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors)
        for more information.

        Parameters
        ----------
        id : object
            The unique Lockstep Platform ID number of this Company; NOT
            the customer's ERP key
        """
        path = f"/api/v1/Companies/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, DeleteResult(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_companies(self, body: list[object]) -> LockstepResponse[list[CompanyModel]]:
        """
        Creates one or more Companies from a given model.

        A Company represents a customer, a vendor, or a company within
        the organization of the account holder. Companies can have
        parents and children, representing an organizational hierarchy
        of corporate entities. You can use Companies to track projects
        and financial data under this Company label.

        See [Vendors, Customers, and
        Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors)
        for more information.

        Parameters
        ----------
        body : list[object]
            The Companies to create
        """
        path = "/api/v1/Companies"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [CompanyModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_companies(self, body: object) -> LockstepResponse[DeleteResult]:
        """
        Delete the Companies referred to by these unique identifiers.

        A Company represents a customer, a vendor, or a company within
        the organization of the account holder. Companies can have
        parents and children, representing an organizational hierarchy
        of corporate entities. You can use Companies to track projects
        and financial data under this Company label.

        See [Vendors, Customers, and
        Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors)
        for more information.

        Parameters
        ----------
        body : object
            The unique Lockstep Platform ID numbers of the Companies to
            delete; NOT the customer's ERP key
        """
        path = "/api/v1/Companies"
        result = self.client.send_request("DELETE", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, DeleteResult(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_companies(self, filter: object, include: object, order: object, pageSize: object, pageNumber: object) -> LockstepResponse[FetchResult[CompanyModel]]:
        """
        Queries Companies for this account using the specified
        filtering, sorting, nested fetch, and pagination rules
        requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        A Company represents a customer, a vendor, or a company within
        the organization of the account holder. Companies can have
        parents and children, representing an organizational hierarchy
        of corporate entities. You can use Companies to track projects
        and financial data under this Company label.

        See [Vendors, Customers, and
        Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors)
        for more information.

        Parameters
        ----------
        filter : object
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : object
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: Attachments,
            Contacts, CustomFields, Invoices, Notes, Classification
        order : object
            The sort order for the results, in the [Searchlight order
            syntax](https://github.com/tspence/csharp-searchlight).
        pageSize : object
            The page size for results (default 250, maximum of 500)
        pageNumber : object
            The page number for results (default 0)
        """
        path = "/api/v1/Companies/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), CompanyModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_customer_summary(self, filter: object, include: object, order: object, pageSize: object, pageNumber: object, reportDate: object) -> LockstepResponse[FetchResult[CustomerSummaryModel]]:
        """
        Queries Customer Summaries for this account using the specified
        filtering, sorting, nested fetch, and pagination rules
        requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        The Customer Summary View represents a slightly different view
        of the data and includes some extra fields that might be useful.
        For more information, see the data format of the Customer
        Summary Model.

        See [Vendors, Customers, and
        Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors)
        for more information.

        Parameters
        ----------
        filter : object
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : object
            To fetch additional data on this object, specify the list of
            elements to retrieve. No collections are currently available
            but may be offered in the future
        order : object
            The sort order for the results, in the [Searchlight order
            syntax](https://github.com/tspence/csharp-searchlight).
        pageSize : object
            The page size for results (default 250, maximum of 500)
        pageNumber : object
            The page number for results (default 0)
        reportDate : object
            The date to calculate the fields on. If no date is entered
            the current UTC date will be used.
        """
        path = "/api/v1/Companies/views/customer-summary"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber, "reportDate": reportDate}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), CustomerSummaryModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_vendor_summary(self, filter: object, include: object, order: object, pageSize: object, pageNumber: object, reportDate: object) -> LockstepResponse[FetchResult[VendorSummaryModel]]:
        """
        Queries Vendor Summaries for this account using the specified
        filtering, sorting, nested fetch, and pagination rules
        requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        The Vendor Summary View represents a slightly different view of
        the data and includes some extra fields that might be useful.
        For more information, see the data format of the Vendor Summary
        Model.

        See [Vendors, Customers, and
        Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors)
        for more information.

        Parameters
        ----------
        filter : object
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : object
            To fetch additional data on this object, specify the list of
            elements to retrieve. No collections are currently available
            but may be offered in the future
        order : object
            The sort order for the results, in the [Searchlight order
            syntax](https://github.com/tspence/csharp-searchlight).
        pageSize : object
            The page size for results (default 250, maximum of 500)
        pageNumber : object
            The page number for results (default 0)
        reportDate : object
            The date to calculate the fields on. If no date is entered
            the current UTC date will be used.
        """
        path = "/api/v1/Companies/views/vendor-summary"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber, "reportDate": reportDate}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), VendorSummaryModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def retrieve_company_detail(self, id: object) -> LockstepResponse[CompanyDetailsModel]:
        """
        Retrieves the Company Details specified by this unique
        identifier, optionally including nested data sets.

        The Company Detail View represents a slightly different view of
        the data and includes some extra fields that might be useful.
        For more information, see the data format of the Company Detail
        Model.

        See [Vendors, Customers, and
        Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors)
        for more information.

        Parameters
        ----------
        id : object
            The unique Lockstep Platform ID number of this Company; NOT
            the company's ERP key
        """
        path = f"/api/v1/Companies/views/details/{id}"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, CompanyDetailsModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def set_company_logo(self, id: object, min_x: object, min_y: object, width: object, height: object, filename: object) -> LockstepResponse[CompanyModel]:
        """
        Sets the logo for specified company. The logo will be stored in
        the Lockstep Platform and will be **publicly accessible**.

        .jpg, .jpeg, .png, and .webp are supported. 2MB maximum. If no
        logo is uploaded, the existing logo will be deleted.

        A Company represents a customer, a vendor, or a company within
        the organization of the account holder. Companies can have
        parents and children, representing an organizational hierarchy
        of corporate entities. You can use Companies to track projects
        and financial data under this Company label.

        Optional view box meta data for the provided logo may be
        supplied using the following query parameters. Please note that
        you must supply either all of the values or none of the values.
        <ul><li>min_x</li><li>min_y</li><li>width</li><li>height</li></ul>


        See [Vendors, Customers, and
        Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors)
        for more information.

        Parameters
        ----------
        id : object
            The unique Lockstep Platform ID number of this Company; NOT
            the customer's ERP key
        min_x : object
            ViewBox minX setting for this Company's logo.
        min_y : object
            ViewBox minY setting for this Company's logo.
        width : object
            ViewBox width setting for this Company's logo.
        height : object
            ViewBox height setting for this Company's logo.
        filename : object
            The full path of a file to upload to the API
        """
        path = f"/api/v1/Companies/{id}/logo"
        result = self.client.send_request("POST", path, None, {"min_x": min_x, "min_y": min_y, "width": width, "height": height}, filename)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, CompanyModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_logo_view_box_settings(self, id: object, body: object) -> LockstepResponse[CompanyModel]:
        """
        Update view box meta data for the given Company id.

        Parameters
        ----------
        id : object
            The unique Lockstep Platform ID number of this Company; NOT
            the customer's ERP key
        body : object
            The `ViewBoxSettingsModel` containing meta data value
            updates
        """
        path = f"/api/v1/Companies/{id}/logo-settings"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, CompanyModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
