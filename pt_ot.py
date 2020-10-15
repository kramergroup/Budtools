# This mini library for onetep stuff - including some ngwf info. this will be ported in from the main pt stuff but it's
# put seperately cause im lazy and this stuff is confuisng

# ONETEP HAS FORMAT; species
# needs a elenumber. symbol, and ngwf info - most of this is done except the ngwf stuff so here is that stuff below.
# It seems finnicky what ngfw you should choose so i'll fiddle with it.

# Ngwfnumber is dependant on the psuedopot used, I am slowly (with my systems anyway) adding those that seem to give
# decent results on onetep

## Re-format things so its less lines and just make it call from PSONETEP/psutype/psufile - might be better.

#Maingroup - p orbs have 4 i guess - infact can probs set all of these to 4
H_ot = {
    "ngwf_num": 2,
    "ngwf_rad": 6.0,
    "psu_recpot": '"~/PSONETEP/Hydrogennotdefined"',  #
    "psu_paw": '"~/PSONETEP/Hydrogennotdefined"'  #
}

He_ot = {

}


# Convergence tests on a 100 atom lco system show that ngwfnum 5, ngwfrad 3.5 is adequate
Li_ot = {
    "ngwf_num": 5,
    "ngwf_rad": 6.0,
    "psu_recpot": '"~/PSONETEP/li-krgga6.recpot"',
    "psu_paw": '"~/PSONETEP/li_pbe_v1_abinit.paw"'
}

Be_ot = {
    "ngwf_num": 4,
    "ngwf_rad": 6.0
}

# Convergence tests on a 108 atom LCO system show that ngwf_num 4, ngwf_rad 3.5 is adequate
O_ot = {
    "ngwf_num": 4,
    "ngwf_rad": 6.0,
    "psu_recpot": '"~/PSONETEP/o-optgga1.recpot"',
    "psu_paw": '"~/PSONETEP/o_pbe_v1.2_abinit.paw"'
}
# Generally tms can just have these values, it might work out that you need to reduce the rad if your cells are small
Mn_ot = {
    "ngwf_num": 14,
    "ngwf_rad": 6.0,
    "psu_paw": '"~/PSONETEP/Mn.PBE-paw.abinit"',
    "psu_recpot": '"~/PSONETEP/Mangenesenotdefined"' #
}

#Convergence tests on a 108 LCO system show that ngwf num 14, ngwf rad 5.0 is adequate.
Co_ot = {
    "ngwf_num": 14,
    "ngwf_rad": 6.0,
    "psu_recpot": '"~/PSONETEP/co-optgga1.recpot"',
    "psu_paw": '"~/PSONETEP/co_pbe_v1.2_abinit.paw"'
}

Ni_ot = {
    "ngwf_num": 18,
    "ngwf_rad": 6.0,
    "psu_paw": '"~/PSONETEP/ni_pbe_v1_abinit.paw"',
    "psu_recpot": '"~/PSONETEP/Nicklenotdefined"'  #
}

Mn_ot = {
    "ngwf_num": 18,
    "ngwf_rad": 6.0,
    "psu_recpot": '"~/PSONETEP/Mangenesenotdefined"',  #
    "psu_paw": '"~/PSONETEP/mn_pbe_v1.2_abinit.paw"'
}




# Set of potentially useful onetep ngwf values, not sure how correct they are but they should be somewhat decent. As 
# always probs need conv on these but this is just a tool to quickly make onetep inputs so it doesn't matter.

## sblock one below
s_ot = {
    "ngwf_num": 4,
    "ngwf_raf": 6.0
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
