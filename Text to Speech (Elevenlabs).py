from elevenlabs import generate, play
 
audio = generate(
  text="Hello! I'm Batman, delighted to make your acquaintance!",
  voice="Bella",
  model="eleven_monolingual_v1"
)
 
play(audio)