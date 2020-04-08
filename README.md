# Budtools
Some simple vasp/oneep tools that've been written painstakingly

Some simple python tools (of which the names make rough sense) enclosed in i_functions. Mostly making input files quickly.

It's all fairly well documented and should make sense and uses a poorly managed pt library. Why i didn't make it use the pmg one from the start is beyond me, apparently i'm hopeless.

It's pretty good at taking an input bulk crystal structure, cleaving it and generating  convergence tests and all vasprun files aswell as a finnicky version of a onetep run (onetep is probably a bit dodge)

KEYNOTE - pymatgen can sometimes suck, it seems to switch between cleavage modes somewhat randomly. I'll try to figure it out.

- B
