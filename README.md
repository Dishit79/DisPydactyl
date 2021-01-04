DisPydactyl
======

DisPydactyl is working fork of pydactyl. This module has been tested with the new Pterodactyl V1 API and is constantly being updated. If any problem arises make an issue on Github. This module still uses the pydactyl [documentation](https://pydactyl.readthedocs.io/en/latest/) and a rewritten one will be coming soon!


## Installation

To install this module simply run the command ``pip install git+https://github.com/Dishit79/DisPydactyl.git#egg=Dis-pydactyl``


## Example of Account Creation

```python
client = PterodactylClient('http://mypanel.com', 'API KEY')
        e = client.user.create_user(username ,email , first_name, last_name, external_id=None, password=password, root_admin=False, language='en')
        print(e)
        return (True,e['attributes']['id'])
```
