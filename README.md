DisPydactyl
======

DisPydactyl is working fork of pydactyl. This module has been tested with the new Pterodactyl V1 API and is constantly being updated. If any problem arises please make an issue on Github. This module still uses the pydactyl [documentation](https://pydactyl.readthedocs.io/en/latest/) and a rewritten one will be coming soon!


## Installation

To install this module simply run the command ``pip install git+https://github.com/Dishit79/DisPydactyl.git#egg=Dis-pydactyl``


## Example of Account Creation

```python
from dispydactyl import PterodactylClient

client = PterodactylClient('http://mypanel.com', 'API KEY')
        json_data = client.user.create_user(username ,email , first_name, last_name, external_id=None, password=password, root_admin=False, language='en')
        #returns json data on the newly created user
        print(json_data)
             
```
