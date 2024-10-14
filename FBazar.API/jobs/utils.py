from django.shortcuts import render
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Job, Contract
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from reportlab.lib.units import inch

# def generate_contract_pdf(request, contract_id):
#     # Retrieve the Job and Contract data from your models
#     # job = Job.objects.get(pk=job_id)
#     contract = Contract.objects.get(id=contract_id)
#     job = contract.job


#     # Create a response object with appropriate PDF headers
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="contract_{job.id}.pdf"'

#     # Create the PDF content using ReportLab
#     p = canvas.Canvas(response, pagesize=letter)

#     # Title
#     p.setFont("Helvetica-Bold", 16)
#     p.drawCentredString(300, 770, 'Freelance Bazar Task Contract')

#     # Contract Details
#     p.setFont("Helvetica", 12)
#     y_position = 750

#     # Task Details
#     p.drawString(50, y_position, 'Contract Details:')
#     y_position -= 15
#     p.drawString(50, y_position, f'1. Task ID: {job.id}')
#     y_position -= 15
#     p.drawString(50, y_position, f'2. Task Name: {job.title}')
#     y_position -= 15
#     p.drawString(50, y_position, f'3. Task Description: {job.description}')
#     y_position -= 25

#     # Parties
#     p.drawString(50, y_position, 'Parties:')
#     y_position -= 15
#     p.drawString(70, y_position, 'Client:')
#     y_position -= 15
#     p.drawString(90, y_position, f'  - Username: {contract.client.username}')
#     y_position -= 15
#     p.drawString(90, y_position, f'  - Full Name: {contract.client.name}')
#     y_position -= 15
#     p.drawString(70, y_position, 'Freelancer:')
#     y_position -= 15
#     p.drawString(90, y_position, f'  - Username: {contract.freelancer.username}')
#     y_position -= 15
#     p.drawString(90, y_position, f'  - Full Name: {contract.freelancer.name}')
#     y_position -= 25

#     # Contract Terms
#     p.drawString(50, y_position, 'Contract Terms:')
#     y_position -= 15
#     p.drawString(70, y_position, f'3. Price: The agreed-upon price for the task is {job.budget} Uzbek soums.')
#     y_position -= 15
#     p.drawString(70, y_position, f'4. Duration: The duration for completing the task is {job.duration} days.')
#     y_position -= 25

#     # Contractual Agreements
#     p.drawString(50, y_position, 'Contractual Agreements:')
#     y_position -= 15
#     p.drawString(70, y_position, '5. Scope of Work:')
#     y_position -= 15
#     p.drawString(90, y_position, f'  - The Freelancer agrees to complete the task as described in the task details.')
#     y_position -= 15
#     p.drawString(70, y_position, '6. Payment and Settlement:')
#     y_position -= 15
#     p.drawString(90, y_position, f'  - Payment details and settlement terms are agreed upon independently between the Client and Freelancer.')
#     y_position -= 15
#     p.drawString(70, y_position, '7. Communication:')
#     y_position -= 15
#     p.drawString(90, y_position, f'  - Important communication regarding the task must occur within the Freelance Bazar messaging system for record-keeping.')
#     y_position -= 15
#     p.drawString(90, y_position, f'  - The assignment letter, progress updates, and final files related to the task should be shared and documented exclusively within the platform\'s internal communication channel.')
#     y_position -= 15
#     p.drawString(90, y_position, f'  - External communication through other messengers is allowed but may not serve as proof of work or communication.')
#     y_position -= 25

#     # Prohibited Content
#     p.drawString(50, y_position, 'Prohibited Content:')
#     y_position -= 15
#     p.drawString(70, y_position, '8. Prohibited Content:')
#     y_position -= 15
#     p.drawString(90, y_position, '  - Both parties acknowledge that it is strictly prohibited to include content in the task that involves or promotes pornography, violence, hate speech, discrimination, illegal activities, politically biased content, or any material that violates the laws and regulations of the Republic of Uzbekistan or any relevant jurisdiction.')
#     y_position -= 25

