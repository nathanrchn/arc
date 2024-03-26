# Report
## Arc MAX ai api endpoint
The following Arc MAX features uses this api endpoint to access AI services (`https://open-ai-chat-omega.vercel.app`):
1. Ask on Page
2. 5 Second Previews
3. Instant links

Theses features uses two different endpoints to access the AI services:
1. `https://open-ai-chat-omega.vercel.app/api/open-ai-chat-stream` for OpenAI models
2. `https://open-ai-chat-omega.vercel.app/api/claude-stream` for Anthropic models

None of theses endpoints are protected against parallel requests (I tested up to 100 parallel requests). I used the same user JWT token for all the requests.

Also theses endpoints are weakly protected against multiples modifications of the request body.

### OpenAI models (/api/open-ai-chat-stream endpoint)
The model used can be modified: `gpt-4`, `gpt-4-turbo-preview`, `gpt-3.5-turbo` (the default one is: `gpt-3-5-turbo-browser-company`). The only restriction is the gpt-4 vision models are not allowed (`gpt-4-vision-preview`).
The `max_tokens`, `stop`, `temperature` parameters can be set to arbitrary values.
We can even add `tools`.
The `messages` can be modified but the system prompt must allways start with the first sentence of the system prompt.
- `"You are a perfect editor, summarizer and translator"` for the `renamePinnedTabs` feature
- `"You are an expert research assistant."` for the `please` feature
- `"As a concise and helpful summarizer, create a glanceable \"answer card\" containing the most important information from the webpage."` for the `hoverCards` feature

### Anthropic models (/api/claude-stream endpoint)
The model used can be modified: `claude-3-opus-20240229`, `claude-3-sonnet-20240229`, `claude-3-haiku-20240307`, `claude-2.1`, `claude-2.0` (the default one is: `claude-instant-v1`).
The `max_tokens_to_sample`, `stop_sequences`, `temperature` parameters can be set to arbitrary values.
The `prompt` can be modified but the content must start with the first sentence of the system prompt.
- `"Human: You will be acting as a research assistant. I will give you the content of a webpage, and you will concisely answer questions from a human using information from that page."` for the `askInPage` feature