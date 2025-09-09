import boto3  # Import AWS SDK for Python to interact with AWS services

# Create EC2 client to get all AWS regions
ec2 = boto3.client('ec2')  # Connects to EC2 service
regions = [r['RegionName'] for r in ec2.describe_regions()['Regions']]  # Fetch all region names

# Loop through each AWS region
for region in regions:
    ec2_region = boto3.client('ec2', region_name=region)  # Connect to EC2 in the current region
    instance_groups = ec2_region.describe_instances()['Reservations']  # Get all instance reservations in this region

    # Loop through each reservation group
    for group in instance_groups:
        # Loop through each instance in the reservation
        for instance in group['Instances']:
            instance_id = instance['InstanceId']  # Get the unique ID of the instance
            state = instance['State']['Name']  # Get the current state of the instance (running, stopped, etc.)

            # Check instance state and format for readable output with emojis
            if state == 'running':
                state_display = 'running ✅'  # Running instances marked with check emoji
            elif state == 'stopped':
                state_display = 'stopped ⏸️'  # Stopped instances marked with pause emoji
            elif state == 'terminated':
                state_display = 'terminated ❌'  # Terminated instances marked with cross emoji
            else:
                state_display = state  # Keep other states as is

            # Print the instance ID, state, and region
            print(f"Instance ID: {instance_id}, State: {state_display}, Region: {region}")