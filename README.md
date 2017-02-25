# UnifyIDRandom

##About
This is a python script that uses the Random.org API to obtain more truly random numbers
and creates sound and image files out of it. Generates a 128x128 bitmap image @random128.png.
Generates a 3 second sound wav @ random3sec.wav

##Setup
In the stable-req.txt file are the python module requirements.
Install these first using pip/pip3 (I'm using python3, and in particular
the anaconda distribution, but these are what I think are necessary regardless)

##Running
python3 random_generation.py

##Reading through the file
Start at random_generation.py (really the only file)

##Testing
You can run this script interactive to test the functions!
python3 -i random_generation.py

I also ran out of queries in the middle of writing up the sound
query so I wrote gen_test_input(low, high, size) in order to
simulate data. If I did this wrong then all my script may be broken!
Crossing my fingers!


##Credits
CREDIT TO https://github.com/sole/snippets/blob/master/audio/generate_noise_test_python/script.py
SOLEDAD PENADÉS for starter code for writing audio file