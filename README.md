# Lockstep SDK For Python

![PyPI](https://img.shields.io/pypi/v/lockstep-sdk)

A financial service SDK for python for innovative accounting solutions providers.

### Who are we?

Lockstep automates accounting workflows to improve your operational efficiency and cash flow. Accelerate payments through automated customer communications, enhanced collections activity management, and innovative forecasting and reporting.

# Getting Started

Here's how to add the Lockstep python SDK to your project.

1. Pip install the Lockstep API

```bash
 path\\to\\project\\file: pip install lockstep-sdk
```

2. Obtain an API key for the Lockstep Platform API by visiting: [API Key](https://developer.lockstep.io/docs/api-keys)

3. Creating LockstepAPI Client in your .py file

```python
env = 'PASS_ENVIRONMENT_HERE'
client = LockstepApi(env)
client.with_api_key([INSERT_API_KEY])

if not client:
    print("ISSUE WITH CLIENT, NO API KEY OR WRONG ENVIRONMENT")
else:
    print(f"CLIENT WAS CREATED SUCCESSFULLY: {client}")
    return client
```

4. Make a ping call to make sure you're connected https://developer.lockstep.io/reference/v1_status_retrievestatus

```python
status_results = client.status.ping()
print(f"StatusResult: {status_results}")
```

You now have your API credentials and have successfully created your client.

## How to Use (Basic Usage)

This example will show you how to call an API, using the [Query Invoices API](https://developer.lockstep.io/reference/v1_invoices_queryinvoices) to retrieve a collection of invoices.

```python
# Connect to Client
# Lockstep provides sandbox and production environments
env = 'sbx'
client = LockstepApi(env)

# Add your API key here
client.with_api_key([INSERT_API_KEY])

# Querying for the first 10 invoices sorted by invoice date
invoices = client.invoices.query_invoices(
            "invoiceDate",
            "Company",
            "invoiceDate asc",
            10,
            0)

print(invoices['records'])
```

## Sample Project

[Fetch Invoice Sample Python Project](https://github.com/Lockstep-Network/lockstep-sdk-examples/tree/main/PythonExample)
