import base64
import pyperclip
import os

def main():
    file_path = "/Path/to/Your/Audio_file.mp3"
    audio_file = os.path.basename(file_path)
    with open(file_path, "rb") as audio:
        encoded_string = base64.b64encode(audio.read()).decode()

    if file_path.endswith('.mp3'):
        data_uri = 'data:audio/mp3;base64,' + encoded_string

    elif file_path.endswith('.wav'):
        data_uri = 'data:audio/wav;base64,' + encoded_string

    else:
        print("Error : Audio file format not supported.")
        return

    print('Data URI :\n', data_uri)
    pyperclip.copy(data_uri)
    print('The URI data chain was copied to the clipboard.')
    save_to_file(data_uri, audio_file)

def save_to_file(data_uri, audio_file):
    file_name = 'Base64|' + audio_file
    if not file_name.endswith('.txt'):
        file_name = file_name + '.txt'
    directory = "/Output/Path/"
    file_path = os.path.join(directory, file_name)
    with open(file_path, "w") as file:
        file.write(data_uri)
    print("Data URI saved at : ", file_path)

main()
