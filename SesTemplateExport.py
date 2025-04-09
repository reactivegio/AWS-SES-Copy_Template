import os
import boto3

session = boto3.Session(profile_name="<my_profile>")
ses_client = session.client('ses')

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "SES_Templates")

# If the directory not exist, create it
if not os.path.exists(desktop_path):
    os.makedirs(desktop_path)

# Pagination parameter
next_token = None

# Until pages exist
while True:
    try:
        # Ses call to get template list
        if next_token:
            response = ses_client.list_templates(NextToken=next_token)
        else:
            response = ses_client.list_templates()

        for template in response['TemplatesMetadata']:
            template_name = template['Name']

            try:
                template_response = ses_client.get_template(TemplateName=template_name)
                template_data = template_response['Template']

                # Create a dir for each template
                template_folder = os.path.join(desktop_path, template_name)
                if not os.path.exists(template_folder):
                    os.makedirs(template_folder)

                with open(os.path.join(template_folder, f"{template_name}.txt"), 'w') as f:
                    f.write(f"Template Name: {template_data['TemplateName']}\n")
                    f.write(f"Subject: {template_data['SubjectPart']}\n\n")
                    f.write("HTML Body:\n")
                    f.write(template_data['HtmlPart'])
                    f.write("\n\nText Body:\n")
                    f.write(template_data['TextPart'])

            except Exception as e:
                print(f"Error retrieve '{template_name}': {e}")

        # exists other pages?
        next_token = response.get('NextToken')

        # no more pages
        if not next_token:
            break
        
    except ses_client.exceptions.Throttling:
        print("Throttling error, wait before retry...")
        time.sleep(5) 
        continue

print("Process completated!")
