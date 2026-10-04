import wave, numpy as np
def read(p):
    w=wave.open(p,'rb'); sr=w.getframerate(); n=w.getnframes(); ch=w.getnchannels()
    a=np.frombuffer(w.readframes(n),dtype=np.int16).astype(np.float32)/32768.0
    if ch>1: a=a.reshape(-1,ch).mean(1)
    return sr,a
def write(p,sr,a):
    w=wave.open(p,'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes((np.clip(a,-1,1)*32767).astype(np.int16).tobytes()); w.close()
