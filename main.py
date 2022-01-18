from src.lockstep_api.lockstep_api import LockstepApi
import os


def retrieve_api_key():
    API_KEY = os.environ.get('LockstepAPI_SBX')
    if API_KEY is None:
        print('NO API KEY')
    else:
        print('VALID API KEY FOUND')
        return API_KEY


def create_client(apikey):
    env = 'sbx'
    client = LockstepApi(env)
    client.with_api_key(apikey)
    if not client:
        print("ISSUE WITH CLIENT, NO API KEY OR WRONG ENVIRONMENT")
    else:
        print(f"CLIENT WAS CREATED SUCCESSFULLY: {client}")
        return client


def main():
    api_key = retrieve_api_key()
    client = create_client(api_key)

    # Ping
    status_results = client.status.ping()
    print(f"StatusResult: {status_results}")

    page_num = 0;
    count = 1;

    while True:
        # Single API call to fetch invoices and company info.
        invoices = client.invoices.query_invoices(
            "invoiceDate GT 2021-01-10 AND invoiceDate LT 2021-05-10",
            "Company",
            "invoiceDate asc",
            100,
            page_num)

        if (invoices.status_code != 200) | ((invoices.json()['records']) == 0):
            break

        for record in invoices.json()['records']:
            print(f"Invoice {count}: {record['invoiceId']}")
            print(f"Company name: {record['company']['companyName']}")
            print(f"Outstanding Balance: ${record['outstandingBalanceAmount']} \n")
            count += 1

        page_num += 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()