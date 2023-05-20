import librosa
import numpy as np

def extract_spectral_flux(audio_file):
    y, sr = librosa.load(audio_file)
    spectral_flux = librosa.onset.onset_strength(y=y, sr=sr)
    return spectral_flux

def extract_features(path, threshold):
    # Load the audio file
    audio, sr = librosa.load(path, sr=None)

    # Calculate the amplitude envelope
    envelope = np.abs(librosa.amplitude_to_db(np.abs(librosa.stft(audio)), ref=np.max))

    # Calculate the spectral flux
    spectral_flux = extract_spectral_flux(path)

    # Normalize the spectral flux
    spectral_flux /= np.max(spectral_flux)

    # Find the frames where the spectral flux exceeds the threshold
    keyword_frames = np.where(spectral_flux > threshold)[0]
 
    # Calculate the average envelope value for each frame
    frame_envelope = [np.mean(envelope[frame]) for frame in keyword_frames]

    return frame_envelope

def result(keyword, comparing_file, threshold):
    # Check if the keyword is present in the comparing file
    for env in comparing_file:
        diff = np.abs(keyword - env)
        if np.any(diff <= threshold):
            return True
    return False

# Example usage
keyword_file_path ="D:/Reuben/SpeechLogix Project/normal voice/pyar.wav"
wav_file_path = "D:/Reuben/SpeechLogix Project/normal voice/hindi_test.wav"
threshold = 0.3

keyword = extract_features(keyword_file_path, threshold)
comparing_file = extract_features(wav_file_path, threshold)

keyword_detected = result(keyword, comparing_file, threshold)

if keyword_detected:
    print("Keyword detected!")
else:
    print("Keyword not found.")
