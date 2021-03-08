from env import config
import meraki

dashboard = meraki.DashboardAPI(config['MERAKI_KEY'])

def get_organizations():
    response = dashboard.organizations.getOrganizations()
    return response

if __name__ == "__main__": 
    for org in get_organizations():
        print(f"Organization ID {org['id']} has the name {org['name']}")