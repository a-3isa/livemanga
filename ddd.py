# with open ("speakers.txt",'r') as g:
#     print(g.readlines()[0])
g=open("speakers.txt",'r').read().splitlines()
print(g[0])
# print(os.system("""tts --model_name "tts_models/multilingual/multi-dataset/xtts_v2"  --list_speaker_idxs"""))



