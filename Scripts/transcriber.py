import os
from youtube_transcript_api import YouTubeTranscriptApi as yta


video_link = "https://youtu.be/TwJX9AHdnQg?si=iutu9D2s-gq3GQT8"


class Transcriber:
    def __init__(self,video_link):
        self.video_id = self.get_video_id(video_link)
        data = self.get_transcript(self.video_id)
        final_data = self.convert_data(data)
        self.transcript = self.process_data(final_data)
        transcript_file = self.write_transript_to_file(self.video_id,self.transcript)

    @staticmethod
    def get_video_id(video_link):
        video_id = video_link.split('v=')[-1].split('&')[0]
        return video_id
    
    def get_transcript(self, youtube_link_id):
        data = yta.get_transcript(youtube_link_id)
        return data

    def convert_data(self, data):
        final_data = ''
        for val in data:
            final_data += val['text'] + ' '
        return final_data
    
    def process_data(self, final_data):
        return final_data.replace('\n', ' ')
    
    def write_transript_to_file(self, video_id, transcript):
        filename = f"{self.video_id}_transcript.txt"
        try:
            with open(filename,'w') as file:
                file.write(self.transcript)
            print(f"Transcript saved to {filename}")

        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")


video_transcript = Transcriber(video_link)