#     # Governing Law
#     p.drawString(50, y_position, 'Governing Law:')
#     y_position -= 15
#     p.drawString(70, y_position, '9. Governing Law:')
#     y_position -= 15
#     p.drawString(90, y_position, '  - This Contract is governed by and construed in accordance with the laws of the Republic of Uzbekistan.')
#     y_position -= 25

#     # Contact Information
#     p.drawString(50, y_position, 'Contact Information:')
#     y_position -= 15
#     p.drawString(70, y_position, '10. Contact:')
#     y_position -= 15
#     p.drawString(90, y_position, f'  - For inquiries or concerns related to this Contract, contact aaaa@aaa.com.')
#     y_position -= 25

#     # Agreement
#     y_position -= 15
#     p.drawString(50, y_position, 'Agreement:')
#     y_position -= 15
#     p.drawString(70, y_position, 'By accepting this task and entering into this Contract, both parties acknowledge that they have read, understood, and agree to abide by the terms outlined in this Task Contract. If there are any disagreements with any part of these terms, parties should communicate promptly.')
#     y_position -= 25

#     # Platform Information
#     p.drawString(50, y_position, 'Freelance Bazar')
#     y_position -= 15
#     p.drawString(70, y_position, '[Address]')
#     y_position -= 15
#     p.drawString(70, y_position, '[Date]')
#     y_position -= 25

#     # # Signatures
#     # y_position -= 15
#     # p.drawString(50, y_position, 'Client\'s Signature: Signed')
#     # y_position -= 15
#     # p.drawString(50, y_position, 'Freelancer\'s Signature: _______________________')

#     # Save the PDF content
#     p.showPage()
#     p.save()

#     return response

