from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path='test_eng.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print(f'*** Original feli: {Path(file_path).name} ***')
        print(f'*** IN PROGRESS.... ***')
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)
        text = text.replace('\n', '')

        audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        audio.save(f'{file_name}.mp3')

        return f'{file_name}.mp3 is successfully saved to {file_path}.'

    else:
        return 'File does not exist'


def main():
    tprint('PDF >> TO >> MP3',)
    file_path = input('Enter your PDF file path:')
    language = input('Choose language(en, ru):')
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
