# Powerpoint Karaoke Generator
Assigns Slidedecks randomly PowerpointKaraoke Players

# Usage
* Put the slidedecks into the `slidedecks` folder. Note: The filenames need to comply with the following nameing convention:
  `<Creator_name>-<Identifier>.<File extention>`
* Run `./powerpointshuffle.py` or `python powerpointshuffle.py`. This generates something along those lines:
```
### Initial Setting ###
Edsger_Dijkstra      -> foobar.pdf
Donald_Knuth         -> grokbaz.pdf
Alan_Turing          -> bargrok.pdf

### New Setting ###
Donald_Knuth         -> foobar.pdf
Alan_Turing          -> grokbaz.pdf
Edsger_Dijkstra      -> bargrok.pdf 
```
