from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'djangoaccountstorage03' # Must be replaced by your <storage_account_name>
    account_key = 'IOV0vAr3xrefVtdKTiuqce+pzIGzGVtk8uTx//p5aaKRJsChFzx7+63Zh0Y8V/PJ1gMSYL65LZmYA2xXqvGugw==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'djangoaccountstorage03' # Must be replaced by your storage_account_name
    account_key = 'oXO3vjNVZ0y53rPcZCwf8QFXbRUW3uv8FTX/mIgxUkmo7Xar6XVSKfeJYR5jAXkaztnYe1Ytff0EzNUA5qvPlA==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None