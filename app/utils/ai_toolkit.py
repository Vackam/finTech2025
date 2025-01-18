# ai_toolkit.py

from openai import OpenAI

import os

client = OpenAI()

def load_prompt():
    # Set Path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "prompt", "insurance.md")

    try: 
        with open(file_path, "r", encoding="utf-8") as file:
            prompt = file.read()
            return prompt
    except FileNotFoundError:
        raise Exception(f"파일을 찾을 수 없습니다: {file_path}")
    
# Export
def get_insurance_model(input_diseases):
    prompt = load_prompt()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {
                "role": "user",
                "content": f"입력: {input_diseases}"
            }
        ]
    )

    return completion.choices[0].message.content

if __name__ == "__main__":
    print(get_insurance_model("에이즈 콜레라"))
