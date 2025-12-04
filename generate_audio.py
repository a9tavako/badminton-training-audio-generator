import random
from pydub import AudioSegment
from generate_times import get_times
from datetime import datetime

TOTAL_COUNT = 100
timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M")
OUTPUT_FILE_NAME = "Training_Audio_" + timestamp + ".mp3"
sounds = ["1.mp3", "2.mp3", "3.mp3", "4.mp3"]

def generate_audio(total_count:int = TOTAL_COUNT):
    times = get_times(TOTAL_COUNT) 
    beep = AudioSegment.from_mp3("beep.mp3")
    short_silence = AudioSegment.silent(50)
    
    final = AudioSegment.silent(duration=0)

    for delay in times:
        chosen = random.choice(sounds)

        long_silence = AudioSegment.silent(duration=int(delay * 1000))
        clip = AudioSegment.from_mp3(chosen)

        final += long_silence
        final += beep
        final += short_silence
        final += beep
        final += short_silence
        final += clip

    # export the result
    final.export(OUTPUT_FILE_NAME, format="mp3")
    print(f"Created {OUTPUT_FILE_NAME}")

if __name__ == "__main__":
    generate_audio()