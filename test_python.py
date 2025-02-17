import requests
HF_API_KEY = "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"
hf_url = "https://api-inference.huggingface.co/models/Vamsi/T5_Paraphrase_Paws"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}
prompt = f"Rewrite the following sentence to sound more polite: 'give me water'"
payload = {"inputs": prompt}
response = requests.post(hf_url, headers=headers, json=payload)
print(response.json())