import mysql.connector
from tkinter import *
from tkinter import messagebox
import sounddevice
from scipy.io.wavfile import write
import soundfile
from tkinter import filedialog
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import speech_recognition as sr
class AdminHome:
    def __init__(self,master):
        self.master=master
        self.duration=StringVar()
        self.fpath=StringVar()
        self.lbl_text=StringVar()

        self.lbl_text.set("waiting")
        #master1 = Toplevel()
        master.title("Admin Home")
        master.state("zoomed")
        large_font = ('Verdana', 25)

        lbl_2 = Label(master, text="Duration", height=2, width=20, font=large_font).place(x=700, y=10)
        dur = Entry(master,textvariable=self.duration, width=3, font=large_font).place(x=1000, y=20)
        #dur = Entry(master, text="Select a Voice...", width=20, font=large_font).place(x=400, y=20)
        sbmitbtn = Button(master, text="RECORD VOICE", height = 2, width = 20,font=large_font,command=self.recordvoice ).place(x=700, y=75)
        lbl = Label(master, text="Select a Voice...", height=2, width=20, font=large_font).place(x=700, y=200)
        voice_emotion = Label(master,textvariable=self.lbl_text, text="Emotion...", height=2, width=20, font=large_font).place(x=100, y=200)
        txt = Entry(master,textvariable=self.fpath, width=20, font=large_font).place(x=700, y=300)
        browse = Button(master, text="Browse",  font=large_font,command=self.browsefunc).place(x=1150, y=300)
        emotion = Button(master, text="VIEW EMOTION", height=2, width=20, font=large_font,command=self.viewemotion).place(x=700, y=400)
        ext = Button(master, text="Exit", height=2, width=20, font=large_font,command=master.destroy).place(x=700, y=550)
        master.mainloop()

    def recordvoice(self):
        print("record")
        tme = int(self.duration.get().strip())
        print("Time:", tme)
        fs = 44100
        # second = int(input("Enter time duration in seconds: "))
        print("Recording.....n")
        # record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
        record_voice = sounddevice.rec(int(tme * fs), samplerate=fs, channels=2)
        sounddevice.wait()
        write("out.wav", fs, record_voice)
        print("Finished.....nPlease check your ou1tput file")
        data, samplerate = soundfile.read('out.wav')
        soundfile.write('new.wav', data, samplerate, subtype='PCM_16')
        messagebox.showinfo("Record", "Voice recording finished...")

    def browsefunc(self):
        print("browse here")
        #data = self.fpath.get().strip()
        #print("Path entry...:",data)
        #global voice_emotion
        try:
            filename = str(filedialog.askopenfilename())
            print("Filepath:",filename)
            self.fpath.set(filename)
            #self.lbl_text.set("hai.... bye...")
        except:
            messagebox.showinfo("Alert", "only wave files supported...")

    def viewemotion(self):
        print("started...")
        path=self.fpath.get().strip()
        print(path)
        # Initialize recognizer class (for recognizing the speech)
        r = sr.Recognizer()

        # Reading Audio file as source
        # listening the audio file and store in audio_text variable
        with sr.AudioFile(path) as source:
            audio_text = r.listen(source)

            # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
            try:

                # using google speech recognition
                text = r.recognize_google(audio_text)
                print('Converting audio transcripts into text ...')
                print(text)

                paragraph=text


                lines_list = tokenize.sent_tokenize(paragraph)
                print(lines_list)


                NEG=NEU=POS=0

                for sentence in lines_list:
                    sid = SentimentIntensityAnalyzer()
                    # print(sentence)

                    ss = sid.polarity_scores(sentence)
                    # print(ss)
                    k = ss.keys()
                    p = list(k)
                    # print("P=",p)

                    print("Negative:", ss.get(p[0]), ",Neutral:", ss.get(p[1]), ",Positive:", ss.get(p[2]), ",Sent:",  sentence)
                    NEG=NEG+ss.get(p[0])
                    NEU=NEU+ss.get(p[1])
                    POS=POS+ss.get(p[2])
                if NEG > NEU:
                    if NEG > POS:
                        print("Negative Emotion",NEG*100,"%")
                    else:
                        print("Positive Emotion",POS*100,"%")
                else:
                    if NEU>POS:
                        print("Neutral Emotion",NEU*100,"%")
                    else:
                        print("Positive Emotion",POS*100,"%")

            except:
                print('Sorry.. run again...')

#cp=Tk()
#w=AdminHome(cp)