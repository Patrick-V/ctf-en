from env import config
import meraki
import stage0
import json

organization_name = "DevNet Sandbox"
network_name = "DevNet Sandbox ALWAYS ON"

dashboard = meraki.DashboardAPI(config['MERAKI_KEY'])

def get_organization_id(organization_name):
    for org in stage0.get_organizations():
        if org['name'] == organization_name:
            organization_id = org['id']
    return organization_id

def get_network_id(network_name, organization_name):
    response = dashboard.organizations.getOrganizationNetworks(get_organization_id(organization_name), total_pages='all')
    for network in response:
        if network['name'] == network_name:
            network_id = network['id']
    return network_id


def get_device_inventory(organization_name):
    response = dashboard.organizations.getOrganizationInventoryDevices(get_organization_id(organization_name), total_pages='all')
    return response

if __name__ == "__main__":
    # Generalizes this for given organization name and network name
    network_id = get_network_id(network_name, organization_name)
    inventory = get_device_inventory(organization_name)

    # Create a relevant inventory with only devices from the relevant network
    relevant_inventory = []

    for device in inventory:
        if device['networkId'] == network_id:
            relevant_inventory.append(device)

    # Removes irrelevant info from desired inventory
    for relevant_device in relevant_inventory:
        relevant_device.pop('networkId')
        relevant_device.pop('claimedAt')
        relevant_device.pop('orderNumber')

    # Writes the relevant inventory to inventory.json
    with open('inventory.json', 'w') as output_file:
        json.dump(relevant_inventory, output_file)
    
    print(f"Inventory for network {network_name} from organization {organization_name} was successfully written to inventory.json!")