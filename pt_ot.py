# This mini library for onetep stuff - including some ngwf info. this will be ported in from the main pt stuff but it's
# put seperately cause im lazy and this stuff is confuisng

# ONETEP HAS FORMAT; species
# needs a elenumber. symbol, and ngwf info - most of this is done except the ngwf stuff so here is that stuff below.
# It seems finnicky what ngfw you should choose so i'll fiddle with it.

# Ngwfnumber is dependant on the psuedopot used, I am slowly (with my systems anyway) adding those that seem to give
# decent results on onetep



#Maingroup - p orbs have 4 i guess - infact can probs set all of these to 4
H_ot = {
    "ngwf_num": 2,
    "ngwf_rad": 6.0,
    "psu": '"~/PSONETEP/Hydrogennotdefined"'
}

He_ot = {

}


# Convergence tests on a 100 atom lco system show that ngwfnum 5, ngwfrad 3.5 is adequate
Li_ot = {
    "ngwf_num": 5,
    "ngwf_rad": 9.0,
    "psu": '"~/PSONETEP/li-krgga6.recpot"'
}

Be_ot = {
    "ngwf_num": 4,
    "ngwf_rad": 6.0
}

# Convergence tests on a 108 atom LCO system show that ngwf_num 4, ngwf_rad 3.5 is adequate
O_ot = {
    "ngwf_num": 4,
    "ngwf_rad": 9.0,
    "psu": '"~/PSONETEP/o-optgga1.recpot"'
}
# Generally tms can just have these values, it might work out that you need to reduce the rad if your cells are small
Mn_ot = {
    "ngwf_num": 14,
    "ngwf_rad": 9.0,
    "psu": '"~/PSONETEP/Mn.PBE-paw.abinit"'
}

#Convergence tests on a 108 LCO system show that ngwf num 14, ngwf rad 5.0 is adequate.
Co_ot = {
    "ngwf_num": 14,
    "ngwf_rad": 9.0,
    "psu": '"~/PSONETEP/co-optgga1.recpot"'
}

Ni_ot = {
    "ngwf_num": 14,
    "ngwf_rad": 9.0,
    "psu": '"~/PSONETEP/Ni.PBE-paw.abinit"'
}



# Set of potentially useful onetep ngwf values, not sure how correct they are but they should be somewhat decent. As 
# always probs need conv on these but this is just a tool to quickly make onetep inputs so it doesn't matter.

## sblock one below
s_ot = {
    "ngwf_num":4,
    "ngwf_raf":6.0
}
## pblock one below
p_ot = {
    "ngwf_num": 4,
    "ngwf_rad": 6.0
}

# dblock one below
d_ot = {
    "ngwf_num": 10,
    "ngwf_rad:": 6.0
}

# fblock one below
f_ot = {
    "ngwf_num": 18,
    "ngwf_rad:": 6.0
}
