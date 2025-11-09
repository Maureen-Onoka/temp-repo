# llm_utils.py
# -----------------------------
# Summarizes text (e.g., README.md) using an OpenAI LLM

from openai import OpenAI

def summarize_readme(text: str) -> str:
    """
    Summarize the README.md content using an LLM.
    """
    if not text.strip():
        return "No README content found."

    try:
        client = OpenAI()
        prompt = f"Summarize the following README into a clear project overview:\n\n{text}"

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional technical writer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=400
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error summarizing README: {e}"
