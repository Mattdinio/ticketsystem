from csv import DictReader as dr
from django.core.management import BaseCommand
from ticketingsystem.models import Device


loaded_error_message = """
If you need to reload the device data from the CSV file,
delete the db.sqlite3 file to destroy the database.
Then do a new migration"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "populates device model with data from devicelist.csv"

    def handle(self, *args, **options):
        if Device.objects.exists():
            print('device data already loaded...exiting.')
            print(loaded_error_message)
            return
        print("Creating device data")
        csv = open('.\devicelist.csv', encoding='utf-8-sig')
        reader = dr(csv)
        for row in reader:
            device = Device()
            device.deviceMake = row['Make']
            device.deviceModel = row['Model']
            device.deviceType = row['Type']
            device.description = row['Description']
            device.save()