def generate_contract_pdf(request, contract_id):
    # Retrieve the Job and Contract data from your models
    contract = Contract.objects.get(id=contract_id)
    job = contract.job

    # Create a response object with appropriate PDF headers
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="contract_{job.id}.pdf"'

    # Create the PDF content using ReportLab
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Title
    p.setFont("Helvetica-Bold", 16)
    p.drawCentredString(width / 2.0, height - 1 * inch, 'Freelance Bazar Task Contract')

    # Contract Details
    p.setFont("Helvetica", 12)
    y_position = height - 1.25 * inch
    line_height = 14
    margin = 0.75 * inch
    page_bottom = margin

    def draw_text_block(text, x, y, max_width):
        lines = []
        for line in text.split('\n'):
            while line:
                split_index = len(line)
                while p.stringWidth(line[:split_index], "Helvetica", 12) > max_width:
                    split_index -= 1
                if split_index == len(line):
                    lines.append(line)
                    break
                else:
                    while line[split_index] != ' ' and split_index > 0:
                        split_index -= 1
                    lines.append(line[:split_index])
                    line = line[split_index+1:]
        for line in lines:
            if y <= page_bottom:
                p.showPage()
                y = height - margin
                p.setFont("Helvetica", 12)
            p.drawString(x, y, line)
            y -= line_height
        return y

    # Helper function to draw a section title
    def draw_section_title(title, y):
        p.setFont("Helvetica-Bold", 12)
        y = draw_text_block(title, margin, y, width - 2 * margin)
        p.setFont("Helvetica", 12)
        return y

    y_position = draw_section_title('Contract Details:', y_position)
    y_position = draw_text_block(f'1. Task ID: {job.id}', margin, y_position, width - 2 * margin)
    y_position = draw_text_block(f'2. Task Name: {job.title}', margin, y_position, width - 2 * margin)
    y_position = draw_text_block(f'3. Task Description: {job.description}', margin, y_position, width - 2 * margin)
    y_position -= line_height

    y_position = draw_section_title('Parties:', y_position)
    y_position = draw_text_block('Client:', margin, y_position, width - 2 * margin)
    y_position = draw_text_block(f'  - Username: {contract.client.username}', margin + 20, y_position, width - 2 * margin)
    y_position = draw_text_block(f'  - Full Name: {contract.client.name}', margin + 20, y_position, width - 2 * margin)
    y_position = draw_text_block('Freelancer:', margin, y_position, width - 2 * margin)
    y_position = draw_text_block(f'  - Username: {contract.freelancer.username}', margin + 20, y_position, width - 2 * margin)
    y_position = draw_text_block(f'  - Full Name: {contract.freelancer.name}', margin + 20, y_position, width - 2 * margin)
    y_position -= line_height

    y_position = draw_section_title('Contract Terms:', y_position)
    y_position = draw_text_block(f'3. Price: The agreed-upon price for the task is {job.budget} Uzbek soums.', margin, y_position, width - 2 * margin)
    y_position = draw_text_block(f'4. Duration: The duration for completing the task is {job.duration} days.', margin, y_position, width - 2 * margin)
    y_position -= line_height

    y_position = draw_section_title('Contractual Agreements:', y_position)
    y_position = draw_text_block('5. Scope of Work:', margin, y_position, width - 2 * margin)
    y_position = draw_text_block(f'  - The Freelancer agrees to complete the task as described in the task details.', margin + 20, y_position, width - 2 * margin)
    y_position = draw_text_block('6. Payment and Settlement:', margin, y_position, width - 2 * margin)
    y_position = draw_text_block(f'  - Payment details and settlement terms are agreed upon independently between the Client and Freelancer.', margin + 20, y_position, width - 2 * margin)
    y_position = draw_text_block('7. Communication:', margin, y_position, width - 2 * margin)
    y_position = draw_text_block(f'  - Important communication regarding the task must occur within the Freelance Bazar messaging system for record-keeping.', margin + 20, y_position, width - 2 * margin)
    y_position = draw_text_block(f'  - The assignment letter, progress updates, and final files related to the task should be shared and documented exclusively within the platform\'s internal communication channel.', margin + 20, y_position, width - 2 * margin)
    y_position = draw_text_block(f'  - External communication through other messengers is allowed but may not serve as proof of work or communication.', margin + 20, y_position, width - 2 * margin)
    y_position -= line_height

    y_position = draw_section_title('Prohibited Content:', y_position)
    y_position = draw_text_block('8. Prohibited Content:', margin, y_position, width - 2 * margin)
    y_position = draw_text_block(f'  - Both parties acknowledge that it is strictly prohibited to include content in the task that involves or promotes pornography, violence, hate speech, discrimination, illegal activities, politically biased content, or any material that violates the laws and regulations of the Republic of Uzbekistan or any relevant jurisdiction.', margin + 20, y_position, width - 2 * margin)
    y_position -= line_height

    y_position = draw_section_title('Governing Law:', y_position)
    y_position = draw_text_block('9. Governing Law:', margin, y_position, width - 2 * margin)
    y_position = draw_text_block(f'  - This Contract is governed by and construed in accordance with the laws of the Republic of Uzbekistan.', margin + 20, y_position, width - 2 * margin)
    y_position -= line_height

    y_position = draw_section_title('Contact Information:', y_position)
    y_position = draw_text_block('10. Contact:', margin, y_position, width - 2 * margin)
    y_position = draw_text_block(f'  - For inquiries or concerns related to this Contract, contact aaaa@aaa.com.', margin + 20, y_position, width - 2 * margin)
    y_position -= line_height

    y_position = draw_section_title('Agreement:', y_position)
    y_position = draw_text_block('By accepting this task and entering into this Contract, both parties acknowledge that they have read, understood, and agree to abide by the terms outlined in this Task Contract. If there are any disagreements with any part of these terms, parties should communicate promptly.', margin, y_position, width - 2 * margin)
    y_position -= line_height

    y_position = draw_text_block('Freelance Bazar', margin, y_position, width - 2 * margin)
    y_position = draw_text_block('[Address]', margin + 20, y_position, width - 2 * margin)
    y_position = draw_text_block('[Date]', margin + 20, y_position, width - 2 * margin)

    # Save the PDF content
    p.showPage()
    p.save()

    return response
def searchJobs(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    jobObj = Job.objects.distinct().filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    return jobObj, search_query


def paginateProfiles(request, profiles, results):
    page = request.GET.get('page')
    # results = 3
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    left_index = (int(page) - 4)
    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 5)

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)
    return custom_range, profiles
