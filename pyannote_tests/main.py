from pyannote.audio import Pipeline
import time
import os

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.0",
    use_auth_token=os.environ.get("API_TOKEN"),
)

# Add audio files to the chunks directory (I was using 30s chunks of 2 hours of audio)
chunks = os.listdir("./chunks")

# Sort by 00, 01, 02, ..., 10, 11, 12, ...
chunks.sort()

"""
Process each chunk; this approach is not feasible for
production, assigned speaker # is not consistent across chunks
But it's a good way to test performance and accuracy
"""
for chunk in chunks:
    print(f"Processing {chunk}...")

    start = time.perf_counter()

    diarization = pipeline(f"./chunks/{chunk}")

    for turn, _, speaker in diarization.itertracks(yield_label=True):
        print(f"start={turn.start:.1f}s stop={turn.end:.1f}s {speaker}")

        # Save the speaker label to a file
        with open(f"./chunks/{chunk}.txt", "a") as f:
            f.write(f"{turn.start:.1f},{turn.end:.1f},{speaker}\n")

