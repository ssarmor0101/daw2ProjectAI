from ia.base import TranslatorIA
import openai

class OpenAITranslator(TranslatorIA):

    def translate(self, text: str, source: str, target: str) -> str:
        prompt = f"Translate from {source} to {target}: {text}"

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content
