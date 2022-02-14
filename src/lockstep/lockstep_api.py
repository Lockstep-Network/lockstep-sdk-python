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
# @version    2022.6.48.0
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

import requests
import urllib.parse
import platform

"""Lockstep Platform API Client object

Use this object to connect to the Lockstep Platform API.
"""
class LockstepApi:
    from lockstep.lockstep_response import LockstepResponse

    def __init__(self, env: str, appname: str):
        """Construct a new LockstepApi client object
        
        Parameters
        ----------
        env : str
            Select the Lockstep Platform environment to use for this client. You
            may select from either "prd", "sbx", or provide a full URL of a custom
            environment.
        appname : str
            Provide a name for your application for logging and debugging. This
            name will be recorded alongside API calls so that you can identify
            the source of errors. 
        """
        from lockstep.clients.activities_client import ActivitiesClient
        from lockstep.clients.apikeys_client import ApiKeysClient
        from lockstep.clients.appenrollments_client import AppEnrollmentsClient
        from lockstep.clients.applications_client import ApplicationsClient
        from lockstep.clients.attachments_client import AttachmentsClient
        from lockstep.clients.codedefinitions_client import CodeDefinitionsClient
        from lockstep.clients.companies_client import CompaniesClient
        from lockstep.clients.contacts_client import ContactsClient
        from lockstep.clients.creditmemoapplied_client import CreditMemoAppliedClient
        from lockstep.clients.currencies_client import CurrenciesClient
        from lockstep.clients.customfielddefinitions_client import CustomFieldDefinitionsClient
        from lockstep.clients.customfieldvalues_client import CustomFieldValuesClient
        from lockstep.clients.definitions_client import DefinitionsClient
        from lockstep.clients.emails_client import EmailsClient
        from lockstep.clients.invoicehistory_client import InvoiceHistoryClient
        from lockstep.clients.invoices_client import InvoicesClient
        from lockstep.clients.leads_client import LeadsClient
        from lockstep.clients.notes_client import NotesClient
        from lockstep.clients.paymentapplications_client import PaymentApplicationsClient
        from lockstep.clients.payments_client import PaymentsClient
        from lockstep.clients.provisioning_client import ProvisioningClient
        from lockstep.clients.reports_client import ReportsClient
        from lockstep.clients.status_client import StatusClient
        from lockstep.clients.sync_client import SyncClient
        from lockstep.clients.useraccounts_client import UserAccountsClient
        from lockstep.clients.userroles_client import UserRolesClient
        from lockstep.clients.webhooks_client import WebhooksClient
        self.activities = ActivitiesClient(self)
        self.apiKeys = ApiKeysClient(self)
        self.appEnrollments = AppEnrollmentsClient(self)
        self.applications = ApplicationsClient(self)
        self.attachments = AttachmentsClient(self)
        self.codeDefinitions = CodeDefinitionsClient(self)
        self.companies = CompaniesClient(self)
        self.contacts = ContactsClient(self)
        self.creditMemoApplied = CreditMemoAppliedClient(self)
        self.currencies = CurrenciesClient(self)
        self.customFieldDefinitions = CustomFieldDefinitionsClient(self)
        self.customFieldValues = CustomFieldValuesClient(self)
        self.definitions = DefinitionsClient(self)
        self.emails = EmailsClient(self)
        self.invoiceHistory = InvoiceHistoryClient(self)
        self.invoices = InvoicesClient(self)
        self.leads = LeadsClient(self)
        self.notes = NotesClient(self)
        self.paymentApplications = PaymentApplicationsClient(self)
        self.payments = PaymentsClient(self)
        self.provisioning = ProvisioningClient(self)
        self.reports = ReportsClient(self)
        self.status = StatusClient(self)
        self.sync = SyncClient(self)
        self.userAccounts = UserAccountsClient(self)
        self.userRoles = UserRolesClient(self)
        self.webhooks = WebhooksClient(self)
        if env == "sbx":
            self.serverUrl = "https://api.sbx.lockstep.io/"
        elif env == "prd":
            self.serverUrl = "https://api.lockstep.io/"
        else:
            self.serverUrl = env
        self.sdkName = "Python"
        self.sdkVersion = "2022.6.48.0"
        self.machineName = platform.uname().node
        self.applicationName = appname

    
    def with_api_key(self, apiKey: str):
        """Configure this API client to use API Key authentication
        
        Parameters
        ----------
        apiKey : str
            The [Lockstep Platform API 
            key](https://developer.lockstep.io/docs/api-keys) to use for 
            authentication.
        """
        self.apiKey = apiKey
        self.bearerToken = None
    
    def with_bearer_token(self, bearerToken: str):
        """Configure this API client to use Bearer Token authentication
        
        Parameters
        ----------
        bearerToken : str
            The [Lockstep Platform JWT Bearer 
            Token](https://developer.lockstep.io/docs/jwt-bearer-tokens) to use 
            for authentication.
        """
        self.apiKey = None
        self.bearerToken = bearerToken
    
    def send_request(self, method: str, path: str, body: object, query_params: object) -> LockstepResponse:
        """Send a request and parse the result
        
        Parameters
        ----------
        method : str
            The HTTP method for this request
        path : str
            The path of the API endpoint for this request
        body : object
            For POST, PUT, or PATCH, represents the body of the request. For other
            requests, this value should be nil.
        query_params : object
            The list of query parameters for the request
        """
        if query_params:
            url = urllib.parse.urljoin(self.serverUrl, path) + "?" + urllib.parse.urlencode(query_params)
        else:
            url = urllib.parse.urljoin(self.serverUrl, path)
        
        headers = {"Accept": "application/json",
                   "SdkName": self.sdkName,
                   "SdkVersion": self.sdkVersion,
                   "MachineName": self.machineName,
                   "ApplicationName": self.applicationName}
        if self.apiKey:
            headers["Api-Key"] = self.apiKey
        elif self.bearerToken:
            headers["Authorization"] = "Bearer " + self.bearerToken
    
        response = requests.request(method, url, headers=headers)
        return response.json()
        
