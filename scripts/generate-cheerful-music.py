#!/usr/bin/env python3
"""Compose an original gentle instrumental loop from synthesized tones.
No recordings, samples, voice synthesis, API calls or third-party music.
"""
from pathlib import Path
import math, wave
import numpy as np
ROOT=Path(__file__).resolve().parent.parent
DEST=ROOT/'assets/source/cheerful-woodland-loop.wav'
RATE=24000; BPM=108; BEAT=60/BPM; BARS=16; LENGTH=BARS*4*BEAT
samples=np.zeros(round((LENGTH+0.04)*RATE),dtype=np.float64)

def tone(start,beats,midi,level=0.10,kind='bell'):
 freq=440*2**((midi-69)/12);length=beats*BEAT
 t=np.arange(round((length+0.2)*RATE))/RATE
 if kind=='bell':
  signal=np.sin(2*np.pi*freq*t)+.24*np.sin(2*np.pi*2*freq*t)+.07*np.sin(2*np.pi*3*freq*t)
  env=(1-np.exp(-t/.009))*np.exp(-t/max(.12,length*.6))
 else:
  signal=np.sin(2*np.pi*freq*t)+.12*np.sin(2*np.pi*2*freq*t)
  env=(1-np.exp(-t/.018))*np.exp(-t/max(.18,length*.8))
 env*=np.clip((length+.2-t)/.15,0,1)
 i=round(start*BEAT*RATE);end=min(len(samples),i+len(t))
 samples[i:end]+=signal[:end-i]*env[:end-i]*level

# Sixteen newly composed bars. Each tuple is (beat offset, pitch, duration in beats).
melody=[
 [(0,76,.75),(1,79,.5),(1.75,81,.75),(3,79,.6)],
 [(0,74,.7),(1,76,.7),(2.5,72,1)],
 [(0,79,.5),(.75,81,.5),(1.5,79,.5),(2.5,76,1)],
 [(0,74,.8),(1.25,72,.7),(3,76,.5)],
 [(0,77,.7),(1,81,.7),(2.5,79,.9)],
 [(0,76,.6),(1,74,.6),(2,72,1.2)],
 [(0,74,.5),(.75,79,.7),(2,81,.5),(3,79,.7)],
 [(0,76,.9),(1.5,74,.6),(2.5,72,1.1)],
 [(0,81,.6),(1,79,.7),(2.5,76,.8)],
 [(0,74,.6),(1,76,.5),(2,79,1)],
 [(0,77,.7),(1,76,.5),(2,74,.6),(3,72,.6)],
 [(0,76,.6),(1,79,.6),(2.5,81,.7)],
 [(0,77,.6),(1,81,.5),(2,79,.8)],
 [(0,76,.5),(.75,74,.5),(1.5,76,.5),(2.5,72,1)],
 [(0,74,.7),(1.25,79,.8),(2.5,76,.6)],
 [(0,74,.6),(1,72,2.4)],
]
chords=[(48,[60,64,67]),(48,[60,64,67]),(55,[59,62,67]),(48,[60,64,67]),(53,[60,65,69]),(48,[60,64,67]),(55,[59,62,67]),(48,[60,64,67])]
for bar,notes in enumerate(melody):
 for beat,note,d in notes:tone(bar*4+beat,d,note,.085,'bell')
 bass,chord=chords[bar%8]
 tone(bar*4,1.6,bass,.07,'soft');tone(bar*4+2,1.5,bass+7,.045,'soft')
 for offset,note in zip([.5,1.5,2.5],chord):tone(bar*4+offset,.9,note,.035,'soft')
# Gentle fade at both loop ends; exact 16-bar duration, no abrupt edges.
samples=samples[:round(LENGTH*RATE)]
fadein=np.minimum(1,np.arange(len(samples))/(RATE*.25));fadeout=np.minimum(1,(len(samples)-np.arange(len(samples)))/(RATE*.6))
samples*=fadein*fadeout
samples*=0.23/max(np.max(np.abs(samples)),1e-9)
pcm=np.clip(samples*32767,-32768,32767).astype('<i2')
DEST.parent.mkdir(parents=True,exist_ok=True)
with wave.open(str(DEST),'wb') as f:f.setnchannels(1);f.setsampwidth(2);f.setframerate(RATE);f.writeframes(pcm.tobytes())
print(f'Original instrumental: {DEST} · {LENGTH:.3f}s · {BPM} BPM · no voice or samples')
