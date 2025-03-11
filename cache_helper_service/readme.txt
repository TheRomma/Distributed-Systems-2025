# Cache Helper Service

The Cache Helper Service creates "add" and "remove" caching messages from natural language prompts using OpenAI. This service a single endpoint /prompt which takes a single argument req containing a natural language prompt such as "Could you cache this video some_link with this title some_title?" or "Could you remove some_filename?".

An environment variable API_KEY must be set in the cache_helper_service.yaml containing a valid OpenAI API key.
