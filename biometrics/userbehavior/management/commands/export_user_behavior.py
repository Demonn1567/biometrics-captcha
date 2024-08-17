import csv
from django.core.management.base import BaseCommand
from userbehavior.models import UserBehavior

class Command(BaseCommand):
    help = 'Export user behavior data to a CSV file'

    def handle(self, *args, **kwargs):
        # Define the file name and open the file
        with open('user_behavior_data.csv', 'w', newline='') as csvfile:
            # Create a CSV writer
            writer = csv.writer(csvfile)

            # Write the header
            writer.writerow(['User ID', 'Behavior Data', 'Browser Info', 'IP Address', 'Timestamp'])

            # Write data rows
            for behavior in UserBehavior.objects.all():
                writer.writerow([
                    behavior.user_id,
                    behavior.behavior_data,
                    behavior.browser_info,
                    behavior.ip_address,
                    behavior.timestamp
                ])

        self.stdout.write(self.style.SUCCESS('Successfully exported data to user_behavior_data.csv'))
