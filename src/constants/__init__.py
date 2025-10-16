CODE_EXPLANATION_PROMPT = '''
Analyze and explain the following code professionally and concisely.

Requirements:
- Write in clear, flowing paragraphs (not line-by-line)
- Use bullet points only for listing key features or components
- Keep each section under 5 lines
- Use simple, technical language
- Structure with clear headings
- NO code blocks in the explanation
- Focus on what the code does, not how to write it

Code:
{code}

Format your response as:

Overview:
[2-3 sentence paragraph describing the purpose and main functionality]

Key Components:
• [Component 1 and its role]
• [Component 2 and its role]
• [Component 3 and its role]

Technical Implementation:
[2-3 sentence paragraph explaining the approach and important details]

Notable Features:
[1-2 sentence paragraph highlighting special aspects or considerations]
'''








