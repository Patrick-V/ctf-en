from env import config
from dnacentersdk import DNACenterAPI
import meraki
import json

dnac = DNACenterAPI(username = config['DNAC_USER'],
                        password = config['DNAC_PASSWORD'],
                        base_url = config['DNAC_BASE_URL'],
                        version='2.1.2',
                        verify=True)

if __name__ == "__main__":
    inventory = dnac.devices.get_device_list().response
    relevant_inventory = []

    for device in inventory:
        relevant_device = {}

        relevant_device['mac'] = device['macAddress']
        relevant_device['serial'] = device['serialNumber']
        relevant_device['name'] = device['hostname']
        relevant_device['model'] = device['platformId']
        relevant_device['category'] = 'dnac'

        relevant_inventory.append(relevant_device)
    
    # Appends the existing Meraki inventory with DNAC inventory in inventory.json
    with open('inventory.json', 'r+') as output_file:
        existing_inventory = json.load(output_file)
        total_inventory = existing_inventory + relevant_inventory
        json.dump(relevant_inventory, output_file)
    
    print(f"DNAC inventory was successfully written to inventory.json!")
    

        











    
    