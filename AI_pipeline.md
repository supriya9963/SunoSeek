SunoSeek AI Pipeline

 1. Speech-to-Text (STT)
- OpenAI Whisper model converts voice → text.
- Supports Hindi, Telugu, Tamil, Bengali, Marathi, Kannada, Gujarati.

 2. NLP Intent Detection
- Uses Rasa / Transformers-based classifier.
- Example intents:
  - FindJob
  - AskSalary
  - ChangeLocation
  - ConnectEmployer

 3. Job Matching Engine
- Matches based on:
  - Job role
  - Location
  - Skills
  - Past job preferences

 4. Summarization Engine
- Converts long job descriptions into 1–2 line simple summaries.
- Example:
  - "Housekeeping, 8 hours, ₹12,000, food included."

 5. Text-to-Speech (TTS)
- Converts AI response → Voice.
- Uses Google TTS / Azure TTS.

## 6. Delivery Layer
- Sends audio response via WhatsApp or IVR.
