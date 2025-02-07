from kokoro import KPipeline
import soundfile as sf 

pipeline = KPipeline(lang_code='a') # <= make sure lang_code matches voice

# 4️⃣ Generate, display, and save audio files in a loop.
def convert(text):
    generator = pipeline(
        text, voice='af_heart', # <= change voice here
        speed=1.2, split_pattern=r'\n+'
    )

    for i, (gs, ps, audio) in enumerate(generator):
        print(i)  # i => index
        print(gs) # gs => graphemes/text
        print(ps) # ps => phonemes
        sf.write(f'files/{i}.wav', audio, 24000) # save each audio file
    
