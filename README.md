# GVE_DevNet_Meraki_MX_WAN_Interface_Detail_Reporter
prototype script that collects relevant networking information from the wan interfaces of MX devices across all the organizations and stores it into a csv file. 


## Contacts
* Jorge Banegas

## Solution Components
* Meraki
*  MX

### Prerequisites
* Meraki API Key
* Python installed

## Installation/Configuration

1. The first is to generate a Meraki API key from the Meraki Dashboard if you have not already. This link will show you how you can generate a Meraki API token.

https://documentation.meraki.com/General_Administration/Other_Topics/Cisco_Meraki_Dashboard_API

2. Once the Meraki API key is available, enter the key into the config.py file of the project folder. 
```python
key=''
```
3. Install the python packages. 
```python
pip install -r requirements.txt
```

4. Run the script and once the script is finished running, it generates a csv file called report.csv


## Usage
    $ python3 main.py

## Additional Information
list of header names that is used for the csv file
* network_name, MX model
* serial,modem,cellular_ip_address
* carrier,cell_connected
* cell_active?
* device_public_ip,public_wan_1,public_wan_2_ip,wan_1_ip,w1_static_ip,w1_gateway,
* wan_2_ip,w2_static_ip,w2_gateway,
* last_checkin,uplink_state_json,time

# Preview of the CSV file
![/IMAGES/screenshot.jpg](/IMAGES/screenshot.jpg)



![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
