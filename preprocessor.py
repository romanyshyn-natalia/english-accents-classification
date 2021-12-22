import random
import torch
import torchaudio
import torchaudio.transforms as T


def load_audio(path):
    audio, sr = torchaudio.load(path)
    return audio, sr


def double_channel(sig):
    audio, sr = sig
    if audio.shape[0] == 2:
        return sig
    duplicated = torch.cat([audio, audio])
    return duplicated, sr


def downsample(sig, new_sr=22050):
    audio, sr = sig

    if sr == 22050:
        return sig
    first_channel = T.Resample(sr, new_sr)(audio[:1, :])
    second_channel = T.Resample(sr, new_sr)(audio[1:, :])
    res = torch.cat([first_channel, second_channel])
    return res, new_sr


def append_trunc(sig, milis=3000):
    audio, sr = sig
    rows, audio_len = audio.shape
    max_len = sr // 1000 * milis

    if audio_len > max_len:
        audio = audio[:, :max_len]
    elif audio_len < max_len:
        diff = max_len - audio_len
        append_start_len = random.randint(0, diff)
        append_stop_len = diff - append_start_len
        append_start = torch.zeros((rows, append_start_len))
        append_stop = torch.zeros((rows, append_stop_len))

        audio = torch.cat((append_start, audio, append_stop), 1)
    return audio, sr


def spectro_mfcc(sig):
    audio, sr = sig
    mfcc_transform = T.MFCC(
        sample_rate=sr,
        n_mfcc=64,
        melkwargs={"n_fft": 512, "n_mels": 64, "hop_length": None, "mel_scale": "htk"},
    )
    mfcc = mfcc_transform(audio)
    spec = T.AmplitudeToDB(top_db=80)(mfcc)
    return spec  # shape [channel, n_mels, time]
