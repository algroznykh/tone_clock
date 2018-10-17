import os
import time
from datetime import datetime

import pysynth as ps
import schedule


TONES = {
	0: 'e',
	1: 'f',
	2: 'f#',
	3: 'g',
	4: 'g#',
	5: 'a',
	6: 'a#',
	7: 'b',
	8: 'c',
	9: 'c#',
	10: 'd',
	11: 'd#',
}


def play_tone(name, duration):
    tone = ((name, duration),)
    ps.make_wav(tone, fn="tone.wav")
    os.system("aplay tone.wav")
    os.system("rm tone.wav")

	
def gen_tone():
    now = datetime.now()
    if not now.minute % 5:
        play_tone(TONES[int(now.minute / 5)], 2)
    if now.minute == 0:
        hour = now.hour
        if hour >= 12:
            hour = hour - 12
        play_tone(TONES[hour], 1)


def main():
    while True:
        if datetime.now().second == 0:
            schedule.every().minute.do(gen_tone)
            break
	while True:
		schedule.run_pending()
		time.sleep(1)
		print(datetime.now())


if __name__ == '__main__':
	main()

