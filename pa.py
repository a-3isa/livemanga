import torch
import torchaudio
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
import os

print("Loading model...")
config = XttsConfig()
config.load_json("D:\XTTS_ft_colab-20231223T173409Z-001\XTTS_ft_colab/config.json")
model = Xtts.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir="D:\XTTS_ft_colab-20231223T173409Z-001\XTTS_ft_colab")
model.cuda()

print("Computing speaker latents...")
for reader_voice in os.listdir("reader_voices"):
    gpt_cond_latent, speaker_embedding = model.get_conditioning_latents(audio_path=[f'./reader_voices/{reader_voice}'])

    print("Inference...")
    out = model.inference(
        "It took me quite a long time to develop a voice and now that I have it I am not going to be silent",
        "en",
        gpt_cond_latent,
        speaker_embedding,
        temperature=0.7, # Add custom parameters here
    )
    torchaudio.save(f"D:\liveManga\done\livemanga\speech_models/{reader_voice}", torch.tensor(out["wav"]).unsqueeze(0), 24000)