def format_prompt(code: str, prompt_template: str) -> str:
    """Format the code into the prompt template."""
    return prompt_template.format(code=code.strip())

def style_documentation(content: str) -> str:
    """Add styling markers for better readability."""
    lines = content.split('\n')
    styled_lines = []
    
    for line in lines:
        # Major headings
        if line.strip().endswith(':') and len(line.strip().split()) <= 3:
            styled_lines.append(f"\n{'='*60}\n{line.upper()}\n{'='*60}")
        # Bullet points
        elif line.strip().startswith('•') or line.strip().startswith('-'):
            styled_lines.append(f"  {line.strip()}")
        # Regular paragraphs
        else:
            styled_lines.append(line)
    
    # Join and clean up excessive newlines
    result = '\n'.join(styled_lines)
    
    # Replace multiple newlines with max 2
    while '\n\n\n' in result:
        result = result.replace('\n\n\n', '\n\n')
    
    return result.strip()


