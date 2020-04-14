from pt import pt
import re
from i_functions import vprint
import os

# Since the onetepconv master availible from the onetep utils seems to be somewhat broken in its ability to actually
# make files correctly i've instead taken it into my own hands to wewrite it however my bash skills are severly limited
# and i refuse to use awk unironically when string handling can be around 800x simplier


# Would be wise to have this onetep conv maker thing magic directly from one onetep input file even though
# technically you could use my vasp convergence generator funciton followed by my vasp2onetep

# from what i remember my vasp convergence stuff is largely for slabs and encut can be easily varied with a bash for
# loop and thus is probs unneccessary so, having a way to vary the onetep only params would be good

# 1. ngwf radius.
# 2. number of ngwfs
# 3. cut off energy (this is the only non-broken call from the onetepmaster so will be last of my priority)

# the cool thing is it can techincally use my library for a good starting point for ngwf info and additionally then work
# from there to update the library (a long way off) but is a potentially cool feature.

# As of current the ngwf info is set to false because i'm assumign that the onetep input file you've added is there
# because you're smarter than me

# So clearly the plan to write a bit of code that what onetepconv does proved a little difficult nonetheless this is
# roughly done for the simple cases - will now add the more difficult cases and move on from there. Simples ;)


# TODO add the difficult cases and add a use me thingy magic.
# TODO add a plotting tool like that seen in onetepconvmaster/libs/csv thingy should be fairly simple.
# Actually todo number 2 maybe over kill since the onetepmaster conv call seems to work somewhatwell.
# TODO make it create a small text file at output dir with the input params so people can see what it's done.
# TODO change the os.mkdirs to os.makedirs(pathexists = ok) as seen in other code.
def conv_ngwf_num(input_file, outputdir, numbersteps=4, uselibs=False, simple=True, verbose=True, checkfold=True):
    # Am i going to need a catch all for people using %block vs %BLOCK lets pray not team - ok this is done cusae
    # life is hard
    if uselibs == True:
        print(
            'uselibs has been read as True, this will use the ngwf num defined in Buds pt. Switch this off to use the '
            'initial ngwfs within the file.')

    print('if your result is wildly different from that seen in the pt consider changing the pt for future users')
    if checkfold:
        if len(os.listdir(outputdir)) > 3:
            print('alot of things exist in this directory - i suggest you set your output dir as a clean folder.')
            exit()

    # First step - hunt for the %block species and %endblock species and read the bits inbetween.
    f = open(input_file)
    liz = []  # The unfiltered list, i put this here incase anyone is having problems, it's unused but w/e
    lizstrip = []
    for line in f:  # Seems easiest for my mental sanity to just write whole thing to list. I was trying some goofy thing
        line2 = re.sub(r"\s+$", "", line)  # we all hate regex! but this should make the stringsearch consistant - the
        # plan to not use awk has at this point seemed futile
        if line2.startswith('%'):
            vprint(line2, verbose)
            line2 = line2.upper()  # Incase someone puts things in iwth lower case which may cause issues.
        lizstrip.append(line2)
        liz.append(line)  # write the original file to a list to another file just to make sure.
        vprint('file is opened and written', verbose)
        vprint('lines in file = ' + str(len(lizstrip)), verbose)
    # Second step. new list, that will To those looking for efficiency, i attempted the following as a list
    # comprehension however got confused and decided to use the codemallet.
    low = lizstrip.index("%BLOCK SPECIES")
    high = lizstrip.index("%ENDBLOCK SPECIES")
    changelist = lizstrip[low:high + 1]  # generate a new list to be changed.

    # Boom got all the stuff i need. #Ignore this, its dumb
    # for element in changelist[1:-1]:
    #    print(element)

    os.mkdir(outputdir + '/ngwf_num')
    # Checking my dictionary if the flag is raised.
    if simple:
        vprint('simple mode is on', verbose)
        counter = 0
        vprint('vvvvvv iteration number vvvvvv', verbose)
        vprint(counter, verbose)
        while counter < numbersteps:
            newlist = ['%BLOCK SPECIES']
            if uselibs:
                for element in changelist:  # This way seemed easier than comment above
                    if not element.startswith('%'):
                        vprint(element.split(' ')[0] + ' is being changed', verbose)
                        if pt.get(element.split(' ')[0]).get('name'):
                            vprint(pt.get(element.split(' ')[0]).get('name') + ' has been found in dictionary', verbose)
                            vprint(element.split(' ')[3], verbose)
                            vprint('dictionary rec ngwf num for ' + element.split(' ')[0] + ' = ' + str(
                                pt.get(element.split(' ')[0]).get('ot').get('ngwf_num')), verbose)
                            # lets take a minute to appreciate the .format call in python. god sick.
                            newlist.append('{0} {1} {2} {3} {4}'.format(element.split(' ')[0],
                                                                        element.split(' ')[1],
                                                                        element.split(' ')[2],
                                                                        pt.get(element.split(' ')[0]).get('ot').get(
                                                                            'ngwf_num') - 1 + counter,
                                                                        # This -1 may cause issues later?
                                                                        element.split(' ')[4]))
                        else:
                            print(element.split(' ') + ' element not found - im gunna die now')
            else:
                vprint('uselibs has been set to false using the inputfile as initial ngwf number', verbose)
                for element in changelist:  # This way seemed easier than comment above
                    if not element.startswith('%'):
                        vprint(element.split(' ')[0] + ' is being changed', verbose)
                        if pt.get(element.split(' ')[0]).get('name'):
                            vprint(pt.get(element.split(' ')[0]).get('name') + ' has been found in dictionary', verbose)
                            vprint(element.split(' ')[3], verbose)
                            # lets take a minute to appreciate the .format call in python. god sick.
                            newlist.append('{0} {1} {2} {3} {4}'.format(element.split(' ')[0],
                                                                        element.split(' ')[1],
                                                                        element.split(' ')[2],
                                                                        str(int(element.split(' ')[3]) - 1 + counter),
                                                                        element.split(' ')[4]))
                        else:
                            print(element.split(' ') + ' element not found - im gunna die now')

            newlist.append('%ENDBLOCK SPECIES')  # Put the endblock on

            lizstrip[low:high + 1] = newlist  # Put the changed values in
            os.mkdir(outputdir + '/ngwf_num/' + str(counter))
            with open(outputdir + '/ngwf_num/' + str(counter) + '/ngwf_num.dat', "w") as outfile:  # Write it bois
                outfile.write("\n".join(lizstrip))
            vprint(counter, verbose)
            counter += 1
    else:
        vprint('a non-simple mode has not been coded yet pest bud to do it', verbose)
    vprint('seems to be all done - ' + str(counter) + ' folders made', verbose)
    print('if your result is wildly different from that seen in the pt consider changing the pt for future users')


