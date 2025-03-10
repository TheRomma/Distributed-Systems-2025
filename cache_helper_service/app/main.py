from openai import OpenAI
import json
import os
from fastapi import FastAPI
import requests

#OpenAI client.
client = OpenAI(
	api_key = os.getenv("API_KEY", "my_key")
)

#Example inputs and outputs given as a guide for OpenAI to help translate natural language prompts into arguments for the content distribution service.
examples = '''
		"input" : "Could you cache the following video [given_link] with the following title [given_title]?"
		"output" : {req=[{"link" : "given_link", "title" : "given_title"}]}
		"input" : "Cache [given_link] with the title [given_title]."
		"output" : {req=[{"link" : "given_link", "title" : "given_title"}]}
		"input" : "Could you remove [given_filename] from the cache?"
		"output" : {req=[{"filename" : "given_filename"}]}
		"input" : "Remove [given_filename]."
		"output" : {req=[{"filename" : "given_filename"}]}
		"input" : "Remove [given_filename] and [another_filename]."
		"output" : {req=[{"filename" : "given_filename"}, {"filename" : "another_filename"}]}
'''

#Fastapi init.
app = FastAPI()

@app.post("/prompt")
async def process_message(req: str):
	prompt = "Translate the following request into a dictionary and do not include the input: " + examples + "\nRequest: " + req

	response = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
		max_tokens=50
	)

	result = json.loads(response.choices[0].message.content)
	for thing in result['req']:
		if "link" in thing and "title" in thing:
			#Send message to /add.
			print(thing)
			resp = requests.post("http://content-distribution-service-service:8123/add", params=thing)
		elif "filename" in thing:
			#Send message to /remove.
			print(thing)
			resp = requests.post("http://content-distribution-service-service:8123/remove", params=thing)
		else:
			print("Could not interpret instructions!")
			
	return {"status": response.choices[0].message.content}
