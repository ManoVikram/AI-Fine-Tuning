# Note: This script is not perfect and may break based on the model's output.

import json
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

def generate_data_example(topic, style):
    prompt = f"""Create ONE training data example for fine-tuning.

    Topic: {topic}
    Style: {style}

    Output format (EXACTLY):
    {{"messages": [{{"role": "system", "content": "You are an AI mentor who explains concepts simply with analogies."}}, {{"role": "user", "content": "natural question here"}}, {{"role": "assistant", "content": "detailed answer here"}}]}}

    Rules:
    - Use no special characters
    - Use only the characters that are accepted in JSON
    - Ensure the JSON is valid
    - Do NOT add any extra text outside the JSON
    - Use \\n for newlines inside strings
    - Escape quotes with \\"
    - Or better no escape characters at all
    - Keep code examples on single lines or use \\n
    - Output ONLY valid JSON, nothing else
    
    Just output the JSON, nothing else.
    """

    client = Anthropic()
    response = client.messages.create(
        model="claude-3-5-haiku-latest",
        max_tokens=1500,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text.strip()

if __name__ == "__main__":
    domain = "Applied AI"

    topics = [
        "Applied vs Traditional AI",
        "LLMs",
        "Generative AI",
        "AI ecosystem",
        "Tokens",
        "Temperature",
        "TopP",
        "Context length",
        "Prompt engineering",
        "Prompt design strategies - role, context, constraints",
        "Chain of thought",
        "Reasoning prompts",
        "Cost optimization",
        "SDK / API errors & retries",
        "Rate limits",
        "Batch requests",
        "GPT vs Claude vs Open source models",
        "Hugging face",
        "Stable Diffusion",
        "DALL-E",
        "Prompting for images",
        "Combining text and image generation",
        "Safety filters for images",
        "Speech to text",
        "Text to speech",
        "Audio summarization",
        "LangChain",
        "Chains",
        "Agents",
        "Tools",
        "Multi-step reasoning and planning",
        "Tool calling",
        "Fine-tuning",
        "Data preparation for fine-tuning",
        "Using LLMs with relational data",
        "SQL generation with natural language",
        "Deploying AI apps on AWS / GCP",
        "Using docker for portability",
        "n8n",
        "Mid-journey",
        "ElevenLabs",
        "AI avatars",
        "GPT Image",
        "Nano Banana",
        "RAG",
        "Guardrails, Safety & Output Control",
        "Product & UX Patterns for AI Apps",
        "Observing AI and monitoring",
        "Vector DB",
        "Embeddings and semantic search",
        "Long context handling",
        "Structured output",
    ]

    style = """
    - Use simple analogies (like comparing to everyday things)
    - Include code examples when relevant
    - Explain like teaching a friend, not a textbook
    - Keep it practical, avoid theory dumps
    - Add "Pro tip" at the end
    """

    examples = []

    for i, topic in enumerate(topics, 1):
        print(f"Generating example {i}/{len(topics)} on topic: {topic}")
        
        json_str = generate_data_example(topic=topic, style=style)
        
        json_str = json_str.replace("```json", "").replace("```", "").strip()
        
        example = json.loads(json_str)
        examples.append(example)

        with open("fine_tuning_dataset_1.jsonl", "w") as jsonl_file:
            for example in examples:
                jsonl_file.write(json.dumps(example) + "\n")

        print(f"✅ Created {len(examples)} examples!\n")