def conv_ngwf_rad(input_file, outputdir, numbersteps=4, stepsize=0.5, uselibs=False, simple=True, verbose=True,
                  checkfold=True):
    if uselibs == True:
        print(
            'uselibs has been read as True, this will use the ngwf num defined in Buds pt. Switch this off to use the '
            'initial ngwfs within the file.')

    # Am i going to need a catch all for people using %block vs %BLOCK lets pray not team - ok this is done cusae life is hard
    if uselibs == True:
        print(
            'uselibs has been read as True, this will use the ngwf num defined in Buds pt. Switch this off to use the '
            'initial ngwfs within the file.')

    print('if your result is wildly different from that seen in the pt consider changing the pt for future users')
    if checkfold:
        if len(os.listdir(outputdir)) > 3:
            print('alot of things exist in this directory - i suggest you set your output dir as a clean folder.')
            exit()

    # First step - hunt for the %block species and %endblock species and read the bits inbetween.
    f = open(input_file)
    liz = []  # The unfiltered list, i put this here incase anyone is having problems, it's unused but w/e
    lizstrip = []
    for line in f:  # Seems easiest for my mental sanity to just write whole thing to list. I was trying some goofy thing
        line2 = re.sub(r"\s+$", "", line)  # we all hate regex! but this should make the stringsearch consistant - the
        # plan to not use awk has at this point seemed futile
        if line2.startswith('%'):
            vprint(line2, verbose)
            line2 = line2.upper()  # Incase someone puts things in iwth lower case which may cause issues.
        lizstrip.append(line2)
        liz.append(line)  # write the original file to a list to another file just to make sure.
        vprint('file is opened and written', verbose)
        vprint('lines in file = ' + str(len(lizstrip)), verbose)
    # Second step. new list, that will To those looking for efficiency, i attempted the following as a list
    # comprehension however got confused and decided to use the codemallet.
    low = lizstrip.index("%BLOCK SPECIES")
    high = lizstrip.index("%ENDBLOCK SPECIES")
    changelist = lizstrip[low:high + 1]  # generate a new list to be changed.

    # Boom got all the stuff i need. #Ignore this, its dumb
    # for element in changelist[1:-1]:
    #    print(element)

    os.mkdir(outputdir + '/ngwf_rad')
    # Checking my dictionary if the flag is raised.
    if simple:
        vprint('simple mode is on', verbose)
        counter = 0
        vprint('vvvvvv iteration number vvvvvv', verbose)
        vprint(counter, verbose)
        while counter < numbersteps:
            newlist = ['%BLOCK SPECIES']
            if uselibs:
                for element in changelist:  # This way seemed easier than comment above
                    if not element.startswith('%'):
                        vprint(element.split(' ')[0] + ' is being changed', verbose)
                        if pt.get(element.split(' ')[0]).get('name'):
                            vprint(pt.get(element.split(' ')[0]).get('name') + ' has been found in dictionary', verbose)
                            vprint(element.split(' ')[3], verbose)
                            vprint('dictionary rec ngwf num for ' + element.split(' ')[0] + ' = ' + str(
                                pt.get(element.split(' ')[0]).get('ot').get('ngwf_num')), verbose)
                            # lets take a minute to appreciate the .format call in python. god sick.
                            newlist.append('{0} {1} {2} {3} {4}'.format(element.split(' ')[0],
                                                                        element.split(' ')[1],
                                                                        element.split(' ')[2],
                                                                        element.split(' ')[3],
                                                                        pt.get(element.split(' ')[0]).get('ot').get(
                                                                            'ngwf_rad') + (counter * stepsize)))
                            # This -1 may cause issues later?

                        else:
                            print(element.split(' ') + ' element not found - im gunna die now')
            else:
                vprint('uselibs has been set to false using the inputfile as initial ngwf number', verbose)
                for element in changelist:  # This way seemed easier than comment above
                    if not element.startswith('%'):
                        vprint(element.split(' ')[0] + ' is being changed', verbose)
                        if pt.get(element.split(' ')[0]).get('name'):
                            vprint(pt.get(element.split(' ')[0]).get('name') + ' has been found in dictionary', verbose)
                            vprint(element.split(' ')[3], verbose)
                            # lets take a minute to appreciate the .format call in python. god sick.
                            newlist.append('{0} {1} {2} {3} {4}'.format(element.split(' ')[0],
                                                                        element.split(' ')[1],
                                                                        element.split(' ')[2],
                                                                        element.split(' ')[3],
                                                                        str(int(element.split(' ')[4]) + (
                                                                                    counter * stepsize))))
                        else:
                            print(element.split(' ') + ' element not found - im gunna die now')

            newlist.append('%ENDBLOCK SPECIES')  # Put the endblock on

            lizstrip[low:high + 1] = newlist  # Put the changed values in
            os.mkdir(outputdir + '/ngwf_rad/' + str(counter))
            with open(outputdir + '/ngwf_rad/' + str(counter) + '/ngwf_rad.dat', "w") as outfile:  # Write it bois
                outfile.write("\n".join(lizstrip))
            vprint(counter, verbose)
            counter += 1
    else:
        vprint('a non-simple mode has not been coded yet pest bud to do it', verbose)
    vprint('seems to be all done - ' + str(counter) + ' folders made', verbose)
    print('if your result is wildly different from that seen in the pt consider changing the pt for future users')
