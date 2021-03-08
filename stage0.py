from env import config
import meraki

dashboard = meraki.DashboardAPI(config['MERAKI_KEY'])
response = dashboard.organizations.getOrganizations()

for org in response:
    print(f"Organization ID {org['id']} has the name {org['name']}")