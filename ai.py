from google import genai
from google.genai import types

# GEM_API_KEY = "AIzaSyBHCUty1kcAfQ9zk37lzo2dgUZIdc1JzrA"
GEM_API_KEY = "AIzaSyBmG6pKvp8zdKxA2WqfUXTQFiUfaotNvlg"

def feature(image):
  with open(image, 'rb') as f:
      image_bytes = f.read()
  client = genai.Client(api_key=GEM_API_KEY)
  response = client.models.generate_content(
    # model='gemini-2.5-flash',
    model='gemini-3-flash-preview',
    contents=[
      types.Part.from_bytes(
        data=image_bytes,
        mime_type='image/jpeg',
      ),
      "Analyze the image and detect animals. \n"
      "Determine total animals. \n"
      "Interaction (between animals if more than 1, like playing, chasing, wrestling, bonding, huddling, none). \n"
      "For each animal, estimate the following: \n"
      "- animal_type \n"
      "- mood (happy, calm, aggressive, playful, sleepy, alert) \n"
      "- posture (standing, sitting, lying, jumping) \n"
      "- playfulness_level (0 to 10) \n"
      "- energy_level (0 to 10) \n"
      "- cuteness_level (0 to 10) \n"
      "- bbox: [x, y, w, h] \n"
      "Respond ONLY in valid JSON."
    ]
  )
  text= response.text
  text = text.replace("```json", "").replace("```", "").strip()
  return text