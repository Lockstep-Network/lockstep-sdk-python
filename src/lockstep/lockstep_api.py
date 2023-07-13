#
# Lockstep Platform SDK for Python
#
# (c) 2021-2023 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
#             
# @copyright  2021-2023 Lockstep, Inc.
# @version    2023.28.10
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

import platform
import requests
import typing
import urllib.parse

from requests.models import Response

class LockstepApi:
    """
    Lockstep Platform SDK API Client object
    
    Use this object to connect to the API.
    """
    apiKey: str | None
    bearerToken: str | None

    def __init__(self, env: str, appname: str):
        """Construct a new LockstepApi client object
        
        Parameters
        ----------
        env : str
            Select the environment to use for this client. You may either 
            provide an environment name or a full URL of a custom environment.
        appname : str
            Provide a name for your application for logging and debugging. This
            name will be recorded alongside API calls so that you can identify
            the source of errors. 
        """
        from lockstep.clients.apikeys_client import ApiKeysClient
        from lockstep.clients.appenrollments_client import AppEnrollmentsClient
        from lockstep.clients.applications_client import ApplicationsClient
        from lockstep.clients.attachmentlinks_client import AttachmentLinksClient
        from lockstep.clients.attachments_client import AttachmentsClient
        from lockstep.clients.codedefinitions_client import CodeDefinitionsClient
        from lockstep.clients.companies_client import CompaniesClient
        from lockstep.clients.contacts_client import ContactsClient
        from lockstep.clients.creditmemosapplied_client import CreditMemosAppliedClient
        from lockstep.clients.currencies_client import CurrenciesClient
        from lockstep.clients.customfielddefinitions_client import CustomFieldDefinitionsClient
        from lockstep.clients.customfieldvalues_client import CustomFieldValuesClient
        from lockstep.clients.definitions_client import DefinitionsClient
        from lockstep.clients.featureflags_client import FeatureFlagsClient
        from lockstep.clients.financialaccount_client import FinancialAccountClient
        from lockstep.clients.financialaccountbalancehistory_client import FinancialAccountBalanceHistoryClient
        from lockstep.clients.financialinstitutionaccounts_client import FinancialInstitutionAccountsClient
        from lockstep.clients.financialyearsettings_client import FinancialYearSettingsClient
        from lockstep.clients.groupaccounts_client import GroupAccountsClient
        from lockstep.clients.invoiceaddresses_client import InvoiceAddressesClient
        from lockstep.clients.invoicelines_client import InvoiceLinesClient
        from lockstep.clients.invoices_client import InvoicesClient
        from lockstep.clients.leads_client import LeadsClient
        from lockstep.clients.magiclinks_client import MagicLinksClient
        from lockstep.clients.notes_client import NotesClient
        from lockstep.clients.payments_client import PaymentsClient
        from lockstep.clients.paymentsapplied_client import PaymentsAppliedClient
        from lockstep.clients.profilesaccounting_client import ProfilesAccountingClient
        from lockstep.clients.profilesaccountingcontacts_client import ProfilesAccountingContactsClient
        from lockstep.clients.profilescompanies_client import ProfilesCompaniesClient
        from lockstep.clients.provisioning_client import ProvisioningClient
        from lockstep.clients.reports_client import ReportsClient
        from lockstep.clients.status_client import StatusClient
        from lockstep.clients.sync_client import SyncClient
        from lockstep.clients.transactions_client import TransactionsClient
        from lockstep.clients.transcriptions_client import TranscriptionsClient
        from lockstep.clients.useraccounts_client import UserAccountsClient
        from lockstep.clients.userroles_client import UserRolesClient
        from lockstep.clients.webhookrules_client import WebhookRulesClient
        from lockstep.clients.webhooks_client import WebhooksClient
        self.apiKeys = ApiKeysClient(self)
        self.appEnrollments = AppEnrollmentsClient(self)
        self.applications = ApplicationsClient(self)
        self.attachmentLinks = AttachmentLinksClient(self)
        self.attachments = AttachmentsClient(self)
        self.codeDefinitions = CodeDefinitionsClient(self)
        self.companies = CompaniesClient(self)
        self.contacts = ContactsClient(self)
        self.creditMemosApplied = CreditMemosAppliedClient(self)
        self.currencies = CurrenciesClient(self)
        self.customFieldDefinitions = CustomFieldDefinitionsClient(self)
        self.customFieldValues = CustomFieldValuesClient(self)
        self.definitions = DefinitionsClient(self)
        self.featureFlags = FeatureFlagsClient(self)
        self.financialAccount = FinancialAccountClient(self)
        self.financialAccountBalanceHistory = FinancialAccountBalanceHistoryClient(self)
        self.financialInstitutionAccounts = FinancialInstitutionAccountsClient(self)
        self.financialYearSettings = FinancialYearSettingsClient(self)
        self.groupAccounts = GroupAccountsClient(self)
        self.invoiceAddresses = InvoiceAddressesClient(self)
        self.invoiceLines = InvoiceLinesClient(self)
        self.invoices = InvoicesClient(self)
        self.leads = LeadsClient(self)
        self.magicLinks = MagicLinksClient(self)
        self.notes = NotesClient(self)
        self.payments = PaymentsClient(self)
        self.paymentsApplied = PaymentsAppliedClient(self)
        self.profilesAccounting = ProfilesAccountingClient(self)
        self.profilesAccountingContacts = ProfilesAccountingContactsClient(self)
        self.profilesCompanies = ProfilesCompaniesClient(self)
        self.provisioning = ProvisioningClient(self)
        self.reports = ReportsClient(self)
        self.status = StatusClient(self)
        self.sync = SyncClient(self)
        self.transactions = TransactionsClient(self)
        self.transcriptions = TranscriptionsClient(self)
        self.userAccounts = UserAccountsClient(self)
        self.userRoles = UserRolesClient(self)
        self.webhookRules = WebhookRulesClient(self)
        self.webhooks = WebhooksClient(self)
        self.serverUrl = env
        if env == "sbx":
            self.serverUrl = "https://api.sbx.lockstep.io/"
        if env == "prd":
            self.serverUrl = "https://api.lockstep.io/"
        self.sdkName = "Python"
        self.sdkVersion = "2023.28.10"
        self.machineName = platform.uname().node
        self.applicationName = appname
        self.apiKey = None
        self.bearerToken = None
    
    def with_api_key(self, apiKey: str):
        """Configure this API client to use API Key authentication
        
                Authentication is either via [Lockstep Platform API key](https://developer.lockstep.io/docs/api-keys) or [JWT Bearer Token](https://developer.lockstep.io/docs/jwt-bearer-tokens)
        
        Parameters
        ----------
        apiKey : str
            The API Key to use for authentication.
        """
        self.apiKey = apiKey
        self.bearerToken = None
    
    def with_bearer_token(self, bearerToken: str):
        """Configure this API client to use Bearer Token authentication
        
        Authentication is either via [Lockstep Platform API key](https://developer.lockstep.io/docs/api-keys) or [JWT Bearer Token](https://developer.lockstep.io/docs/jwt-bearer-tokens)

        Parameters
        ----------
        bearerToken : str
            The Bearer Token to use for authentication.
        """
        self.apiKey = None
        self.bearerToken = bearerToken
    
    def send_request(self, method: str, path: str, body: object, 
        query_params: typing.Dict[str, typing.Any] | None, filename: str | None) -> Response:
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

        # Determine if we're uploading a file
        files = None
        if filename:
            files = { "files": open(filename, "rb") }

        headers = {"Accept": "application/json",
                   "SdkName": self.sdkName,
                   "SdkVersion": self.sdkVersion,
                   "MachineName": self.machineName,
                   "ApplicationName": self.applicationName}
        if self.apiKey:
            headers["Api-Key"] = self.apiKey
        elif self.bearerToken:
            headers["Authorization"] = "Bearer " + self.bearerToken
    
        return requests.request(method, url, headers=headers, json=body, files=files)
        
